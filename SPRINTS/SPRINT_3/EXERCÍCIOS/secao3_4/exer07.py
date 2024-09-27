a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Inicializa uma lista vazia para armazenar os números ímpares
numeros_impares = []

# Percorre a lista 'a' e adiciona os números ímpares à lista 'numeros_impares'
for num in a:
    if num % 2 != 0:
        numeros_impares.append(num)

# Imprime a lista contendo apenas números ímpares
print(numeros_impares)