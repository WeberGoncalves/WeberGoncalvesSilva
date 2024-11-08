# DESAFIO sprint 6

**Nessa sprint além de configurar o cliente AWS e as credências de acesso para usar a biblioteca boto3 do python, foi criado imagem para criar container no Docker, e do container excutar script ´´criarBucket.py``, assim foi possível realizar o upload de dois arquivos CSV(movies e series) para esse bucket, organizando-os por dados em diretórios específico.**

## **Dockerfile- instruções para cosntruir imagem no docker**
```yaml annotate
# Imagem base do Python
FROM python:3.9-slim
# Diretório de trabalho dentro do container
WORKDIR /app
VOLUME ["/app/sprint6"]
# Copiar os arquivos de requisitos e o código para o diretório de trabalho
COPY requirements.txt .
COPY criarBucket.py /app/sprint6/criarBucket.py
COPY series.csv /app/sprint6/series.csv
COPY movies.csv /app/sprint6/movies.csv
# Instala as dependências do Python
RUN pip install -r requirements.txt
# Comando para executar o script Python
CMD ["python", "/app/sprint6/criarBucket.py"]
```
**Nesse script no Dockerfile, Configura um ambiente de contêiner para executar um aplicativo Python que interage com o AWS S3.**
**Ele define um diretório de trabalho, copia os arquivos necessários, instala as dependências e especifica o comando de execução.**
**O uso de uma imagem base "slim" e de volumes ajuda a manter a imagem leve e a persistir os dados conforme necessário.**

## **Cria bucket e faz upload para AWS"**
```yaml annotate
import boto3
from botocore.exceptions import ClientError
from datetime import datetime

# Criar um cliente S3
s3_client = boto3.client('s3')

# Nome do bucket
nome_bucket = 'data-lake-do-weber'

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
data = datetime.now().strftime("%Y-%m-%d")

# Definir os caminhos no S3
local_series = f"RAW/Local/CSV/Series/{data}/{nome_arquivo1}"
local_movies = f"RAW/Local/CSV/Movies/{data}/{nome_arquivo2}"

# Fazer upload dos arquivos
fazer_upload(local_arquivo1, nome_bucket, local_series)
fazer_upload(local_arquivo2, nome_bucket, local_movies)
```
**O script cria um bucket S3 (se não existe) e realiza o upload de dois arquivos CSV para esse bucket, organizando-os por dados em um diretório específico. O tratamento de erros garante que o usuário seja informado sobre o sucesso ou falha das operações.**

**Evidência 01 - Comando ``docker build -t imag_sprint6 .`` é usado para construir uma imagem Docker a partir de um Dockerfile localizado no diretório atual.**
![weber](/SPRINTS/SPRINT_6/EVIDÊNCIAS/Desafio_A_01a_criando%20Image-docker.png)

**Evidência 02 - confirmação sucesso da excução do comando anterior.**
![weber](/SPRINTS/SPRINT_6/EVIDÊNCIAS/Desafio_A_01b_criando%20Image-docker.png)

**Evidência 03 -Usando comando ``docker run -e AWS_ACCESS_KEY_ID="##" -e AWS_SECRET_ACCESS_KEY="##" -e AWS_SESSION_TOKEN="##" -e AWS_DEFAULT_REGION=us-east-1 imag_sprint6``.**
**Este comando ``docker run`` está iniciando um contêiner baseado em imagem imag_sprint6, passando pelas credenciais da AWS como variáveis ​​de ambiente. Isso permite que o aplicativo dentro do contêiner acesse os serviços da AWS usando as credenciais fornecidas, como criar buckets ou fazer upload de arquivos para o S3.**
![weber](/SPRINTS/SPRINT_6/EVIDÊNCIAS/Desafio_A_02a_execultado-container-docker.png)

**Evidência 04 - Continuação da excução do comando anterior.**
![weber](/SPRINTS/SPRINT_6/EVIDÊNCIAS/Desafio_A_02b_execultado-container-docker.png)

**Evidência 05 - Criado bucket "data-lake-do-weber" na AWS.**
![weber](/SPRINTS/SPRINT_6/EVIDÊNCIAS/Desafio_A_03_criarBucket.png)

**Evidência 06 - Criado os Diretórios onde ficaria os arquivos de movies e series.**
![weber](/SPRINTS/SPRINT_6/EVIDÊNCIAS/Desafio_A_04_upload-movies-series.png)

**Evidência 07 - Upload bem sucedido do arquivo movies.csv.**
![weber](/SPRINTS/SPRINT_6/EVIDÊNCIAS/Desafio_A_05_estruturas%20da%20pastas-fimes.png)

**Evidência 08 - Upload bem sucedido do arquivo series.csv.**
![weber](/SPRINTS/SPRINT_6/EVIDÊNCIAS/Desafio_A_06_estruturas%20da%20pastas-series.png)