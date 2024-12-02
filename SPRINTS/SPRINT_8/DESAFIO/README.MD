## Seção 04 Desafio da sprint

**Neste desafio foi realizado com script em pyspark no Job no Glue, para realizar limpeza e salvar na extensão parquet no S3 AWS, isso ocorreu tanto no arquivo CSV como JSON.**

**Scriptno Job Glue processar arquivo CSV.**
**Este script é utilizado para processar dados de um arquivo CSV, limpá-los, transformá-los e armazená-los em um formato otimizado (Parquet) na camada Trusted do Data Lake, mantendo uma estrutura organizada e pronta para análises futuras.**

```yaml annotate
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
schema = StructType(
[
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
raw_data_df = spark.read.csv(
    path=raw_s3_path,
    schema=schema,
    header=True,
    sep=","
)
columns_to_select =
[
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

trusted_data.write.mode("overwrite").partitionBy("ano", "mes", "dia").format("parquet").save(trusted_s3_path)

print(f"Dados processados e salvos na camada Trusted no caminho: {trusted_s3_path}")

# Commit do job Glue
job.commit()

```
**Evidência 01 - .**

![weber](/SPRINTS/SPRINT_8/EVIDÊNCIAS/Desafio/sprint_08_csv_1.png)

**Evidência 02 - .**

![weber](/SPRINTS/SPRINT_8/EVIDÊNCIAS/Desafio/sprint_08_csv_2.png)

**Evidência 03 - .**

![weber](/SPRINTS/SPRINT_8/EVIDÊNCIAS/Desafio/sprint_08_csv_3.png)

**Evidência 04 - .**

![weber](/SPRINTS/SPRINT_8/EVIDÊNCIAS/Desafio/sprint_08_csv_4.png)

**Evidência 05 - .**

![weber](/SPRINTS/SPRINT_8/EVIDÊNCIAS/Desafio/sprint_08_csv_5.png)

**Scriptno Job Glue processar arquivo JON.**
**O script é responsável por ler dados JSON de uma localização no S3, processar e limpar esses dados, transformá-los conforme necessário e salvá-los em formato Parquet na camada Trusted do S3, com atualizações no Glue Data Catalog para facilitar consultas futuras.**
```yaml annotate
import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions
from awsglue.job import Job
from pyspark.sql.functions import current_date, year, month, dayofmonth, lit, col, when, struct, array, explode
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.types import IntegerType

# Inicialização do contexto Glue
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
print(f"Parâmetros do job: {args}")  # Log dos parâmetros recebidos

# Criando o contexto do Spark e do Glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)  # Inicializando o job

# Caminho para o arquivo S3 diretamente
s3_input_path = "s3://data-lake-do-weber/RAW/TMDB/json/2024/11/28/filmes_1.json"
trusted_s3_path = "s3://data-lake-do-weber/TRUSTED/JSON/"
glue_database = "bd_sprint_08_csv"
glue_table_trusted = "tmdb_trusted"

# Lendo dados diretamente do S3 (sem Glue Catalog) com opção 'multiline' caso o arquivo tenha múltiplas linhas JSON
raw_data = spark.read.option("multiline", "true").json(s3_input_path)  # Lê os dados JSON diretamente do S3
print(f"Dados carregados com sucesso de '{s3_input_path}'.")

# Verificando o esquema dos dados
print("Esquema dos dados carregados:")
raw_data.printSchema()

print("Amostra inicial dos dados:")
raw_data.show(5)

# Verifique as colunas disponíveis no DataFrame
available_columns = raw_data.columns
print(f"Colunas disponíveis: {available_columns}")

# Exploda a coluna 'artistas' se ela existir
if "artistas" in available_columns:
    raw_data = raw_data.withColumn("artista_explodido", explode(col("artistas")))

    raw_data = raw_data.select(
        col("titulo_original"),
        col("ano_lancamento"),
        col("genero"),
        col("nota_media"),
        col("numero_votos"),
        col("artista_explodido.genero_artista").alias("genero_artista"),
        col("artista_explodido.nome_artista").alias("nome_artista"),
        col("artista_explodido.personagem").alias("personagem")
    )
    raw_data.show(5)
else:
    print("A coluna 'artistas' não está disponível no DataFrame.")
    raw_data.show(5)  # Verificar a amostra dos dados

# Remova linhas com valores nulos em `nome_artista` e `genero_artista` se existirem
if all(col in available_columns for col in ["nome_artista", "genero_artista"]):
    cleaned_data = raw_data.dropna(subset=["nome_artista", "genero_artista"])
else:
    cleaned_data = raw_data
    print("As colunas 'nome_artista' ou 'genero_artista' não estão disponíveis no DataFrame.")

# Remover duplicatas
cleaned_data = cleaned_data.dropDuplicates()

# Filtrar valores em `nota_media` se a coluna existir
if "nota_media" in available_columns:
    cleaned_data = cleaned_data.filter(col("nota_media").isNotNull() & (col("nota_media") >= 0))
else:
    print("A coluna 'nota_media' não está disponível no DataFrame.")

print(f"Número de registros após limpeza: {cleaned_data.count()}")
cleaned_data.show(5)  # Verificar a amostra dos dados após limpeza

# Transformações nos dados
trusted_data = cleaned_data.withColumn("data_criacao", current_date()) \
    .withColumn("ano", year(current_date())) \
    .withColumn("mes", month(current_date())) \
    .withColumn("dia", dayofmonth(current_date()))
print("Transformações aplicadas com sucesso.")

# Verificar o número de registros transformados
print(f"Número de registros após transformações: {trusted_data.count()}")
trusted_data.show(5)  # Verificar a amostra dos dados após transformações

# Salvando os dados no formato Parquet
trusted_data.write.mode("overwrite").partitionBy("ano", "mes", "dia").format("parquet").save(trusted_s3_path)
print(f"Dados processados e salvos com sucesso na camada Trusted no caminho: {trusted_s3_path}")

# Converter para DynamicFrame para atualizar o Glue Data Catalog
dyf_trusted = DynamicFrame.fromDF(trusted_data, glueContext, "dyf_trusted")
glueContext.write_dynamic_frame.from_options(
    frame=dyf_trusted,
    connection_type="s3",
    connection_options={"path": trusted_s3_path},
    format="parquet"
)
print("Glue Data Catalog atualizado com sucesso.")

# Finalizar o Job
job.commit()
```
**Evidência 06 - .**

![weber](/SPRINTS/SPRINT_8/EVIDÊNCIAS/Desafio/sprint_08_json_1.png)

**Evidência 06 - .**

![weber](/SPRINTS/SPRINT_8/EVIDÊNCIAS/Desafio/sprint_08_json_2.png)

**Evidência 06 - .**

![weber](/SPRINTS/SPRINT_8/EVIDÊNCIAS/Desafio/sprint_08_json_3.png)

**Evidência 06 - .**

![weber](/SPRINTS/SPRINT_8/EVIDÊNCIAS/Desafio/sprint_08_json_4.png)