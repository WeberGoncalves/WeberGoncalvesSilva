# Exercícios da Sprint 03
### Aqui encontra os exercícios das seções 3 e 4,  como evidências que foram lançado no Udemy, tem as imagens a baixo.
### **Imagem 01 do Udemy**
 ![weber](/SPRINTS/SPRINT_3/EVIDÊNCIAS/udemy_exercicios01.png)

 ### **Imagem 02 do Udemy**
 ![weber](/SPRINTS/SPRINT_3/EVIDÊNCIAS/udemy_exercicios02.png)

## **Exercício 01**
**A chamada da função pessoa100() com a idade fornecida pelo usuário. Exibe uma mensagem informando o ano em que o usuário completará 100 anos.**
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
**O algoritmo identifica e imprime se cada número na lista é par ou ímpar. Usando Laço for percorre cada número na lista numeros. A condição "if num % 2 == 0" verifica se o número é par (ou seja, se o resto da divisão por 2 é zero).**
```yaml annotate
numeros = list(range(10, 13, 1)) 

for num in numeros:
    if num % 2 == 0:             # modulo % verifica se o resto é zero 
        print(f"Par: {num}")
    else:
        print(f"Ímpar: {num}")
```
## **Exercício 03**
 **Com mesma linha de raciocínio usa um laço com a condição "if num % 2 == 0" verifica se o resto da divisão por 2 é zero. para que o algoritmo percorre todos os números de 0 a 20 e imprime apenas aqueles que são pares.**
