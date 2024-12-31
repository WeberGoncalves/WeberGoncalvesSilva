import boto3
import pandas as pd
from io import StringIO

boto3.setup_default_session(
     aws_access_key_id='ASIA2MNVMGWN3NKZURHK',
    aws_secret_access_key='7cnvMupiUMlpwyfamCnnluGn7V97QnY2bICwWImM',
    aws_session_token='IQoJb3JpZ2luX2VjEKP//////////wEaCXVzLWVhc3QtMSJHMEUCIQDLNWg1HGUybGRs+Uzl8AcNQ9ZfuB6vqUMKZnhy6RheUQIgLLLwSx8OPCrMBDOGnMNzFhNzA8UcuomgBL+QWYEDWMsqmwMIGxAAGgw3MTM4ODE4MjY3MTUiDKYK0dgkv9KTbst5sCr4AssQDUE+VXfXzdm7EWceduokielSjWInakUBIBhcQwlNZrUkg6fShBIV7MUDHpuy1crDZQZaVjTJVpaMZ6mwpZz12JWIuOOZWm4VpA2IYXVScCHfoqcsZu8gA6DyxG7cGXGHDVWamIouNMywRQca3BEpjllyAao8YbMXKnn50l+y67ol9BIYuThI6FUdCxSI8HMRgqmy5yO2GRRJUDMw8F8jCrp/IetWRVELVMyFt02/NkATr8h9blawuDSZQaTmk9i7tZnBnztoyzzwQJ733QWIA5C40TAVoh1X41rbPLr39f9wbbC6G4XQM5MlEE1+9a2KVadqC5a72PxF5Q5u1icXerW01GFjiK1uJbTTE7mLXty2rhw9VGV9GpPtLkKKtJX4XP2SEgIhIhQj7vDCwml1dTbl1MPoFFZkH+7zGJ7bzvJm1n6OudGpA/hKUpqmmEaOiM4y4l7VYHhyVQgvJ+HQpLk4w7mJR0O1xYpWjlQXi7ZYVPLgVnYw3OH0uAY6pgFP0ag33crsih+izF3Y2GPifgTHXQWgCPtmDnUaYSSAGoiScXLRDGeqtMMCunoNgX6rTfoZM8cpILfOLVQmsf1bkNbVSMVZDrMrIcBbD70xGga5cbL6ZmlxAMKtRoxmT1XN00OrDoIZxL3Dp286bpiw2hIASzsSWXMkoQyV4mpLuZKD5YqIo7JhY/9RnhxVHKhM7QSz0zjZ5ytk0gfIGCCv46TRHWTm')

# Inicializar cliente S3
cliente_s3 = boto3.client('s3')

# Definir parâmetros
nome_bucket = 'sprint5weber'
nome_objeto = 'dados.csv'  # Nome do arquivo no S3
nome_objeto_saida = 'resultado.csv'  # Nome do arquivo de saída

# Ler o arquivo CSV do S3
resposta = cliente_s3.get_object(Bucket=nome_bucket, Key=nome_objeto)
dados = resposta['Body'].read().decode('utf-8')
df = pd.read_csv(StringIO(dados), sep=';')
print("DataFrame carregado com sucesso!")

# 4.1 Filtragem com dois operadores lógicos
df_filtrado = df[(df['Quantidade Recursos'] > 10) &
                 (df['Quantidade Downloads'] < 50)]
print("Filtragem:\n", df_filtrado)

# 4.2 Duas funções de agregação
agregacao = df.groupby('Organização').agg(
    {'Quantidade Recursos': 'sum', 'Quantidade Downloads': 'mean'})
print("Agregação:\n", agregacao)

# 4.3 Função condicional
df['Status'] = df['Quantidade Recursos'].apply(
    lambda x: 'Alta' if x > 20 else 'Baixa')
print("Coluna condicional:\n", df[['Quantidade Recursos', 'Status']])

# 4.4 Função de conversão
df['Quantidade Recursos'] = df['Quantidade Recursos'].astype(int)
print("Conversão de tipo:\n", df.dtypes)

# 4.5 Função de data (adicionando uma coluna de data fictícia)
df['Data Criacao'] = pd.to_datetime('2023-01-01')
print("Coluna de data adicionada:\n", df['Data Criacao'])

# 4.6 Função de string
df['Nome'] = df['Nome'].str.upper()
print("Coluna de string convertida:\n", df[['Nome']])

# Salvar o DataFrame como CSV no S3
buffer_saida = StringIO()
df.to_csv(buffer_saida, index=False, sep=';')
buffer_saida.seek(0)
cliente_s3.put_object(Bucket=nome_bucket,
                      Key=nome_objeto_saida, Body=buffer_saida.getvalue())
print(f'Arquivo {nome_objeto_saida} salvo no bucket S3 com sucesso!')
