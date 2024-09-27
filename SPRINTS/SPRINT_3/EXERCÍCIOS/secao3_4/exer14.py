def imprimir_parametros(*args, **kwargs):
    # Imprimir parâmetros não nomeados
    for arg in args:
        print(arg)
    
    # Imprimir parâmetros nomeados
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

# Testando a função com os parâmetros fornecidos
imprimir_parametros(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

