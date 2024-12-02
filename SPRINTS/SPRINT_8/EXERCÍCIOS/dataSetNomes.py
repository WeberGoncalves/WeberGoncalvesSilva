import random
import names

def definir_parametros():    
    qtd_nomes_aleatorios = 1000000  
    qtd_nomes_unicos = 300       
    random.seed(42)  
    return qtd_nomes_aleatorios, qtd_nomes_unicos

def gerar_nomes_unicos(qtd_nomes_unicos):    
    aux = []
    for _ in range(qtd_nomes_unicos):
        aux.append(names.get_full_name())
    return aux

def gerar_nomes_aleatorios(aux, qtd_nomes_aleatorios):    
    dados = [random.choice(aux) for _ in range(qtd_nomes_aleatorios)]
    return dados

def salvar_nomes_em_arquivo(dados, nome_arquivo='nomes_aleatorios.txt'):    
    with open(nome_arquivo, 'w') as file:
        for nome in dados:
            file.write(nome + '\n')
    print(f"Arquivo '{nome_arquivo}' criado com sucesso!")

def main():
    qtd_nomes_aleatorios, qtd_nomes_unicos = definir_parametros()
    aux = gerar_nomes_unicos(qtd_nomes_unicos)
    print(f"Gerando {qtd_nomes_aleatorios} nomes aleatórios")
    dados = gerar_nomes_aleatorios(aux, qtd_nomes_aleatorios)
    salvar_nomes_em_arquivo(dados)

if __name__ == "__main__":
    main()
