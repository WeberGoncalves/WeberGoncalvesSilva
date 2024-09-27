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


