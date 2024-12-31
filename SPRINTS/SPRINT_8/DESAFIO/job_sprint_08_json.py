import sys
from datetime import datetime
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions
from awsglue.job import Job
from pyspark.sql.functions import year, month, dayofmonth, current_date

# Inicialização do contexto Glue
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

# Criando o contexto do Spark e do Glue
sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminho para o arquivo S3 diretamente
s3_input_path = "s3://data-lake-do-weber/RAW/TMDB/json/2024/12/17/"
trusted_json_path = "s3://data-lake-do-weber/TRUSTED/JSON/{ano}/{mes}/{dia}"

# Lendo dados diretamente do S3 com opção 'multiline' caso o arquivo tenha múltiplas linhas JSON
raw_data = spark.read.option("multiline", "true").json(s3_input_path)

# Verificar e renomear colunas duplicadas
available_columns = raw_data.columns
unique_columns = []
duplicate_columns = []

for column in available_columns:
    if column in unique_columns:
        duplicate_columns.append(column)
    else:
        unique_columns.append(column)

for dup_col in duplicate_columns:
    raw_data = raw_data.withColumnRenamed(dup_col, f"{dup_col}_renamed")

# Selecionar apenas as colunas desejadas
selected_columns = ["titulo", "ano", "genero", "numero_de_votos", "nota_media", "nome_artistico", "orcamento", "receita"]

# Verificar se as colunas existem no DataFrame
missing_columns = [col for col in selected_columns if col not in raw_data.columns]
if missing_columns:
    print(f"As seguintes colunas estão faltando no DataFrame: {', '.join(missing_columns)}")
    raw_data.show(5)
else:
    final_data = raw_data.select(*selected_columns)

    # Remover duplicatas
    final_data = final_data.dropDuplicates()

    # Obtendo a data atual
    data_atual = datetime.now()
    ano = data_atual.year
    mes = str(data_atual.month).zfill(2)  
    dia = str(data_atual.day).zfill(2)

    # Corrigindo o caminho para salvar
    trusted_json_path_final = trusted_json_path.format(ano=ano, mes=mes, dia=dia)

    # Salvando os dados no formato Parquet no caminho especificado
    final_data.write.mode("overwrite").format("parquet").save(trusted_json_path_final)

# Finalizar o Job
job.commit()

