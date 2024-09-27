# Nome do arquivo de texto a ser lido
nome_arquivo = "arquivo_texto.txt"

# Abrir e ler o arquivo de texto
with open(nome_arquivo, "r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
