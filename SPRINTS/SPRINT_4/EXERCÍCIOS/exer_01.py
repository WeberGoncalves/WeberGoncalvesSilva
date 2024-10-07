""" _______________________________________________________________________________________________________________________
Questão 01 - Você está recebendo um arquivo contendo 10.000 números inteiros, um em cada linha. Utilizando lambdas e high order functions, apresente os 5 maiores valores pares e a soma destes.
Você deverá aplicar as seguintes funções no exercício:
map , filter, sorted, sum, Seu código deverá exibir na saída (simplesmente utilizando 2 comandos `print()`):
a lista dos 5 maiores números pares em ordem decrescente;a soma destes valores.
"""
# Abrindo o arquivo e lendo os números
with open('numeros.txt', 'r') as file:
    numeros = list(map(int, file.readlines()))
# Filtrando os números pares
pares = list(filter(lambda x: x % 2 == 0, numeros))
# Ordenando os números pares em ordem decrescente e pegando os 5 maiores
maiores_pares = sorted(pares, reverse=True)[:5]
# Calculando a soma dos 5 maiores números pares
soma_maiores_pares = sum(maiores_pares)
# Exibindo os resultados
print(maiores_pares)
print(soma_maiores_pares)

""" _______________________________________________________________________________________________________________________
Questão 02 - Utilizando high order functions, implemente o corpo da função conta_vogais. O parâmetro de entrada será uma string e o resultado deverá ser a contagem de vogais presentes em seu conteúdo. 
É obrigatório aplicar as seguintes funções: len , filter, lambda
Desconsidere os caracteres acentuados. Eles não serão utilizados nos testes do seu código.
"""
def conta_vogais(s):
    # Definindo as vogais
    vogais = 'aeiouAEIOU'
        # Filtrando os caracteres que são vogais
    apenas_vogais = filter(lambda x: x in vogais, s)
        # Contando o número de vogais
    return len(list(apenas_vogais))
# Exemplo de uso
texto = "Exemplo de string para contar vogais"
print(conta_vogais(texto))  # Saída: 11

""" _______________________________________________________________________________________________________________________
Questão 03 -  A função calcula_saldo recebe uma lista de tuplas, correspondendo a um conjunto de lançamentos bancários. Cada lançamento é composto pelo seu valor (sempre positivo) e pelo seu tipo (C - crédito ou D - débito). 
Abaixo apresentando uma possível entrada para a função.
lancamentos = [(200,'D'),(300,'C'),(100,'C')]
A partir dos lançamentos, a função deve calcular o valor final, somando créditos e subtraindo débitos. Na lista anterior, por exemplo, teríamos como resultado final 200.
Além de utilizar lambdas, você deverá aplicar, obrigatoriamente, as seguintes funções na resolução: reduce (módulo functools) map
"""
from functools import reduce

def calcula_saldo(lancamentos):
    # Mapeando os lançamentos para valores positivos ou negativos
    valores = map(lambda x: x[0] if x[1] == 'C' else -x[0], lancamentos)
    
    # Reduzindo a lista de valores para calcular o saldo final
    saldo_final = reduce(lambda acc, x: acc + x, valores)
    
    return saldo_final

# Exemplo de uso
lancamentos = [
    (200, 'D'),
    (300, 'C'),
    (100, 'C')
]

print(calcula_saldo(lancamentos))  # Saída: 200

""" _______________________________________________________________________________________________________________________
Questão 04 - A função calcular_valor_maximo deve receber dois parâmetros, chamados de operadores e operandos. Em operadores, espera-se uma lista de caracteres que representam as operações matemáticas suportadas (+, -, /, *, %), as quais devem ser aplicadas à lista de operadores nas respectivas posições. Após aplicar cada operação ao respectivo par de operandos, a função deverá retornar o maior valor dentre eles.
Veja o exemplo: Entrada
operadores = ['+','-','*','/','+']  operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]
Aplicar as operações aos pares de operandos [ 3+6 , -7-4.9, 8*-8 , 10/2 , 8+4 ] 
Obter o maior dos valores  12, Na resolução da atividade você deverá aplicar as seguintes funções: max, zip, map
"""
def calcular_valor_maximo(operadores, operandos):
    # Função para realizar a operação
    def aplicar_operacao(op, operando1, operando2):
        if op == '+':
            return operando1 + operando2
        elif op == '-':
            return operando1 - operando2
        elif op == '*':
            return operando1 * operando2
        elif op == '/':
            return operando1 / operando2 if operando2 != 0 else float('inf')  # Evitar divisão por zero
        elif op == '%':
            return operando1 % operando2 if operando2 != 0 else float('inf')  # Evitar divisão por zero
        else:
            raise ValueError(f"Operador desconhecido: {op}")

    # Usar zip para combinar operadores e operandos
    resultados = map(lambda x: aplicar_operacao(x[0], x[1][0], x[1][1]), zip(operadores, operandos))
    
    # Retornar o maior valor
    return max(resultados)

