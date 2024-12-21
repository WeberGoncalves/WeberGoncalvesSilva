# DESAFIO
## Seção 04 Desafio da sprint

**Neste desafio foi realizado com script em pyspark no Job no Glue, foi realizado algumas limpezas dos dados, para depois juntas os Dataframes originados dos arquivos CSV e JSON.**

**Script no Job Glue processar arquivo da junção e Modelagem.**
**Neste script separarei cada tarefa a ser feita por funções, ler arquivos, limpar, juntar, filtrar e criar tabelas modeladas e salvar no bucket, aproveite consertei os caminhos(ano/mês/dia) job_csv e job_json, conforme o Feedback Técnico.**

##**Script para serviço de ETL**

**O script apresentado  uma série de etapas de processamento para preparar dados para análise, desenvolvido para ser executada no AWS Glue, um serviço de ETL (Extract, Transform, Load) da Amazon. Ele utiliza o AWS Glue e PySpark para processar dados de filmes, transformar e salvar dados em um Data Lake armazenado no Amazon S3**

**Foi criado varias funções para realizar as tarefas a ser feitas, Função para ler os arquivos Parquet no S3; Função para limpar os títulos dos filmes, Removendo os caracteres específicos.**

**Função para filtrar e juntar os DataFrames, ela também Renomeia as colunas para garantir consistência, faz  Seleção das colunas necessárias.**

**Função para inserir dados nas tabelas, que também criau a Dimensão de filmes, Adicionou o id_filme ao DataFrame principal, criou Dimensão de tempo,Dimensão artística e tabela Fato.**

**Ainda na Função para inserir dados, também Defininiu os caminhos para salvar os dados com a interpolação correta. Salvou os dados nos respectivos caminhos.**
**por fora da função ocorre a Execução das funções principais.**

**Algoritmo Completo**
```yaml annotate
import sys
from datetime import datetime
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, regexp_replace, row_number, when
from pyspark.sql.window import Window

# Inicialização do Glue Context
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
job.init(args['JOB_NAME'], args)

# Configuração de logs para CloudWatch
logGroupName = '/aws-glue/jobs/logs-v2'
logStreamNamePrefix = args['JOB_NAME']

def ler_arquivos_parquet():
    caminho_parquet_csv = "s3://data-lake-do-weber/TRUSTED/CSV/2024/12/17/"
    caminho_parquet_json = "s3://data-lake-do-weber/TRUSTED/JSON/2024/12/17/"
    df_csv = spark.read.parquet(caminho_parquet_csv)
    df_json = spark.read.parquet(caminho_parquet_json)
    return df_csv, df_json

def limpar_titulos(df):
    titulos = ['tituloPrincipal', 'titulo']
    for titulo in titulos:
        if titulo in df.columns:
            df = df.withColumn(
                titulo,
                regexp_replace(titulo, r'[\",!&\.\.:\?\[\]]', '')  
            )
    return df

def filtrar_e_juntar_dataframes(df_csv, df_json):
    df_csv = limpar_titulos(df_csv)
    df_json = limpar_titulos(df_json)

    df_csv = df_csv.withColumnRenamed('anoLancamento', 'ano')
    df_json = df_json.withColumnRenamed('ano', 'ano_json')

    # Junção dos DataFrames
    df_filtrado = df_csv.join(df_json, df_csv['ano'] == df_json['ano_json'], 'inner')

    # Seleção das colunas necessárias
    df_junto = df_filtrado.select(
        col('tituloPrincipal').alias('titulo'),
        col('ano'),
        col('notaMedia').alias('nota_media'),
        col('numeroVotos').alias('numero_de_votos'),
        col('generoArtista').alias('genero_artista'),
        col('nomeArtista').alias('nome_artistico'),
        col('orcamento'),
        col('receita')
    )
    return df_junto

def inserir_dados(df_filtrado):
    df_dim_filme = df_filtrado.select("titulo").distinct() \
        .withColumn("id_filme", row_number().over(Window.orderBy("titulo"))) \
        .select("id_filme", "titulo")

    df_filtrado = df_filtrado.join(df_dim_filme, on="titulo", how="inner")

    df_dim_tempo = df_filtrado.select("ano").distinct() \
        .withColumn("id_tempo", row_number().over(Window.orderBy("ano"))) \
        .withColumn(
            "decada",
            when((col("ano") >= 1980) & (col("ano") <= 1989), '80')
            .when((col("ano") >= 1990) & (col("ano") <= 1999), '90')
            .when((col("ano") >= 2000) & (col("ano") <= 2009), '2000')
            .when((col("ano") >= 2010) & (col("ano") <= 2019), '2010')
            .when((col("ano") >= 2020) & (col("ano") <= 2029), '2020')
            .otherwise('Desconhecido')
        ) \
        .select("id_tempo", "ano", "decada")

    df_dim_artistico = df_filtrado.select("nome_artistico", "genero_artista").distinct() \
        .withColumn("id_artistico", row_number().over(Window.orderBy("nome_artistico"))) \
        .select("id_artistico", "nome_artistico", "genero_artista")

    df_fato_filme = df_filtrado.join(df_dim_tempo, on="ano", how="inner") \
        .join(df_dim_artistico, on=["nome_artistico", "genero_artista"], how="inner") \
        .select(
            col("id_filme"),
            col("id_tempo"),
            col("id_artistico"),
            col("orcamento"),
            col("receita"),
            col("numero_de_votos").alias("numero_votos"),
            col("nota_media")
        ).withColumn("id_fato", row_number().over(Window.orderBy("id_filme"))) \
        .select("id_fato", "id_filme", "id_tempo", "id_artistico", "orcamento", "receita", "numero_votos", "nota_media")
    
    # Obtendo a data atual
    data_atual = datetime.now()
    ano = data_atual.year
    mes = str(data_atual.month).zfill(2)
    dia = str(data_atual.day).zfill(2)

    path_final = "s3://data-lake-do-weber/REFINED/BD/{ano}/{mes}/{dia}/{tabela}/"

    df_fato_filme.write.mode("overwrite").format("parquet").save(path_final.format(ano=ano, mes=mes, dia=dia, tabela="fato_filme"))
    df_dim_filme.write.mode("overwrite").format("parquet").save(path_final.format( ano=ano, mes=mes, dia=dia, tabela="dim_filme"))
    df_dim_tempo.write.mode("overwrite").format("parquet").save(path_final.format(ano=ano, mes=mes, dia=dia, tabela="dim_tempo"))
    df_dim_artistico.write.mode("overwrite").format("parquet").save(path_final.format(ano=ano, mes=mes, dia=dia, tabela="dim_artistico"))

# Executar as funções principais
df_csv, df_json = ler_arquivos_parquet()
df_junto = filtrar_e_juntar_dataframes(df_csv, df_json)
inserir_dados(df_junto)

job.commit()

```
**Evidência 01 - código dentro job da Aws Glue .**

