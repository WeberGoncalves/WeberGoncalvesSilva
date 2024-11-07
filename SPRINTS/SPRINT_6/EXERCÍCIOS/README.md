# Realização dos laboratórios AWS

**Evidência 01 de criaçao do bucket na AWS.**

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
**OBS:Na pasta dde evidencia tem o aquirvo grado da consulta: Lab_B_10b-arq-gerado-consultar-1999.csv**

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

**OBS: Na pasta dde evidencia tem o aquirvo grado da consulta: Lab_B_arq-gerado-consultar-1950.csv**

**Resultados das consunta no bucket**
![weber](/SPRINTS/SPRINT_6/EVIDÊNCIAS/Lab_B_10c_resultados-consulta.png)

