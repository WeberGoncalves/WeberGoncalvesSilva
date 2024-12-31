import sys
from datetime import datetime
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark.sql.functions import current_date, year, col, trim, row_number
from pyspark.sql.window import Window
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

# Inicialização do contexto Glue
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
contexto_spark = SparkContext()
contexto_glue = GlueContext(contexto_spark)
spark = contexto_glue.spark_session
job = Job(contexto_glue)
job.init(args['JOB_NAME'], args)

# Caminhos S3
caminho_raw_s3 = "s3://data-lake-do-weber/RAW/Local/CSV/Movies/2024-11-06/movies.csv"
caminho_trusted_s3 = "s3://data-lake-do-weber/TRUSTED/CSV/{ano}/{mes}/{dia}"

# Definição do esquema explícito para o arquivo CSV
esquema = StructType([
    StructField("id", StringType(), True),
    StructField("tituloPrincipal", StringType(), True),
    StructField("tituloOriginal", StringType(), True),
    StructField("anoLancamento", IntegerType(), True),
    StructField("tempoMinutos", IntegerType(), True),
    StructField("genero", StringType(), True),
    StructField("notaMedia", DoubleType(), True),
    StructField("numeroVotos", IntegerType(), True),
    StructField("generoArtista", StringType(), True),
    StructField("personagem", StringType(), True),
    StructField("nomeArtista", StringType(), True),
    StructField("anoNascimento", IntegerType(), True),
    StructField("anoFalecimento", IntegerType(), True),
    StructField("profissao", StringType(), True),
    StructField("titulosMaisConhecidos", StringType(), True),
])

# Lendo dados CSV com esquema definido e separador de coluna "|"
dados_raw_df = spark.read.csv(
    path=caminho_raw_s3,
    schema=esquema,
    header=True,
    sep="|"
)

# Seleção das colunas desejadas
colunas_para_selecionar = [
    "tituloPrincipal", "anoLancamento", "genero", "notaMedia", "numeroVotos", "generoArtista", "nomeArtista"
]
dados_limpos_df = dados_raw_df.select(*colunas_para_selecionar) \
    .withColumn("tituloPrincipal", trim(col("tituloPrincipal"))) \
    .withColumn("genero", trim(col("genero"))) \
    .withColumn("generoArtista", trim(col("generoArtista"))) \
    .withColumn("nomeArtista", trim(col("nomeArtista")))

# Filtrando os 30 filmes do gênero crime com maiores notaMedia, dos últimos 40 anos
ano_atual = year(current_date())
dados_filtrados_df = dados_limpos_df.filter(
    (col("genero") == "Crime") & (col("anoLancamento") >= ano_atual - 40)
).orderBy(col("notaMedia").desc()).limit(1000)

# Removendo duplicatas para garantir títulos originais únicos
especificacao_janela = Window.partitionBy("tituloPrincipal").orderBy(col("notaMedia").desc())
titulos_unicos_df = dados_filtrados_df.withColumn("numero_linha", row_number().over(especificacao_janela)) \
    .filter(col("numero_linha") == 1).drop("numero_linha")

# Define dados_trusted
dados_trusted = titulos_unicos_df

# Obtendo a data atual
data_atual = datetime.now()
ano = data_atual.year
mes = str(data_atual.month).zfill(2)  
dia = str(data_atual.day).zfill(2)

# Caminho para salvar dados particionados
caminho_trusted_final = caminho_trusted_s3.format(ano=ano, mes=mes, dia=dia)

# Persistindo os dados na camada Trusted no formato PARQUET, particionados por ano/mês/dia corrente
dados_trusted.write.mode("overwrite").format("parquet").save(caminho_trusted_final)

job.commit()
