def soma_numeros_em_string(string_numeros):
    numeros = string_numeros.split(",")  # Dividindo a string pelos separadores de vírgula
    soma = sum(int(numero) for numero in numeros)  # Convertendo os números para inteiros e somando

    return soma

# String de números
string_numeros = "1,3,4,6,10,76"

# Chamando a função para obter a soma
soma_total = soma_numeros_em_string(string_numeros)

# Imprimindo a soma dos valores
print("Soma dos valores:", soma_total)