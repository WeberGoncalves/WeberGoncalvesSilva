# DESAFIO sprint 5

**Nessa sprint foi necessario configurar o cliente AWS e as credências de acesso para usar a biblioteca boto3 do python .**
**Depois foi feito algoritmo "criarBucket.py" de acesso as credências, criava bucket e enviava o arquivo de dados.csv para o bucket.**
**No algoritmo "queries.py" faz leitura do arquivo dados.csv, realiza as consultas e envia os resultados para bucket.**

## **Configuração acesso como Clienete da AWS pelo Terminal**
**Evidência 01- solicitação de cliente.**

![weber](/SPRINTS/SPRINT_5/EVIDÊNCIAS/conf-AWS-Cli.png)

**Evidência 02- mostra acesso aprovado.**

![weber](/SPRINTS/SPRINT_5/EVIDÊNCIAS/conf-AWS-Cli-2.png)

## **Algoritmo "criarBucket.py"**
```yaml annotate
# criar um cliente
s3 = boto3.resource('s3')
# nome do bucket
nome_bucket = 'sprint5weber'
# criando bucket
s3.create_bucket(Bucket=nome_bucket)
arquivo = 'dados.csv'

# Nome do arquivo no bucket
nome_arquivo = 'dados.csv'

# fazer upaload para o bucket
s3.Bucket(nome_bucket).upload_file(arquivo, nome_arquivo)

print(f'Arquivo{nome_arquivo}\
    enviando para backet {nome_bucket} com sucesso!')

```
**Evidência 01- rodando o algoritmo.**

![weber](/SPRINTS/SPRINT_5/EVIDÊNCIAS/desafio_01A.png)

**Evidência 02- resultou na criação do bucket chamado sprint5weber.**

![weber](/SPRINTS/SPRINT_5/EVIDÊNCIAS/desafio_01B.png)


**Evidência 03- enviado arquivo dados.csv para bucket sprint5weber.**

![weber](/SPRINTS/SPRINT_5/EVIDÊNCIAS/desafio_01C.png)


**Evidência 04-.**

![weber](/SPRINTS/SPRINT_5/EVIDÊNCIAS/Config_credenciais_AWS_4.png)

## **Configuração acesso sessão com credenciais da AWS pelo Terminal**
**Evidência 01-.**

![weber](/SPRINTS/SPRINT_5/EVIDÊNCIAS/Config_credenciais_AWS_1.png)


## **Algoritmo "queries.py"**

```yaml annotate
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

```
**Evidência 01- rodando o algoritmo.**

![weber](/SPRINTS/SPRINT_5/EVIDÊNCIAS/desafio_01D.png)

**Evidência 02- resultado pelo terminal.**

![weber](/SPRINTS/SPRINT_5/EVIDÊNCIAS/desafio_02.png)

**Evidência 03- resultado pelo terminal.**

![weber](/SPRINTS/SPRINT_5/EVIDÊNCIAS/desafio_03.png)


**Evidência 04-Pelo terminal mostrando o envio do arquivo resultado.csv para bucket.**

![weber](/SPRINTS/SPRINT_5/EVIDÊNCIAS/desafio_04.png)

