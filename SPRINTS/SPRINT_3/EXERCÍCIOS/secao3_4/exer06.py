a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Converte as listas em conjuntos para remover duplicatas e encontrar a interseção
set_a = set(a)
set_b = set(b)

# Encontra a interseção entre os conjuntos
intersecao = set_a.intersection(set_b)

# Imprime a lista de valores da interseção na saída padrão
print(list(intersecao))