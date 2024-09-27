import json

# Nome do arquivo JSON a ser lido
nome_arquivo = "person.json"

# Abrir e ler o arquivo JSON
with open(nome_arquivo, "r") as arquivo:
    # Fazer o parsing do conteúdo JSON
    dados_json = json.load(arquivo)

# Imprimir o conteúdo do arquivo JSON
print(dados_json)