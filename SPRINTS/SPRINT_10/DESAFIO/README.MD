# DESAFIO

**No último desafio das sprints, foi realizado analise dos dados do arquivo filmes.csv e dados da extensão .json, extraído por meio de algoritmo executado no aws lambda, para complementar o arquivo CSV, foi necessário realizar um limpeza e juntas os arquivos, e realizar modelagem dimensional para depois usar a ferramenta aws Quicksight para realizar analise por meio dos gráficos que explicarei a seguir.**

## Nesta Análise tem objetivo verificar o quanto publico geral gosta do genero crime em filmes,em que década teve mais atenção, e dentro deste genero crime foi analisado a preferência por genero artistico, para investigar foi usado dados sobre notas medias dos filmes, orçamento, e lucro. Esses dados foram distribuido nos graficos por ano, décadas e lucros.


**Evidência 01 -Os dados modelados foram retirados do bucket data-lake-do-weber no AWS S3 e vinculado ao quicksight.**

![weber](/SPRINTS/SPRINT_10/EVIDÊNCIAS/1_ConjuntoDados_Quicksight.png)


**Evidência 02 - Para complementar ainda mais os dados bucket foi criado dois campos calculados, um para Décadas e outro para Lucro, que é a difernça entre orçamento gasto e receitas que entreram.**

![weber](/SPRINTS/SPRINT_10/EVIDÊNCIAS/2_campoCalculado_Quicksight.png)

**Evidência 03 - Neste gráfico observamos que nas ultimas  cinco décadas os votos médios teve pequeno crescimento entre 1980 e 1990, mas que na década de 2000 houve queda, no entanto na década de 2010 começou a crescer, indicando que em que década recente as pessoas tiveram mais interesse no gênero crime.**

![weber](/SPRINTS/SPRINT_10/EVIDÊNCIAS/3_Quicksight_Grafico_01.png)


**Evidência 04 - Neste gráfico observamos que nas ultimas  cinco décadas os lucros por década teve crescimento até 2010, mas houve decréscimo na década seguinte indicando que de 2010 a 2020 diminuiu o interesse no gênero crime, podemos concluir isso, já que lucro tem ligação direta com receita, e ela esta intrínseca com quantos assistiram os filmes.**

![weber](/SPRINTS/SPRINT_10/EVIDÊNCIAS/4_Quicksight_Grafico_02.png)


**Evidência 05 - Agora inspecionando a preferência pelo gênero artístico, observamos a nota media dos filmes por gênero artístico, em que o protagonista ator ficou em mais evidencia do que as atrizes.**

![weber](/SPRINTS/SPRINT_10/EVIDÊNCIAS/5_Quicksight_Grafico_03.png)


**Evidência 06 - Seguindo raciocínio do gráfico anterior, mas agora observando a receita, o dinheiro gerado pelos filmes por gênero artístico, esta indicando a preferência maior por ator como protagonista.**

![weber](/SPRINTS/SPRINT_10/EVIDÊNCIAS/6_Quicksight_Grafico_04.png)


**Evidência 07 - Como já observado no gráfico anterior, neste gráfico também a evidência é para a preferência por ator, então ao desenvolver um projeto de filme é melhor usar ator para ter maior lucro como gráfico mostra.**

![weber](/SPRINTS/SPRINT_10/EVIDÊNCIAS/7_Quicksight_Grafico_05.png)

## **Dashboard Completo.**
**Obs: Tem uma copia em PDF com melhor visualização na pasta evidências.**

![weber](/SPRINTS/SPRINT_10/EVIDÊNCIAS/Dashboard_filmes.png)