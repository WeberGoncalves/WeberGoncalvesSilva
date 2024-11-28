import boto3
from botocore.exceptions import ClientError
from datetime import datetime

# Criar um cliente S3
s3_client = boto3.client('s3')

# Nome do bucket
nome_bucket = 'test-data-lake-do-weber'


def criar_bucket(nome_bucket):
    """Cria um bucket S3 se não existir."""
    try:
        # Verifica se o bucket já existe
        s3_client.head_bucket(Bucket=nome_bucket)
        print(f'O bucket {nome_bucket} já existe.')
    except ClientError as e:
        # Se o erro for 404, o bucket não existe e pode ser criado
        if e.response['Error']['Code'] == '404':
            s3_client.create_bucket(Bucket=nome_bucket)
            print(f'Bucket {nome_bucket} criado com sucesso.')
        else:
            print(f'Erro ao verificar o bucket: {e}')


def fazer_upload(local_arquivo, nome_bucket, caminho_s3):
    """Faz o upload de um arquivo para o bucket S3."""
    try:
        s3_client.upload_file(local_arquivo, nome_bucket, caminho_s3)
        print(f'Arquivo {local_arquivo} enviado para\
               {caminho_s3} com sucesso!')
    except FileNotFoundError:
        print(f'O arquivo {local_arquivo} não foi encontrado.')
    except ClientError as e:
        print(f'Erro ao fazer upload do arquivo: {e}')


# Criar o bucket
criar_bucket(nome_bucket)

# Nome dos arquivos locais
local_arquivo1 = r"/app/sprint6/series.csv"
local_arquivo2 = r"/app/sprint6/movies.csv"
nome_arquivo1 = "series.csv"
nome_arquivo2 = "movies.csv"

# Usando hífens para o formato de data
data = datetime.now().strftime("%Y/%m/%d")

# Definir os caminhos no S3
local_series = f"RAW/Local/CSV/Series/{data}/{nome_arquivo1}"
local_movies = f"RAW/Local/CSV/Movies/{data}/{nome_arquivo2}"

# Fazer upload dos arquivos
fazer_upload(local_arquivo1, nome_bucket, local_series)
fazer_upload(local_arquivo2, nome_bucket, local_movies)
