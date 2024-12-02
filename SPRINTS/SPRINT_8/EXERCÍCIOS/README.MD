## Seções 02 e 03 Exercicios Spark Batch

**Na seção 02 dos exercicios foi usado python para 3 primeiros e no ultimo foi necessario python com spark.**

**Script do 250 números aleatórios**

```yaml annotate
import random

lista_aleatoria = [random.randint(0, 1000) for _ in range(250)]

lista_aleatoria.reverse()

print(lista_aleatoria)

```
**Evidência 01 - lista com 250 números inteiros obtidos de forma aleatória.**

![weber](/SPRINTS/SPRINT_8/EVIDÊNCIAS/seção_02/250_inteiros.png)


**Neste script foi utilizado List comprehension, que é uma técnica concisa e eficiente do Python para criar listas. Ela permite construir novas listas aplicando uma expressão a cada item de uma sequência (como listas, tuplas, ou strings) e, opcionalmente, filtrando itens usando uma condição.**
***Estrutura básica da list comprehension ***
**´´´[expressão for item in sequência if condição]´´´**

```yaml annotate
animais = 
        [
            "Cachorro", "Gato", "Elefante", "Girafa", "Leão", "Tigre", "Cavalo", "Vaca", "Baleia", "Golfinho", "Coelho", "Panda", "Rinoceronte", "Canguru", "Pinguim", "Urso", "Lobo", "Macaco", "Zebra", "Hipopótamo"
        ]

animais_ordenados = sorted(animais)
[print(animal) for animal in animais_ordenados]

with open('animais.csv', 'w') as file:
    for animal in animais_ordenados:
        file.write(f"{animal}\n")

```
**Evidência 02 - Lista de 20 animais em ordem crescente.**

![weber](/SPRINTS/SPRINT_8/EVIDÊNCIAS/seção_02/20Animais.png)

**Neste script gera 1.000.000 de nomes aleatórios a partir de uma lista de 300 nomes únicos e salva esses nomes em um arquivo de texto. Ele utiliza bibliotecas para geração de nomes (names) e funções para manipulação de listas e arquivos. A semente do gerador de números aleatórios é definida para garantir que os resultados sejam sempre os mesmos em diferentes execuções.**

```yaml annotate
import random
import names

def definir_parametros():    
    qtd_nomes_aleatorios = 1000000  
    qtd_nomes_unicos = 300       
    random.seed(42)  
    return qtd_nomes_aleatorios, qtd_nomes_unicos

def gerar_nomes_unicos(qtd_nomes_unicos):    
    aux = []
    for _ in range(qtd_nomes_unicos):
        aux.append(names.get_full_name())
    return aux

def gerar_nomes_aleatorios(aux, qtd_nomes_aleatorios):    
    dados = [random.choice(aux) for _ in range(qtd_nomes_aleatorios)]
    return dados

def salvar_nomes_em_arquivo(dados, nome_arquivo='nomes_aleatorios.txt'):    
    with open(nome_arquivo, 'w') as file:
        for nome in dados:
            file.write(nome + '\n')
    print(f"Arquivo '{nome_arquivo}' criado com sucesso!")

def main():
    qtd_nomes_aleatorios, qtd_nomes_unicos = definir_parametros()
    aux = gerar_nomes_unicos(qtd_nomes_unicos)
    print(f"Gerando {qtd_nomes_aleatorios} nomes aleatórios")
    dados = gerar_nomes_aleatorios(aux, qtd_nomes_aleatorios)
    salvar_nomes_em_arquivo(dados)

if __name__ == "__main__":
    main()
```
**OBS: na pasta exercicios tem o arquivo nomes_aleatorios.txt, para conferência.**
**Evidência 03 - Nomes aleatórios a partir de uma lista de 300 nomes únicos.**

![weber](/SPRINTS/SPRINT_8/EVIDÊNCIAS/seção_02/dataSetNomes.png)

### Exercício realiazado com pySpark

**Esse código demonstra como usar o PySpark para manipular e analisar dados, aplicando transformações, filtragens e agregações de maneira eficiente e escalável.**

