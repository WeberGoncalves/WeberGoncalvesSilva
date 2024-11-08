# Realização dos laboratórios AWS

**Evidência 01 - criaçao do bucket na AWS.**

![weber](/SPRINTS/SPRINT_6/EVIDÊNCIAS/Lab_A_01_criarBucket.png)

**Evidência 02 - Habilitando a hospedagem de site estático no bucket na AWS.**

![weber](/SPRINTS/SPRINT_6/EVIDÊNCIAS/Lab_A_02_HospedagemStatica.png)

**Evidência 03 - Adicionar política de bucket que torna o conteúdo do bucket publicamente disponível.**

![weber](/SPRINTS/SPRINT_6/EVIDÊNCIAS/Lab_A_03_PoliticaBucket.png)
![weber](/SPRINTS/SPRINT_6/EVIDÊNCIAS/Lab_A_04_PoliticaBucket.png)

**Evidência 04 - uploado dos arquivos CSV e o de erro com o nome 404.html.**

![weber](/SPRINTS/SPRINT_6/EVIDÊNCIAS/Lab_A_05_UploadArq_CSV.png)
![weber](/SPRINTS/SPRINT_6/EVIDÊNCIAS/Lab_A_06_UploadArq_404-erro.png)

**Evidência 05 -  testar o endpoint do site.**

![weber](/SPRINTS/SPRINT_6/EVIDÊNCIAS/Lab_A_07_Endpoint_siteDeBucket.png)

## **Utilizando Athena- serviço de consultas interativas.**

**Evidência 06 - Configurar Athena.**
![weber](/SPRINTS/SPRINT_6/EVIDÊNCIAS/Lab_B_08_conf-Athenas.png)

**Evidência 07 - Criando banco de dados.**
![weber](/SPRINTS/SPRINT_6/EVIDÊNCIAS/Lab_B_09_CriarBD_Tabela.png)

**Evidência 08 - Teste os dados com a seguinte consulta 15 nomes de 1999.**
**Código**
```yaml annotate
select nome from meubanco.nomes where ano = 1999 order by total limit 15;
```
![weber](/SPRINTS/SPRINT_6/EVIDÊNCIAS/Lab_B_10a_consulta1999.png)
**OBS:Na pasta dde evidencia tem o aquirvo gerado da consulta: Lab_B_10b-arq-gerado-consultar-1999.csv**

**Evidência 09 - 2º Teste de uma consulta que lista os 3 nomes mais usados em cada década desde o 1950 até hoje.**
**Código** 
```yaml annotate
WITH NomePorDecada AS (
    SELECT 
        nome,
        FLOOR(ano / 10) * 10 AS decada,  -- Agrupa os anos por década
        COUNT(*) AS quantidade
    FROM 
        nomes
    WHERE 
        ano >= 1950  -- Considera apenas anos a partir de 1950
    GROUP BY 
        nome, 
        FLOOR(ano / 10) * 10  -- Agrupa por nome e década
),
RankedNomes AS (
    SELECT 
        nome,
        decada,
        quantidade,
        ROW_NUMBER() OVER (PARTITION BY decada ORDER BY quantidade DESC) AS rank
    FROM 
        NomePorDecada
)
SELECT 
    decada,
    nome,
    quantidade
FROM 
    RankedNomes
WHERE 
    rank <= 3  -- Filtra os 3 nomes mais comuns por década
ORDER BY 
    decada, 
    quantidade DESC;
```
![weber](/SPRINTS/SPRINT_6/EVIDÊNCIAS/Lab_B_10_consulta1950.png)

**OBS: Na pasta dde evidencia tem o aquirvo gerado da consulta: Lab_B_arq-gerado-consultar-1950.csv**

**Resultados das consunta no bucket**
![weber](/SPRINTS/SPRINT_6/EVIDÊNCIAS/Lab_B_10c_resultados-consulta.png)


### serviço AWS Lambda
**O serviço AWS Lambda não possui a biblioteca pandas. Por isso, foi criar uma layer(camada) para importar bibliotecas necessárias a nossa Lambda.**

**É Importante, pois camadas do Lambda fornecem um modo conveniente de empacotar bibliotecas e outras dependências que podem ser usada nas funções Lambda. O uso de camadas reduz o tamanho dos arquivos de implantação carregados e acelera a implantação do código.**

**Usando um método, foi instalado as bibliotecas python e suas dependências necessárias em pasta de um Conteiner Docker, compactei-os para serem carregados na como camada da função Lambda.**

**Criei uma pasta e fiz o arquivo Dockerfile, nele continha imagem de sistema operacional Linux específica da Amazon e instalador o python versão 3.9 e a ferramenta para fazer a compressão dos dados.**

### Passo 01 arquivo Dockerfile com instruções da imagem
 
```yaml annotate
FROM amazonlinux:2023
RUN yum update -y
RUN yum install -y \
python3-pip \
zip
RUN yum -y clean all
```
### Passo 02 Usando o terminal rodar comados docker
```yaml annotate
#criado Imagem
docker build -t amazonlinuxpython39 .

#o Docker, Cria e inicia um novo contêiner a partir da imagem amazonlinuxpython39.
#(-it) permite interagir com o contêiner de maneira interativa.
docker run -it amazonlinuxpython39 bash
```
### Usando o terminal criar pastas
```yaml annotate
 cd ~		    #comando muda o diretório atual para o diretório home do usuário.
mkdir layer_dir  #cria um diretório chamado layer_dir no diretório atual
cd layer_dir/    #muda o diretório atual para o diretório layer_dir
mkdir python     #muda o diretório atual para o diretório python
cd python/       #comando muda o diretório atual para o diretório python
pwd              #o comando para imprimir o diretório de trabalho atual
pip3 install pandas -t . # instalando as bibliotecas Python
cd ..
zip -r minha-camada-pandas.zip . #Compactou todos os arquivos em um arquivo chamado minha-camada-pandas.zip
docker container ls
```
**Evidência 11 - o upload realizado do arquivo: minha-camada-pandas.zip .**
![weber](/SPRINTS/SPRINT_6/EVIDÊNCIAS/Lab_C_11_Upload-Arq-minhaCamadaPandas.png)

**Evidência 12 - Camada PandasLayer criada com sucesso.**

![weber](/SPRINTS/SPRINT_6/EVIDÊNCIAS/Lab_C_12_Criando-CamadaPandasLayer.png)

**Evidência 13 - todos Uploads esperados.**

![weber](/SPRINTS/SPRINT_6/EVIDÊNCIAS/Lab_C_13_Bucket.png)


**Evidência 14 - A função Runtime atualizada com êxito.**

![weber](/SPRINTS/SPRINT_6/EVIDÊNCIAS/Lab_C_13_Execultando-Lambda.png)