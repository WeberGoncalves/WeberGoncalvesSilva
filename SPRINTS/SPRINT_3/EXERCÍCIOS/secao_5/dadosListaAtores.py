#Função para ler o arquivo e colocar os dados em listas
def ler_arquivo_para_listas(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    titulos = linhas[0].strip().split(',')
    dados = {titulo: [] for titulo in titulos}
    for linha in linhas[1:]:
        partes = linha.strip().split(',')
        for i, titulo in enumerate(titulos):
            if titulo in ['receitaBilheteriaAtor', 'numeroFilmesAtor', 'ReceitaPorFilmes', 'receitaFilmeMaisCaro']:
                dados[titulo].append(int(partes[i]))
            else:
                dados[titulo].append(partes[i])
    return dados, titulos

#Função para encontrar o ator com o maior número de filmes 
def maior_numero_filmes(dados, titulos):
    max_filmes = max(dados[titulos[2]])
    index = dados[titulos[2]].index(max_filmes)
    nome = dados[titulos[0]][index]
    with open('etapa-1.txt', 'w') as arquivo:
        arquivo.write(f'{nome} participou de {max_filmes} filmes')

"""#Função para calcular a média da coluna receitaFilmeMaisCaro
def media_receita_filme_mais_caro(dados, titulos):
    media = sum(dados[titulos[5]]) / len(dados[titulos[5]])
    with open('etapa-2.txt', 'w') as arquivo:
        arquivo.write(f'Média da receita do filme mais caro: {media:.2f}')"""

def media_receita_filme_mais_caro(dados, titulos):
    total_gross = 0
    num_filmes = len(titulos) - 1
    total_gross += titulos[-1]
media_receita_bruta = total_gross / num_filmes
with open('etapa-2.txt', 'w') as arquivo:
        arquivo.write(f'Média da receita do filme mais caro: {media_receita_bruta:.2f}')
 


#Função para encontrar o ator com a maior ReceitaPorFilmes
def maior_receita_por_filmes(dados, titulos):
    max_receita = max(dados[titulos[3]])
    index = dados[titulos[3]].index(max_receita)
    nome = dados[titulos[0]][index]
    with open('etapa-3.txt', 'w') as arquivo:
        arquivo.write(f'{nome} tem a maior receita por filme: {max_receita}')

#Função para contar aparições de cada filme e ordenar
def contar_aparicoes_filmes(dados, titulos):
    from collections import Counter
    contagem = Counter(dados[titulos[4]])
    contagem_ordenada = sorted(contagem.items(), key=lambda x: x[1], reverse=True)
    with open('etapa-4.txt', 'w') as arquivo:
        for filme, quantidade in contagem_ordenada:
            arquivo.write(f'{filme}: {quantidade}\n')

#Função para ordenar atores pela receitaBilheteriaAtor
def ordenar_atores_por_receita(dados, titulos):
    atores_ordenados = sorted(zip(dados[titulos[0]], dados[titulos[1]]), key=lambda x: x[1], reverse=True)
    with open('etapa-5.txt', 'w') as arquivo:
        for ator, receita in atores_ordenados:
            arquivo.write(f'{ator}: {receita}\n')
 
#Executar as funções
dados, titulos = ler_arquivo_para_listas('actors.csv')
maior_numero_filmes(dados, titulos)
media_receita_filme_mais_caro(dados, titulos)
maior_receita_por_filmes(dados, titulos)
contar_aparicoes_filmes(dados, titulos)
ordenar_atores_por_receita(dados, titulos)