```yaml annotate
for num in range(0, 21, 1):
     if num % 2 == 0:             
        print(num)
   
```
## **Exercício 04**
**A função e_primo() recebe um argumento "numero" , iniciamente verifica se o número for menor que 2, a função retorna False, pois números menores que 2 não são primos.Mas o coração da função é (int(numero ** 0.5) + 1) onde verifica se o número é divisível por qualquer valor de i no intervalo de 2 até a raiz quadrada do número.**

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
**Simplesmente  Imprime a data neste formato dia/mes/ano**
```yaml annotate
dia = 22
mes = 10
ano = 2022
# Imprime a data correspondente no formato dia/mes/ano
print(f"{dia}/{mes}/{ano}")
```
## **Exercício 06**
**Basicamente pega duas liste transforma para Set ou conjunto e remover nuemro duplicado em cada conjunto e depois vererifica a interseção entre os conjuntos, seja, todos os elementos que estão presentes em ambos os conjuntos. depois imprime.**
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
**Verifica quais números são ímpares na lista A e adiciona-os na lista numeros_impares e imprime-os.**
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
**A função e_palindromo() verifica se pode ser lida da mesma forma de trás para frente e de frente para trás, ignorando espaços, pontuação e acentuação. depois imprime quais delas são e não são palíndromo.**
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
**Este algoritmo combina três listas (primeirosNomes, sobreNomes, idades) em uma sequência de tuplas, adiciona um índice a cada tupla, e imprime cada tupla em um formato legível.**
```yaml annotate
primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for indice, (primeiroNome, sobreNome, idade) in enumerate(zip(primeirosNomes, sobreNomes, idades)):
    print(f"{indice} - {primeiroNome} {sobreNome} está com {idade} anos")
```
## **Exercício 10**
**O algoritmo remove duplicatas da lista original lista_primitiva e imprime a lista resultante lista_sem_duplicatas. Isso é útil quando você precisa garantir que uma lista contenha apenas elementos únicos.**
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
**Este algoritmo lê um arquivo JSON chamado person.json, converte seu conteúdo em um objeto Python usando json.load, e imprime esse objeto. Isso é útil para manipular dados JSON em Python, permitindo que trabalhe com eles de maneira mais conveniente e integrada ao seu código.**
```yaml annotate
import json

# Nome do arquivo JSON a ser lido
nome_arquivo = "person.json"

# Abrir e ler o arquivo JSON
with open(nome_arquivo, "r") as arquivo:
    # Fazer o parsing do conteúdo JSON
    dados_json = json.load(arquivo)

# Imprimir o conteúdo do arquivo JSON
print(dados_json)
```
## **Exercício 12**
**O algoritmo define uma função my_map que aplica uma função a cada elemento de uma lista e retorna uma nova lista com os resultados. Neste exemplo, a função quadrado é aplicada a cada número da lista lista_de_numeros, resultando em uma lista de quadrados desses números.**
```yaml annotate
def my_map(lista, funcao):
    return [quadrado(elemento) for elemento in lista]

# Função para elevar ao quadrado
def quadrado(x):
    return x ** 2

# Lista de entrada
lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Aplicando a função quadrada a cada elemento da lista de entrada
resultado = my_map(lista_de_numeros, quadrado)

# Imprimindo o resultado
print(resultado)
```
## **Exercício 13**
**Este algoritmo é útil para ler e exibir o conteúdo de um arquivo de texto. Ele abre o arquivo especificado, lê todo o seu conteúdo e o imprime. Isso pode ser útil para visualizar rapidamente o conteúdo de arquivos de texto em scripts Python.**
```yaml annotate
# Nome do arquivo de texto a ser lido
nome_arquivo = "arquivo_texto.txt"

# Abrir e ler o arquivo de texto
with open(nome_arquivo, "r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)

```
## **Exercício 14**
**O algoritmo com a função "imprimir_parametros(*args, **kwargs)" tem como objetivo imprimir todos os parâmetros que são passados para ela, tanto os não nomeados (também conhecidos como argumentos posicionais) quanto os nomeados (também conhecidos como argumentos de palavra-chave). Dentro da função, args é tratado como uma tupla que contém todos os argumentos posicionais passados. Já Dentro da função, kwargs é tratado como um dicionário que contém todos os argumentos nomeados passados.**
```yaml annotate
def imprimir_parametros(*args, **kwargs):
    # Imprimir parâmetros não nomeados
    for arg in args:
        print(arg)
    
    # Imprimir parâmetros nomeados
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

# Testando a função com os parâmetros fornecidos
imprimir_parametros(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)


```
## **Exercício 15**
**algoritmo com a classe Lampada tem como objetivo simular o comportamento de uma lâmpada, permitindo que ela seja ligada e desligada, e verificando seu estado atual (ligada ou desligada). "__init__" é o método inicializador da classe. Ele define o estado inicial da lâmpada.**
```yaml annotate
class Lampada:
    def __init__(self, ligada=False):
        self.ligada = ligada

    def liga(self):
        self.ligada = True

    def desliga(self):
        self.ligada = False

    def esta_ligada(self):
        return self.ligada

# Testando a classe Lampada
minha_lampada = Lampada()

# Ligar a lâmpada
minha_lampada.liga()

# Imprimir se a lâmpada está ligada
print("A lâmpada está ligada?", minha_lampada.esta_ligada())

# Desligar a lâmpada
minha_lampada.desliga()

# Imprimir se a lâmpada ainda está ligada
print("A lâmpada ainda está ligada?", minha_lampada.esta_ligada())
```
## **Exercício 16**
**O algoritmo com a função soma_numeros_em_string tem como objetivo calcular a soma de uma série de números que estão representados como uma string, separados por vírgulas.**
```yaml annotate
def soma_numeros_em_string(string_numeros):
    numeros = string_numeros.split(",")  # Dividindo a string pelos separadores de vírgula
    soma = sum(int(numero) for numero in numeros)  # Convertendo os números para inteiros e somando

    return soma
# String de números
string_numeros = "1,3,4,6,10,76"
# Chamando a função para obter a soma
soma_total = soma_numeros_em_string(string_numeros)
# Imprimindo a soma dos valores
print("Soma dos valores:", soma_total)
```
## **Exercício 17**
**Nesse algoritmo com a função divide_lista tem como objetivo dividir uma lista em três partes aproximadamente iguais. A linha "tamanho_parte = tamanho // 3" calcula o tamanho de cada uma das três partes, usando divisão inteira para garantir que o resultado seja um número inteiro.**
```yaml annotate
def divide_lista(lista):
    tamanho = len(lista)
    tamanho_parte = tamanho // 3 #calcula o tamanho de cada uma das três partes.

    parte1 = lista[:tamanho_parte]
    parte2 = lista[tamanho_parte: 2*tamanho_parte]
    parte3 = lista[2*tamanho_parte:]

    return (parte1, parte2, parte3)

# Lista de entrada
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Dividindo a lista em 3 partes iguais
parte1, parte2, parte3 = divide_lista(lista)

# Imprimindo as partes resultantes
print(parte1, parte2, parte3)
```
## **Exercício 18**
**O algoritmo tem o objetivo do código fornecido é criar uma lista de valores únicos a partir dos valores de um dicionário, eliminando quaisquer duplicatas.**
```yaml annotate
speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

# Criar um conjunto (set) dos valores para eliminar duplicatas
valores_unicos = set(speed.values())

# Converter o conjunto de valores únicos de volta para uma lista
lista_valores_unicos = list(valores_unicos)

# Imprimir a lista de valores únicos
print(lista_valores_unicos)
```
## **Exercício 19**
**O objetivo deste algoritmo é gerar uma lista de 50 números aleatórios dentro do intervalo de 0 a 500 e calcular algumas estatísticas básicas dessa lista, como o valor mínimo, máximo, média e mediana.**
```yaml annotate
import random
# Amostra aleatoriamente 50 números do intervalo 0...500
random_list = random.sample(range(500), 50)
# Ordenar a lista para calcular a mediana
random_list.sort()
# Calcular o valor mínimo, máximo e médio
valor_minimo = min(random_list)
valor_maximo = max(random_list)
soma_total = sum(random_list)
media = soma_total / len(random_list)
# Calcular a mediana
tamanho = len(random_list)
if tamanho % 2 == 0:
    mediana = (random_list[tamanho // 2 - 1] + random_list[tamanho // 2]) / 2
else:
    mediana = random_list[tamanho // 2]

# Imprimir os resultados
print(f"Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}")

```
## **Exercício 20**
**O objetivo deste algoritmo é imprimir a lista a em ordem reversa.**
```yaml annotate
a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(a[::-1])
```
## **Exercício 21**
**O objetivo deste algoritmo é demonstrar a herança e a sobrescrita de métodos em Python. A classe base "Passaro" define comportamentos genéricos, enquanto as classes derivadas "Pato" e "Pardal" especializam o comportamento do método "emitir_som" para cada tipo específico de pássaro.**
```yaml annotate
class Passaro:
    def voar(self):
        print("Passaro Voando...")

    def emitir_som(self):
        print("Passaro emitindo som...")

class Pato(Passaro):
    def emitir_som(self):
        super().emitir_som()
        print("Quack Quack")

class Pardal(Passaro):
    def emitir_som(self):
        super().emitir_som()
        print("Piu Piu")

# Testando as classes
pato = Pato()
pato.voar()
pato.emitir_som()

pardal = Pardal()
pardal.voar()
pardal.emitir_som()
```
## **Exercício 22**
**O objetivo deste algoritmo é demonstrar o uso de propriedades em Python para encapsular atributos privados, permitindo controle sobre como esses atributos são acessados e modificados. A propriedade nome permite que o atributo "privado __nome" seja manipulado de forma segura e controlada, mantendo a interface pública simples e intuitiva.**
```yaml annotate
class Pessoa:
    def __init__(self, identificador):
        self.id = identificador
        self.__nome = None

    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def get_nome(self):
        return self.__nome

    nome = property(get_nome, set_nome)

# Exemplo de uso
pessoa = Pessoa(0)
pessoa.nome = 'Fulano De Tal'
print(pessoa.nome)
```
## **Exercício 23**
**O objetivo deste algoritmo é demonstrar a criação de uma classe simples em Python que realiza operações matemáticas básicas (soma e subtração). Ele mostra como definir métodos dentro de uma classe, criar instâncias dessa classe e chamar seus métodos para realizar cálculos.**
```yaml annotate
class Calculo:
    def somar(self, x, y):
        return x + y

    def subtrair(self, x, y):
        return x - y

# Valores para teste
x = 4
y = 5

# Criando uma instância da classe Calculo
calculo = Calculo()

# Realizando as operações de soma e subtração
soma = calculo.somar(x, y)
subtracao = calculo.subtrair(x, y)

# Imprimindo os resultados
print(f"Somando: {x}+{y} = {soma}")
print(f"Subtraindo: {x}-{y} = {subtracao}")
```
## **Exercício 24**
**O objetivo deste algoritmo é demonstrar como criar uma classe em Python que pode ordenar listas de números em ordem crescente ou decrescente. Ele mostra como definir métodos dentro de uma classe, criar instâncias dessa classe e chamar seus métodos para realizar a ordenação.**
```yaml annotate
class Ordenadora:
    def __init__(self, lista):
        self.listaBaguncada = lista

    def ordenacaoCrescente(self):
        return sorted(self.listaBaguncada)

    def ordenacaoDecrescente(self):
        return sorted(self.listaBaguncada, reverse=True)

# Instanciando objetos com as listas fornecidas
crescente = Ordenadora([3, 4, 2, 1, 5])
decrescente = Ordenadora([9, 7, 6, 8])

# Ordenando as listas
resultado_crescente = crescente.ordenacaoCrescente()
resultado_decrescente = decrescente.ordenacaoDecrescente()

# Imprimindo os resultados das ordenações
print(resultado_crescente)
print(resultado_decrescente)
```
## **Exercício 25**
**O objetivo deste algoritmo é demonstrar a criação e manipulação de objetos em Python usando uma classe que representa aviões. Ele mostra como definir atributos de classe e de instância, inicializar objetos com diferentes valores e iterar sobre uma coleção de objetos para acessar e exibir suas propriedades.**
```yaml annotate
class Aviao:
    cor = "Azul"  # Atributo de classe para definir a cor como "Azul" para todas as instâncias

    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade

# Entradas fornecidas
entradas = [
    {"modelo": "BOIENG456", "velocidade_maxima": "1500 km/h", "capacidade": "400 passageiros"},
    {"modelo": "Embraer Praetor 600", "velocidade_maxima": "863 km/h", "capacidade": "14 passageiros"},
    {"modelo": "Antonov An-2", "velocidade_maxima": "258 km/h", "capacidade": "12 passageiros"}
]
# Lista para armazenar as instâncias de Aviao
avioes = []

# Instanciando objetos da classe Aviao com base nas entradas
for entrada in entradas:
    aviao = Aviao(entrada["modelo"], entrada["velocidade_maxima"], entrada["capacidade"])
    avioes.append(aviao)

# Iterando pela lista e imprimindo as informações de cada avião
for aviao in avioes:
    print(f"O avião de modelo {aviao.modelo} possui uma velocidade máxima de {aviao.velocidade_maxima}, capacidade para {aviao.capacidade} e é da cor {Aviao.cor}.")
```
# **Exercício da seção 5**

