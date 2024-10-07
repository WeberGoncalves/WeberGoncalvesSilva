# Abrindo o arquivo e lendo os números
with open('number.txt', 'r') as file:
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

