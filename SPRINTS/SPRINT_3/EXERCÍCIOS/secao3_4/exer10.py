def remover_duplicatas(lista):
    return list(set(lista))

# Lista de teste
lista_primitiva = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

# Chamando a função e armazenando o resultado em uma nova lista
lista_sem_duplicatas = remover_duplicatas(lista_primitiva)

# Imprimindo a nova lista sem elementos duplicados
print(lista_sem_duplicatas)