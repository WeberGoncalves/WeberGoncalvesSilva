def my_map(lista, funcao):
    return [quadrado(elemento) for elemento in lista]

# Função para elevar ao quadrado
def quadrado(x):
    return x ** 2

# Lista de entrada
lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Aplicando a função square a cada elemento da lista de entrada
resultado = my_map(lista_de_numeros, quadrado)

# Imprimindo o resultado
print(resultado)