## **Seção 04- Apache Spark- contador de palavras.**

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

![weber](/SPRINTS/SPRINT_7/EVIDÊNCIAS/ContadorPalavras01.png)


**Evidência 02 - O termino da Execução com resultado das quantidades.**

![weber](/SPRINTS/SPRINT_7/EVIDÊNCIAS/ContadorPalavras02.png)


**---------------------------------------------------------------**
## **Seção 05- Lab AWS Glue.**
 
**Evidência 01 - realizado upload do arquivo nomes.**

![weber](/SPRINTS/SPRINT_7/EVIDÊNCIAS/Lab-B_1_Glue-upload-nomes.png)


**Evidência 02 - Configurando sua conta para utilizar o AWS Glue.**

![weber](/SPRINTS/SPRINT_7/EVIDÊNCIAS/Lab_1_Glue.png)

**Evidência 03 - Configurando para utilizar o AWS Glue.**

![weber](/SPRINTS/SPRINT_7/EVIDÊNCIAS/Lab_2_Glue.png)


**Evidência 04 - Configurando utilizar o AWS Glue.**

![weber](/SPRINTS/SPRINT_7/EVIDÊNCIAS/Lab_3_Glue.png)

**Evidência 05 - Configurando da função no AWS Glue.**

![weber](/SPRINTS/SPRINT_7/EVIDÊNCIAS/Lab_4_Criando-novo-job-AWS-Glue.png)


**Evidência 06 - criando no job.**

![weber](/SPRINTS/SPRINT_7/EVIDÊNCIAS/Lab_4B_Criando-novo-job-AWS-Glue.png)

**Evidência 07 - job executado com sucesso.**

![weber](/SPRINTS/SPRINT_7/EVIDÊNCIAS/Lab_4C_novo-job-Corrigido-AWS-Glue.png)


**Evidência 08 - arquivos gerados.**

![weber](/SPRINTS/SPRINT_7/EVIDÊNCIAS/Lab_4D_novo-job-Corrigido-AWS-Glue.png)


### Algoritmo completo

**.**
```yaml annotate
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql import functions as F

## @params: [JOB_NAME, INPUT_PATH, OUTPUT_PATH]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'INPUT_PATH', 'OUTPUT_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminho do arquivo no S3
source_file = args['INPUT_PATH']

# Esquema manual (ajuste conforme necessário)
schema = StructType([import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql import functions as F

## @params: [JOB_NAME, INPUT_PATH, OUTPUT_PATH]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'INPUT_PATH', 'OUTPUT_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminho do arquivo no S3
source_file = args['INPUT_PATH']

# Esquema manual (ajuste conforme necessário)
schema = StructType(
[
    StructField("nome", StringType(), True),
    StructField("sexo", StringType(), True),
    StructField("ano", StringType(), True),
    StructField("total", IntegerType(), True)
])

# 1. Ler o arquivo CSV do S3 com esquema manual
try:
    df = spark.read.csv(
        source_file,
        schema=schema,
        header=True,  # Assumir que há cabeçalhos no arquivo
        sep="|"  # Ajuste o delimitador caso necessário
    )
    print("Leitura do arquivo realizada com sucesso!")
    df.printSchema()
    df.show(10)
except Exception as e:
    print(f"Erro ao ler o arquivo: {e}")
    raise

# Garantir que todas as colunas esperadas estão presentes
colunas_necessarias = {"nome", "sexo", "ano"}
if not colunas_necessarias.issubset(df.columns):
    raise ValueError(f"As colunas esperadas {colunas_necessarias} estão ausentes no esquema!")

# 2. Alterar os valores da coluna 'nome' para maiúsculas
df = df.withColumn("nome", F.upper(F.col("nome")))

# 3. Contagem de linhas no DataFrame
contagem_linhas = df.count()
print(f"Contagem de linhas: {contagem_linhas}")

# 4. Total de registros por ano
total_registros = df.groupBy("ano").count().orderBy("ano", ascending=True)
total_registros.show(10)

# 5. Gravar os dados no S3 com partições
output_path = f"{args['OUTPUT_PATH']}/frequencia_registro_nomes_eua/"
df.write.partitionBy("sexo", "ano").json(output_path)

job.commit()

    StructField("nome", StringType(), True),
    StructField("sexo", StringType(), True),
    StructField("ano", StringType(), True),
    StructField("total", IntegerType(), True)
])

# 1. Ler o arquivo CSV do S3 com esquema manual
try:
    df = spark.read.csv(
        source_file,
        schema=schema,
        header=True,  # Assumir que há cabeçalhos no arquivo
        sep="|"  # Ajuste o delimitador caso necessário
    )
    print("Leitura do arquivo realizada com sucesso!")
    df.printSchema()
    df.show(10)
except Exception as e:
    print(f"Erro ao ler o arquivo: {e}")
    raise

# Garantir que todas as colunas esperadas estão presentes
colunas_necessarias = {"nome", "sexo", "ano"}
if not colunas_necessarias.issubset(df.columns):
    raise ValueError(f"As colunas esperadas {colunas_necessarias} estão ausentes no esquema!")

# 2. Alterar os valores da coluna 'nome' para maiúsculas
df = df.withColumn("nome", F.upper(F.col("nome")))

# 3. Contagem de linhas no DataFrame
contagem_linhas = df.count()
print(f"Contagem de linhas: {contagem_linhas}")

# 4. Total de registros por ano
total_registros = df.groupBy("ano").count().orderBy("ano", ascending=True)
total_registros.show(10)

# 5. Gravar os dados no S3 com partições
output_path = f"{args['OUTPUT_PATH']}/frequencia_registro_nomes_eua/"
df.write.partitionBy("sexo", "ano").json(output_path)

job.commit()

```
**Evidência 09 - Criado o crawler.**

![weber](/SPRINTS/SPRINT_7/EVIDÊNCIAS/Lab_5A_Create-Crawler.png)


**Evidência 09 - Criado o crawler.**

![weber](/SPRINT_7/EVIDÊNCIAS/Lab_5B_Create-Crawler.png)
