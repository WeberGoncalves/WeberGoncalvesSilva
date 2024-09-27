def divide_lista(lista):
    tamanho = len(lista)
    tamanho_parte = tamanho // 3

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
#ou assim para estetica mais bonita
"""print("Parte 1:", parte1)
print("Parte 2:", parte2)
print("Parte 3:", parte3)"""
