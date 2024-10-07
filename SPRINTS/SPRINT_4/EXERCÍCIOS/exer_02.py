def conta_vogais(s):
    # Definindo as vogais
    vogais = 'aeiouAEIOU'
        # Filtrando os caracteres que são vogais
    apenas_vogais = filter(lambda x: x in vogais, s)
        # Contando o número de vogais
    return len(list(apenas_vogais))
# Exemplo de uso
texto = "Exemplo de string para contar vogais"
print(conta_vogais(texto))  # Saída: 12