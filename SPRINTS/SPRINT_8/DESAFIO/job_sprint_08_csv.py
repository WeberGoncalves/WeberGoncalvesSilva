import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark.sql.functions import current_date, year, month, dayofmonth, col, trim
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

# Inicialização do contexto Glue
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()  # Criando SparkContext
glueContext = GlueContext(sc)  # Criando GlueContext
spark = glueContext.spark_session  # Criando SparkSession a partir do Glue Context
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminhos S3
raw_s3_path = "s3://data-lake-do-weber/RAW/Local/CSV/Movies/2024-11-06/movies.csv"
trusted_s3_path = "s3://data-lake-do-weber/TRUSTED/Parquet/"

# Definição do esquema explícito para o arquivo CSV
schema = StructType([
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

# Lendo dados CSV com esquema definido
raw_data_df = spark.read.csv(
    path=raw_s3_path,
    schema=schema,
    header=True,
    sep=","
)

# Redução e limpeza de colunas
columns_to_select = [
    "tituloOriginal", "anoLancamento", "genero", 
    "notaMedia", "numeroVotos", "generoArtista", 
    "personagem", "nomeArtista"
]

cleaned_data_df = raw_data_df.select(*columns_to_select) \
    .withColumn("tituloOriginal", trim(col("tituloOriginal"))) \
    .withColumn("genero", trim(col("genero"))) \
    .withColumn("generoArtista", trim(col("generoArtista"))) \
    .withColumn("personagem", trim(col("personagem"))) \
    .withColumn("nomeArtista", trim(col("nomeArtista")))

# Adicionando metadados
trusted_data = cleaned_data_df \
    .withColumn("data_criacao", current_date()) \
    .withColumn("ano", year(current_date())) \
    .withColumn("mes", month(current_date())) \
    .withColumn("dia", dayofmonth(current_date()))

# Persistindo os dados na camada Trusted no formato PARQUET, particionados por ano/mês/dia
trusted_data.write.mode("overwrite").partitionBy("ano", "mes", "dia").format("parquet").save(trusted_s3_path)

print(f"Dados processados e salvos na camada Trusted no caminho: {trusted_s3_path}")

# Commit do job Glue
job.commit()
