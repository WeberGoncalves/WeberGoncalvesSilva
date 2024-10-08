# Exercícios da Sprint 04
### Aqui encontra os exercícios da seção 2,  com as evidências que foram lançadas no Udemy e foram aprovados, tem as imagens a baixo.
### **Imagem do Udemy**

 ![weber](/SPRINTS/SPRINT_4/EVIDÊNCIAS/secao2Prontos.png)

## Começa aqui a lista dos scripts dos exercícios
## **Exercício 01**
**Um detalhe interessante foi o uso da função "``sorted(pares, reverse=True)``" que Ordena a lista pares em ordem decrescente (reverse=True).[:5] Seleciona ou fatia os primeiros 5 elementos da lista ordenada, resultando nos 5 maiores números pares.**
**Resumindo, O algoritmo lê um arquivo com números, filtra os números pares, ordena os pares em ordem decrescente, seleciona os 5 maiores e calcula a soma deles.**

![weber](/SPRINTS/SPRINT_4/EVIDÊNCIAS/exer_01.png)

## **Exercício 02**
**Neste algoritmo a função "``conta_vogais()``" utiliza a função filter para extrair as vogais de uma string e, em seguida, conta o número de vogais encontradas.**

![weber](/SPRINTS/SPRINT_4/EVIDÊNCIAS/exer_02.png)

## **Exercício 03**
**O algoritmo tem a função lambda``"lambda x: x[0] if x[1] == 'C' else -x[0}"`` que recebe uma tupla (lançamento) como entrada e retorna o valor do lançamento se o tipo for 'C' (Crédito), indicando um acréscimo no saldo. O valor do lançamento multiplicado por -1 se o tipo for 'D' (Débito), indicando uma redução no saldo. A função map(...): Aplica a função lambda a cada elemento da lista lancamentos, criando um novo iterável com os valores ajustados.**

![weber](/SPRINTS/SPRINT_4/EVIDÊNCIAS/exer_03.png)

## **Exercício 04**
**A função calcular_valor_maximo recebe duas listas como entrada: uma lista de operadores aritméticos (operadores) e uma lista de pares de operandos (operandos). Ela realiza as operações especificadas pelos operadores sobre os operandos correspondentes e retorna o maior valor resultante.**

![weber](/SPRINTS/SPRINT_4/EVIDÊNCIAS/exer_04.png)

## **Exercício 05**
**Este algoritmo tem função principal, ``def processar_notas(arquivo_csv):`` que lê um arquivo CSV contendo informações sobre estudantes e suas notas. Ele processa essas informações para calcular a média das três maiores notas de cada estudante e gera um relatório ordenado alfabeticamente pelos nomes dos estudantes, alguns dos trechos importantes: ``notas = list(map(int, linha[1:])):`` que Converte as notas (a partir da segunda coluna) para números inteiros e cria uma lista com essas notas, ``maiores_notas = sorted(notas, reverse=True)[:3]:`` que Ordena as notas em ordem decrescente e seleciona as três primeiras (maiores) notas. ``media_maiores_notas = round(sum(maiores_notas) / 3, 2):`` que Calcula a média das três maiores notas e arredonda para duas casas decimais.**

![weber](/SPRINTS/SPRINT_4/EVIDÊNCIAS/exer_05.png)

## **Exercício 06**
**Esse algoritmo tem a função maiores_que_media recebe um dicionário como entrada, onde as chaves representam nomes de produtos e os valores representam seus respectivos preços. A função calcula a média dos preços, filtra os produtos com preços acima da média e retorna uma lista ordenada desses produtos, com o nome e preço de cada um.**

![weber](/SPRINTS/SPRINT_4/EVIDÊNCIAS/exer_06.png)

## **Exercício 07**
**O algoritmo define uma função que gera uma sequência de números pares de 2 até um valor especificado. Essa função utiliza um gerador para retornar os números de forma eficiente,vitando a criação de uma lista completa de números pares, ``def pares_ate(n: int):``Recebe um número inteiro N como entrada, Retorna uma sequência de números pares a partir de 2 até N. ``yield:`` É uma palavra-chave usada para criar um gerador.Um gerador é uma função especial que pausa sua execução e retorna um valor, podendo ser retomada posteriormente.**

![weber](/SPRINTS/SPRINT_4/EVIDÊNCIAS/exer_07.png)