```yaml annotate
# Função para ler o arquivo e colocar os dados em listas
def ler_arquivo_para_listas(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    titulos = linhas[0].strip().split(',')
    dados = {titulo: [] for titulo in titulos}
    for linha in linhas[1:]:
        partes = linha.strip().split(',')
        for i, titulo in enumerate(titulos):
            if titulo in ['receitaBilheteriaAtor', 'numeroFilmesAtor', 'ReceitaPorFilmes', 'receitaFilmeMaisCaro']:
                dados[titulo].append(int(partes[i]))
            else:
                dados[titulo].append(partes[i])
    return dados, titulos

# Função para encontrar o ator com o maior número de filmes


def maior_numero_filmes(dados, titulos):
    max_filmes = max(dados[titulos[2]])
    index = dados[titulos[2]].index(max_filmes)
    nome = dados[titulos[0]][index]
    with open('etapa-1.txt', 'w') as arquivo:
        arquivo.write(f'{nome} participou de {max_filmes} filmes')


def media_receita_filme_mais_caro(dados, titulos):
    total_gross = 0
    num_filmes = len(titulos) - 1
    total_gross += titulos[-1]


media_receita_bruta = total_gross / num_filmes
with open('etapa-2.txt', 'w') as arquivo:
    arquivo.write(f'Média da receita do filme mais caro: {
                  media_receita_bruta:.2f}')


# Função para encontrar o ator com a maior ReceitaPorFilmes
def maior_receita_por_filmes(dados, titulos):
    max_receita = max(dados[titulos[3]])
    index = dados[titulos[3]].index(max_receita)
    nome = dados[titulos[0]][index]
    with open('etapa-3.txt', 'w') as arquivo:
        arquivo.write(f'{nome} tem a maior receita por filme: {max_receita}')

# Função para contar aparições de cada filme e ordenar


def contar_aparicoes_filmes(dados, titulos):
    from collections import Counter
    contagem = Counter(dados[titulos[4]])
    contagem_ordenada = sorted(
        contagem.items(), key=lambda x: x[1], reverse=True)
    with open('etapa-4.txt', 'w') as arquivo:
        for filme, quantidade in contagem_ordenada:
            arquivo.write(f'{filme}: {quantidade}\n')

# Função para ordenar atores pela receitaBilheteriaAtor


def ordenar_atores_por_receita(dados, titulos):
    atores_ordenados = sorted(
        zip(dados[titulos[0]], dados[titulos[1]]), key=lambda x: x[1], reverse=True)
    with open('etapa-5.txt', 'w') as arquivo:
        for ator, receita in atores_ordenados:
            arquivo.write(f'{ator}: {receita}\n')


# Executar as funções
dados, titulos = ler_arquivo_para_listas('actors.csv')
maior_numero_filmes(dados, titulos)
media_receita_filme_mais_caro(dados, titulos)
maior_receita_por_filmes(dados, titulos)
contar_aparicoes_filmes(dados, titulos)
ordenar_atores_por_receita(dados, titulos)
```