![weber](/SPRINTS/SPRINT_9/EVIDÊNCIAS/0A_Bucket_data_lake_weber.png)

**Evidência 02 - evidencia que a execução deu certo o código .**

![weber](/SPRINTS/SPRINT_9/EVIDÊNCIAS/0B_Bucket_data_lake_weber_uniao_csv_json.png)

**Evidência 03 - O Crawlers executado .**

![weber](/SPRINTS/SPRINT_9/EVIDÊNCIAS/0C_Bucket_data_lake_weber_Tabelas.png)

**Evidência 04 - A tabela formada.**

![weber](/SPRINTS/SPRINT_9/EVIDÊNCIAS/1A_job_sprint09.png)

**Evidência 05 - execução do SQL dentro Athena mostrando teve 10 resultados.**

![weber](/SPRINTS/SPRINT_9/EVIDÊNCIAS/1B_job_sprint09_sucesso.png)

**Script no Job Glue processar arquivo JON.**

**Evidência 06 - código dentro job da Aws Glue .**

![weber](/SPRINTS/SPRINT_9/EVIDÊNCIAS/2_Crawlers.png)

**Evidência 07 - evidência que a execução deu certo o código.**

![weber](/SPRINTS/SPRINT_9/EVIDÊNCIAS/3_tabelas-formadas.png)

**Evidência 08 -  A tabela formada.**

![weber](/SPRINT_9/EVIDÊNCIAS/4A_arquivos_csv_json.png)

**Evidência 09 - execução do SQL dentro Athena mostrando teve 10 resultados.**

![weber](/SPRINTS/SPRINT_9/EVIDÊNCIAS/Desafio/5A_Dim_artistico.png)
![weber](/SPRINTS/SPRINT_9/EVIDÊNCIAS/Desafio/5B_Dim_artistico.png)

![weber](/SPRINTS/SPRINT_9/EVIDÊNCIAS/Desafio/6A_Dim_tempo.png)
![weber](/SPRINTS/SPRINT_9/EVIDÊNCIAS/Desafio/6B_Dim_tempo.png)

![weber](/SPRINTS/SPRINT_9/EVIDÊNCIAS/Desafio/7A_Dim_filme.png)
![weber](/SPRINTS/SPRINT_9/EVIDÊNCIAS/Desafio/7B_Dim_filme.png)

![weber](/SPRINTS/SPRINT_9/EVIDÊNCIAS/Desafio/8A_Fato_filme.png)
![weber](/SPRINTS/SPRINT_9/EVIDÊNCIAS/Desafio/8B_Fato_filme.png)

# **Questões que serão respondidas na ultima etapa do desafio?**

**Quero saber que para genero crime, o artista principal que tem maiores notas é ator ou atriz?**
**para genero crime, ator ou atriz, avaliar popularidade ao longo dos anos?**
**Na cinco ultimas decadas, qual delas teve maior nota media?**
