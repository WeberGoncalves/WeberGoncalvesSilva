# **Apache Spark- contador de palavras.**

**Detalhes importante sobre o script.**

´´from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, regexp_replace
´´
**Importação das classes e funções necessárias do PySpark. SparkSession é a entrada para utilizar a API do Spark SQL. explode, split e regexp_replace são funções que você utilizará para manipular os dados.**

´´spark = SparkSession.builder.appName("ContagemDePalavras").getOrCreate()
´´
**Isso cria uma sessão do Spark com o nome "ContagemDePalavras". SparkSession é a interface principal para a programação Spark e permite a conexão ao cluster Spark.**

### Algoritmo completo

**Esse script utiliza o PySpark para realizar um processamento de texto, contando a frequência de cada palavra em um arquivo de texto após remover certos caracteres especiais. É um exemplo clássico de como o Spark pode ser utilizado para tarefas de ETL e processamento de dados em larga escala.**
```yaml annotate
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

```
**Evidência 01 - Algoritmo executado.**

![weber](/SPRINT_7/EVIDÊNCIAS/ContadorPalavras01.png)


**Evidência 02 - O termino da Execução com resultado das quantidades.**

![weber](/SPRINT_7/EVIDÊNCIAS/ContadorPalavras02.png)