```yaml annotate

from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, lit, rand, when
from pyspark.sql.types import StringType, IntegerType
import random

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("NomesAleatorios") \
    .getOrCreate()

df_nomes = spark.read.csv('/content/Dados/nomes_aleatorios.txt', header=False)
df_nomes.show(5)

df_nomes.printSchema()

df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")
df_nomes.printSchema()
df_nomes.show(10)

escolaridades = ['Fundamental', 'Medio', 'Superior']

def gerar_escolaridade():
    return random.choice(escolaridades)

escolaridade_udf = udf(gerar_escolaridade, StringType())
df_nomes = df_nomes.withColumn("Escolaridade", escolaridade_udf())
df_nomes.show(10)

paises = ['Brasil', 'Argentina', 'Chile', 'Uruguai', 'Paraguai', 'Bolívia', 'Peru', 'Equador', 'Colômbia', 'Venezuela', 'Guiana', 'Suriname', 'Guiana Francesa']

def gerar_pais():
    return random.choice(paises)

pais_udf = udf(gerar_pais, StringType())
df_nomes = df_nomes.withColumn("Pais", pais_udf())
df_nomes.show(10)

def gerar_ano():
    return random.randint(1945, 2010)

ano_udf = udf(gerar_ano, IntegerType())
df_nomes = df_nomes.withColumn("AnoNascimento", ano_udf())
df_nomes.show(10)

df_nomes = df_nomes.withColumn(
    "Geracao",
    when(df_nomes.AnoNascimento.between(1944, 1964), "Baby Boomers")
    .when(df_nomes.AnoNascimento.between(1965, 1979), "Geração X")
    .when(df_nomes.AnoNascimento.between(1980, 1994), "Millennials")
    .when(df_nomes.AnoNascimento.between(1995, 2015), "Geração Z")
)
df_nomes.show(10)

df_select = df_nomes.filter(df_nomes.AnoNascimento >= 2000)
df_select.show(10)

df_nomes.createOrReplaceTempView("pessoas")
df_select_sql = spark.sql("SELECT * FROM pessoas WHERE AnoNascimento >= 2000")
df_select_sql.show(10)

millennials_count = df_nomes.filter((df_nomes.AnoNascimento >= 1980) & (df_nomes.AnoNascimento <= 1994)).count()
print("Número de Millennials:", millennials_count)

millennials_count_sql = spark.sql("SELECT COUNT(*) FROM pessoas WHERE AnoNascimento BETWEEN 1980 AND 1994").collect()[0][0]
print("Número de Millennials (SQL):", millennials_count_sql)

df_generations = spark.sql("""
    SELECT Pais, Geracao, COUNT(*) as Quantidade
    FROM pessoas
    GROUP BY Pais, Geracao
    ORDER BY Pais, Geracao
""")
df_generations.show()

```
**Evidência 04 - Script executaldo pyspark.**

![weber](/SPRINTS/SPRINT_8/EVIDÊNCIAS/seção_02/spark_01.png)

**Evidência 05.**
**listem da 5 primeiras linhas usando método show.**
**Foi renomeado a coluna nomes para Nomes, impresso as 10 linhas do dataframe.**
**Foi adicionado uma nova coluna chamada AnoNascimento e atribuido para cada linha um valor de ano entre 1945 e 2010, de forma aleatória.**

![weber](/SPRINTS/SPRINT_8/EVIDÊNCIAS/seção_02/spark_02.png)

**Evidência 06 -Quantidade de pessoas de cada país para cada uma das gerações  • Baby Boomers ,• Geração X e • Millennials (Geração Y).**

![weber](/SPRINTS/SPRINT_8/EVIDÊNCIAS/seção_02/spark_03.png)

**Evidência 07 - Quantidade de pessoas de cada país para cada uma das gerações  • Baby Boomers ,• Geração X e • Millennials (Geração Y).**

![weber](/SPRINTS/SPRINT_8/EVIDÊNCIAS/seção_02/spark_04.png)