# Exemplo de uso
operadores = ['+', '-', '*', '/', '+']
operandos = [(3, 6), (-7, 4.9), (8, -8), (10, 2), (8, 4)]

maior_valor = calcular_valor_maximo(operadores, operandos)
print(maior_valor)  # Saída: 12

""" _______________________________________________________________________________________________________________________
Questão 05 -
Um determinado sistema escolar exporta a grade de notas dos estudantes em formato CSV. Cada linha do arquivo corresponde ao nome do estudante, acompanhado de 5 notas de avaliação, no intervalo [0-10]. É o arquivo estudantes.csv de seu exercício.
Precisamos processar seu conteúdo, de modo a gerar como saída um relatório em formato textual contendo as seguintes informações:
Nome do estudante, Três maiores notas, em ordem decrescente, Média das três maiores notas, com duas casas decimais de precisão
O resultado do processamento deve ser escrito na saída padrão (print), ordenado pelo nome do estudante e obedecendo ao formato descrito a seguir: Nome: <nome estudante> Notas: [n1, n2, n3] Média: <média>
Exemplo: Nome: Maria Luiza Correia Notas: [7, 5, 5] Média: 5.67, Nome: Maria Mendes Notas: [7, 3, 3] Média: 4.33
Em seu desenvolvimento você deverá utilizar lambdas e as seguintes funções: round, map, sorted
"""
import csv

def processar_notas(arquivo_csv):
    with open(arquivo_csv, 'r') as file:
        reader = csv.reader(file)
        estudantes = []

        for linha in reader:
            nome = linha[0]
            notas = list(map(int, linha[1:]))
            maiores_notas = sorted(notas, reverse=True)[:3]
            media_maiores_notas = round(sum(maiores_notas) / 3, 2)
            estudantes.append((nome, maiores_notas, media_maiores_notas))

        # Ordenar os estudantes pelo nome
        estudantes_ordenados = sorted(estudantes, key=lambda x: x[0])

        # Gerar o relatório
        for estudante in estudantes_ordenados:
            nome, maiores_notas, media = estudante
            print(f"Nome: {nome} Notas: {maiores_notas} Média: {media}")

# Exemplo de uso
processar_notas('estudantes.csv')
""" _______________________________________________________________________________________________________________________
Questão 06 -
Você foi encarregado de desenvolver uma nova feature  para um sistema de gestão de supermercados. O analista responsável descreveu o requisito funcional da seguinte forma: - Para realizar um cálculo de custo, o sistema deverá permitir filtrar um determinado conjunto de produtos, de modo que apenas aqueles cujo valor unitário for superior à média deverão estar presentes no resultado. Vejamos o exemplo:
Conjunto de produtos (entrada): Arroz: 4.99; Feijão: 3.49; Macarrão: 2.99 ; Leite: 3.29; Pão: 1.99
Produtos com valor acima da média: Arroz: 4.99 ; Feijão: 3.49
Observe que estamos definindo a assinatura de uma função como parte de sua resposta. Você não pode mudá-la, apenas codificar seu corpo. O parâmetro conteudo é um dicionário cuja chave contém o nome do produto e o valor, o respectivo preço (ponto flutuante).
Observe um exemplo de valor para conteudo: { "arroz": 4.99,"feijão": 3.49, "macarrão": 2.99,"leite": 3.29, "pão": 1.99}
O retorno da função obrigatoriamente deve ser uma lista. Cada elemento da lista é uma tupla em que a primeira posição contém o nome do produto e a segunda, o respectivo preço. Veja um exemplo de retorno: [('feijão', 3.49), ('arroz', 4.99)]
Importante: O retorno da função deve estar ordenado pelo preço do item (ordem crescente).
"""
def maiores_que_media(conteudo):
    # Calcular a média dos preços
    media = sum(conteudo.values()) / len(conteudo)
    # Filtrar produtos com preço acima da média
    produtos_acima_da_media = [
        (nome, preco) for nome, preco in conteudo.items() if preco > media
    ]
    # Ordenar os produtos pelo preço em ordem crescente
    produtos_acima_da_media.sort(key=lambda x: x[1])
    return produtos_acima_da_media
# Exemplo de uso
conteudo = {
    "arroz": 4.99,
    "feijão": 3.49,
    "macarrão": 2.99,
    "leite": 3.29,
    "pão": 1.99
}
resultado = maiores_que_media(conteudo)
print(resultado)  # Saída: [('feijão', 3.49), ('arroz', 4.99)]


""" _______________________________________________________________________________________________________________________
Questão 07 -
Generators são poderosos recursos da linguagem Python. Neste exercício, você deverá criar o corpo de uma função, cuja assinatura já consta em seu arquivo de início (def pares_ate(n:int):) .
O objetivo da função pares_ate é retornar um generator para os valores pares no intervalo [2,n] . Observe que n representa o valor do parâmetro informado na chamada da função.
"""
#def pares_ate(n:int):
def pares_ate(n: int):
    for i in range(2, n + 1):
        if i % 2 == 0:
            yield i

# Exemplo de uso
for par in pares_ate(10):
    print(par)
