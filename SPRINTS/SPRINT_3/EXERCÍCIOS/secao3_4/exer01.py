import datetime

def pessoa100(idade):
    ano_atual = datetime.datetime.now().year
    ano_100_anos = ano_atual + (100 - idade)
    return ano_100_anos

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
com_100_anos=pessoa100(idade)
print(f"{nome} completará 100 anos no ano de {com_100_anos}.")
