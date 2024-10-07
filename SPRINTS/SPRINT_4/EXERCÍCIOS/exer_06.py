def maiores_que_media(conteudo):
    # Calcular a média dos preços
    media = sum(conteudo.values()) / len(conteudo)
    # Filtrar produtos com preço acima da média
    produtos_acima_da_media = [
        (nome, preco) for nome, preco in conteudo.items() if preco > media
    ]
    # Ordenar os produtos pelo preço em ordem crescente
    produtos_acima_da_media.sort(key=lambda x: x[1])
    return produtos_acima_da_media
# Exemplo de uso
conteudo = {
    "arroz": 4.99,
    "feijão": 3.49,
    "macarrão": 2.99,
    "leite": 3.29,
    "pão": 1.99
}
resultado = maiores_que_media(conteudo)
print(resultado)  # Saída: [('feijão', 3.49), ('arroz', 4.99)]
