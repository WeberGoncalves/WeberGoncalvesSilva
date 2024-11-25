# Instalei no Colab !pip install pyspark

# Importe e configure o Spark
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, regexp_replace

# Cria uma sessão Spark
spark = SparkSession.builder.appName("ContagemDePalavras").getOrCreate()

# Carregar o arquivo de texto
linhas = spark.read.text("/content/README.md")

# Remover caracteres especiais específicos: #, [, ##, *, **
linhas_limpa = linhas.select(regexp_replace(linhas.value, r"[\#\[\]\*\*\*]+", "").alias("limpo"))

# Dividir as linhas em palavras e contar
palavras = linhas_limpa.select(explode(split(linhas_limpa.limpo, "\s+")).alias("palavra"))
contagem_palavras = palavras.groupBy("palavra").count().orderBy("count", ascending=False)

# Exibir o resultado
contagem_palavras.show(truncate=False)
