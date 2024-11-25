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

![weber](/SPRINT_7/EVIDÊNCIAS/ContadorPalavras01.png)


**Evidência 02 - O termino da Execução com resultado das quantidades.**

![weber](/SPRINT_7/EVIDÊNCIAS/ContadorPalavras02.png)

**---------------------------------------------------------------**
## **Seção 05- Lab AWS Glue.**
 
**Evidência 01 - texto.**

![weber](/SPRINT_7/EVIDÊNCIAS/Lab-B_1_Glue-upload-nomes.png)


**Evidência 02 - texto.**

![weber](/SPRINT_7/EVIDÊNCIAS/Lab_1_Glue.png)

**Evidência 03 - texto.**

![weber](/SPRINT_7/EVIDÊNCIAS/Lab_2_Glue.png)


**Evidência 04 - texto.**

![weber](/SPRINT_7/EVIDÊNCIAS/Lab_3_Glue.png)

**Evidência 05 - texto.**

![weber](/SPRINT_7/EVIDÊNCIAS/Lab_4_Criando-novo-job-AWS-Glue.png)


**Evidência 06 - texto.**

![weber](/SPRINT_7/EVIDÊNCIAS/Lab_4B_Criando-novo-job-AWS-Glue.png)

**Evidência 07 - texto.**

![weber](/SPRINT_7/EVIDÊNCIAS/Lab_4C_novo-job-Corrigido-AWS-Glue.png)


**Evidência 08 - texto.**

![weber](/SPRINT_7/EVIDÊNCIAS/Lab_4D_novo-job-Corrigido-AWS-Glue.png)


### Algoritmo completo

**.**
```yaml annotate
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F

## @params: [JOB_NAME, INPUT_PATH, OUTPUT_PATH]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'INPUT_PATH', 'OUTPUT_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# 1. Ler o arquivo nomes.csv no S3
source_file = args['INPUT_PATH']
df = glueContext.create_dynamic_frame.from_options(
    "s3",
    {
        "paths": [source_file]
    },
    "csv",
    {"withHeader": True, "separator": "|"}
)

# 2. Imprimir o schema do DataFrame
df.printSchema()

# Converter DynamicFrame para DataFrame para manipulações adicionais
df = df.toDF()

# 3. Alterar a caixa dos valores da coluna 'nome' para MAIÚSCULO
df = df.withColumn("nome", F.upper(df["nome"]))

# 4. Imprimir a contagem de linhas presentes no DataFrame
contagem_linhas = df.count()
print(f"Contagem de linhas: {contagem_linhas}")

# 5. Contar nomes, agrupando pelos dados do DataFrame pelas colunas 'ano' e 'sexo'
contagem_nomes = df.groupBy("ano", "sexo").count().orderBy("ano", ascending=False)
contagem_nomes.show()

# 6. Nome feminino com mais registros e em que ano ocorreu
nome_feminino = df.filter(df.sexo == "FEMININO") \
    .groupBy("nome", "ano") \
    .count() \
    .orderBy(F.desc("count")) \
    .first()
print(f"Nome feminino com mais registros: {nome_feminino['nome']} no ano {nome_feminino['ano']}")

# 7. Nome masculino com mais registros e em que ano ocorreu
nome_masculino = df.filter(df.sexo == "MASCULINO") \
    .groupBy("nome", "ano") \
    .count() \
    .orderBy(F.desc("count")) \
    .first()
print(f"Nome masculino com mais registros: {nome_masculino['nome']} no ano {nome_masculino['ano']}")

# 8. Total de registros (masculinos e femininos) para cada ano
total_registros = df.groupBy("ano").count().orderBy("ano", ascending=True)
total_registros.show(10)  # Mostrar as primeiras 10 linhas

# 9. Gravar o conteúdo do DataFrame com os valores de nome em maiúsculo no S3
output_path = f"{args['OUTPUT_PATH']}/frequencia_registro_nomes_eua/"
df.write.partitionBy("sexo", "ano").json(output_path)

job.commit()

```
