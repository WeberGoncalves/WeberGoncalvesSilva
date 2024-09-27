speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

# Criar um conjunto (set) dos valores para eliminar duplicatas
valores_unicos = set(speed.values())

# Converter o conjunto de valores únicos de volta para uma lista
lista_valores_unicos = list(valores_unicos)

# Imprimir a lista de valores únicos
print(lista_valores_unicos)