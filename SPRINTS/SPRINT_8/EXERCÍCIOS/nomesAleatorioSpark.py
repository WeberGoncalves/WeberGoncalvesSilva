# Importar bibliotecas necessárias
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, lit, rand, when
from pyspark.sql.types import StringType, IntegerType
import random

# Definir a Spark Session
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("NomesAleatorios") \
    .getOrCreate()

# Ler o arquivo CSV e criar o DataFrame
df_nomes = spark.read.csv('/content/Dados/nomes_aleatorios.txt', header=False)
df_nomes.show(5)

# Verificar o Schema
df_nomes.printSchema()

# Renomear a coluna para "Nomes" e mostrar o DataFrame
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")
df_nomes.printSchema()
df_nomes.show(10)

# Etapa 3.3: Adicionar coluna Escolaridade
escolaridades = ['Fundamental', 'Medio', 'Superior']

def gerar_escolaridade():
    return random.choice(escolaridades)

escolaridade_udf = udf(gerar_escolaridade, StringType())
df_nomes = df_nomes.withColumn("Escolaridade", escolaridade_udf())
df_nomes.show(10)

# Etapa 3.4: Adicionar coluna Pais
paises = ['Brasil', 'Argentina', 'Chile', 'Uruguai', 'Paraguai', 'Bolívia', 'Peru', 'Equador', 'Colômbia', 'Venezuela', 'Guiana', 'Suriname', 'Guiana Francesa']

def gerar_pais():
    return random.choice(paises)

pais_udf = udf(gerar_pais, StringType())
df_nomes = df_nomes.withColumn("Pais", pais_udf())
df_nomes.show(10)

# Etapa 3.5: Adicionar coluna AnoNascimento
def gerar_ano():
    return random.randint(1945, 2010)

ano_udf = udf(gerar_ano, IntegerType())
df_nomes = df_nomes.withColumn("AnoNascimento", ano_udf())
df_nomes.show(10)

# Adicionar coluna "Geracao" antes de registrar a tabela temporária
df_nomes = df_nomes.withColumn(
    "Geracao",
    when(df_nomes.AnoNascimento.between(1944, 1964), "Baby Boomers")
    .when(df_nomes.AnoNascimento.between(1965, 1979), "Geração X")
    .when(df_nomes.AnoNascimento.between(1980, 1994), "Millennials")
    .when(df_nomes.AnoNascimento.between(1995, 2015), "Geração Z")
)
df_nomes.show(10)

# Etapa 3.6: Selecionar pessoas que nasceram neste século
df_select = df_nomes.filter(df_nomes.AnoNascimento >= 2000)
df_select.show(10)

# Etapa 3.7: Usar Spark SQL para selecionar pessoas nascidas neste século
df_nomes.createOrReplaceTempView("pessoas")
df_select_sql = spark.sql("SELECT * FROM pessoas WHERE AnoNascimento >= 2000")
df_select_sql.show(10)

# Etapa 3.8: Contar o número de Millennials
millennials_count = df_nomes.filter((df_nomes.AnoNascimento >= 1980) & (df_nomes.AnoNascimento <= 1994)).count()
print("Número de Millennials:", millennials_count)

# Etapa 3.9: Contar o número de Millennials usando Spark SQL
millennials_count_sql = spark.sql("SELECT COUNT(*) FROM pessoas WHERE AnoNascimento BETWEEN 1980 AND 1994").collect()[0][0]
print("Número de Millennials (SQL):", millennials_count_sql)

# Etapa 3.10: Quantidade de pessoas por geração e por país
df_generations = spark.sql("""
    SELECT Pais, Geracao, COUNT(*) as Quantidade
    FROM pessoas
    GROUP BY Pais, Geracao
    ORDER BY Pais, Geracao
""")
df_generations.show()
