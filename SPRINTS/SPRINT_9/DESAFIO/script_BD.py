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

# Função para ler os arquivos Parquet no S3
def ler_arquivos_parquet():
    caminho_parquet_csv = "s3://data-lake-do-weber/TRUSTED/CSV/2024/12/17/"
    caminho_parquet_json = "s3://data-lake-do-weber/TRUSTED/JSON/2024/12/17/"
    df_csv = spark.read.parquet(caminho_parquet_csv)
    df_json = spark.read.parquet(caminho_parquet_json)
    return df_csv, df_json

# Função para limpar os títulos dos filmes
def limpar_titulos(df):
    titulos = ['tituloPrincipal', 'titulo']
    for titulo in titulos:
        if titulo in df.columns:
            df = df.withColumn(
                titulo,
                regexp_replace(titulo, r'[\",!&\.\.:\?\[\]]', '')  # Remove os caracteres específicos
            )
    return df

# Função para filtrar e juntar os DataFrames
def filtrar_e_juntar_dataframes(df_csv, df_json):
    df_csv = limpar_titulos(df_csv)
    df_json = limpar_titulos(df_json)

    # Renomeando as colunas para garantir consistência
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

# Função para inserir dados nas tabelas
def inserir_dados(df_filtrado):
    # Dimensão de filmes
    df_dim_filme = df_filtrado.select("titulo").distinct() \
        .withColumn("id_filme", row_number().over(Window.orderBy("titulo"))) \
        .select("id_filme", "titulo")

    # Adiciona o id_filme ao DataFrame principal
    df_filtrado = df_filtrado.join(df_dim_filme, on="titulo", how="inner")

    # Dimensão de tempo
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

    # Dimensão artística
    df_dim_artistico = df_filtrado.select("nome_artistico", "genero_artista").distinct() \
        .withColumn("id_artistico", row_number().over(Window.orderBy("nome_artistico"))) \
        .select("id_artistico", "nome_artistico", "genero_artista")

    # Fato
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

    # Definindo os caminhos para salvar os dados com a interpolação correta
    path_final = "s3://data-lake-do-weber/REFINED/BD/{ano}/{mes}/{dia}/{tabela}/"

    # Salvando os dados nos respectivos caminhos
    df_fato_filme.write.mode("overwrite").format("parquet").save(path_final.format(ano=ano, mes=mes, dia=dia, tabela="fato_filme"))
    df_dim_filme.write.mode("overwrite").format("parquet").save(path_final.format( ano=ano, mes=mes, dia=dia, tabela="dim_filme"))
    df_dim_tempo.write.mode("overwrite").format("parquet").save(path_final.format(ano=ano, mes=mes, dia=dia, tabela="dim_tempo"))
    df_dim_artistico.write.mode("overwrite").format("parquet").save(path_final.format(ano=ano, mes=mes, dia=dia, tabela="dim_artistico"))

# Executar as funções principais
df_csv, df_json = ler_arquivos_parquet()
df_junto = filtrar_e_juntar_dataframes(df_csv, df_json)
inserir_dados(df_junto)

# Finaliza o trabalho
job.commit()
