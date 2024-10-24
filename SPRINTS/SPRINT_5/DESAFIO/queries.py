import boto3
import pandas as pd
from io import StringIO

boto3.setup_default_session(
    aws_access_key_id='ASIA2MNVMGWNR5V3OVJC',
    aws_secret_access_key='X2GiHkG03Wi9KjeTN0TdHx3ZGyD2zBWLkgwo1u/E',
    aws_session_token='IQoJb3JpZ2luX2VjEFUaCXVzLWVhc3QtMSJHMEUCIQC82PtWHVhQvadqpyt3V3DSS1P0Hr8XUsYI0dpMeS9SQQIgQNHmKRB9PxHWxp2b+WM2iJ4GujVivYxvhWSEJDElIHYqpAMIvv//////////ARAAGgw3MTM4ODE4MjY3MTUiDKxbq0AUdzlh3KU78Cr4Aq/fbl8iUWr/Yxd3DvbVb2o+ihzG/p4qI4etM17+orLFzL0kVshzWgir4ogTvwrofWuFLLvYsW6FI2c6k6vlTav26vnWsTAQVN4N0U5Zy5ONasyoYBikboRx7oJwhB2YJKXU67sP+yNfdT2+azxLVwFv1LWKNtHtss/pjLBIveAa7JCGiVfi4PJvbQUZbCaHCmBnj9ztvQYAq0cL2Xky0RtndWx+Me9QHPBsZzeCHrZ1sKGC0pm3eo5wtFEpQTn7ojMWsbi9AkjjRcl+C9kofPl2TLneXfY7l39ZXG8eq/+1DVVdu9WQ0jyktRXsd5/RyaxMSJ2cDTZvzBHwf9HEAUI7Npe0o1V4H2OQacE8MgrHJ6MPs2OfCnrVBgQ4my9OqMzzFkkVMjUtf400fPbecY7rK2qzKYSUxksJWr6+rBOyQKzJoSPsQjOcQhP9gQAkfhV53q/4dxYxV+SlEp4tmB0Zi2vh+qkCFkVpWvTlIe2ypdHpDJpfdvMw3tXjuAY6pgGhqzs4dtqLnKBsEiTS1xJlsb0R65GV6NdfPEYFtFqqokVyxX2eOk3sJizcGG3Ghg87qOZmTQpJzz5FyRVzYAEaXhS/PpT021taXI7IesiAAt3dGPRkZzTAITNoYxeIfmPH9vVmatQ63L8FGMGWLUzUCYCW5OVEfxsOMfMeRv0nb2iaOeyIT3Hrs6tAoVx0jUI51RCd8nwVoKws5ibe400BUfyMSWkI')

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
