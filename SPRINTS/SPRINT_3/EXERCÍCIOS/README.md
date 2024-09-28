# Exercícios da Sprint 03
## **Exercício 01**
```yaml annotate 
import datetime

def pessoa100(idade):
    ano_atual = datetime.datetime.now().year
    ano_100_anos = ano_atual + (100 - idade)
    return ano_100_anos

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
com_100_anos=pessoa100(idade)
print(f"{nome} completará 100 anos no ano de {com_100_anos}.")
```
## **Exercício 02**
```yaml annotate
numeros = list(range(10, 13, 1))  # Adiciona os números 1, 3, 5 à lista

for num in numeros:
    if num % 2 == 0:             # modulo % verifica se o resto é zero 
        print(f"Par: {num}")
    else:
        print(f"Ímpar: {num}")
```
## **Exercício 03**
```yaml annotate
for num in range(0, 21, 1):
     if num % 2 == 0:             # modulo % verifica se o resto é zero 
        print(num)
   
```
## **Exercício 04**
```yaml annotate
def e_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

for num in range(1, 101):
    if e_primo(num):
        print(num)
```
## **Exercício 05**
```yaml annotate
dia = 22
mes = 10
ano = 2022
# Imprime a data correspondente no formato dia/mes/ano
print(f"{dia}/{mes}/{ano}")
```
## **Exercício 06**
```yaml annotate
a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Converte as listas em conjuntos para remover duplicatas e encontrar a interseção
set_a = set(a)
set_b = set(b)

# Encontra a interseção entre os conjuntos
intersecao = set_a.intersection(set_b)

# Imprime a lista de valores da interseção na saída padrão
print(list(intersecao))
```
## **Exercício 07**
```yaml annotate
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Inicializa uma lista vazia para armazenar os números ímpares
numeros_impares = []

# Percorre a lista 'a' e adiciona os números ímpares à lista 'numeros_impares'
for num in a:
    if num % 2 != 0:
        numeros_impares.append(num)

# Imprime a lista contendo apenas números ímpares
print(numeros_impares)
```
## **Exercício 08**
```yaml annotate
palavras = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

def e_palindromo(palavra):
    return palavra == palavra[::-1]

for palavra in palavras:
    if e_palindromo(palavra):
        print(f"A palavra: {palavra} é um palíndromo")
    else:
        print(f"A palavra: {palavra} não é um palíndromo")

```
## **Exercício 09**
```yaml annotate
primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for indice, (primeiroNome, sobreNome, idade) in enumerate(zip(primeirosNomes, sobreNomes, idades)):
    print(f"{indice} - {primeiroNome} {sobreNome} está com {idade} anos")
```
## **Exercício 10**
```yaml annotate
def remover_duplicatas(lista):
    return list(set(lista))

# Lista de teste
lista_primitiva = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

# Chamando a função e armazenando o resultado em uma nova lista
lista_sem_duplicatas = remover_duplicatas(lista_primitiva)

# Imprimindo a nova lista sem elementos duplicados
print(lista_sem_duplicatas)
```
## **Exercício 11**
```yaml annotate

```
## **Exercício 12**
```yaml annotate

```
## **Exercício 13**
```yaml annotate

```
## **Exercício 14**
```yaml annotate

```
## **Exercício 15**
```yaml annotate

```
## **Exercício 16**
```yaml annotate

```
## **Exercício 17**
```yaml annotate

```
## **Exercício 18**
```yaml annotate

```
## **Exercício 19**
```yaml annotate

```
## **Exercício 20**
```yaml annotate

```
## **Exercício 21**
```yaml annotate

```
## **Exercício 22**
```yaml annotate

```
## **Exercício 23**
```yaml annotate

```
## **Exercício 24**
```yaml annotate

```
## **Exercício 25**
```yaml annotate

```



