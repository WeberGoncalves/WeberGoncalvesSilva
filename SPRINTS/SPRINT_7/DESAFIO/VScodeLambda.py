import requests
import json
from datetime import datetime

# Função para buscar filmes pelo TMDb
def buscar_filmes(chave_api, generos, ano_inicio, ordenacao="vote_average.desc", limite=100):
    url_base = "https://api.themoviedb.org/3/discover/movie"
    filmes = []
    pagina = 1
    while len(filmes) < limite:  # Continuar até encontrar o limite desejado
        parametros = {
            "api_key": chave_api,
            "language": "en-US",  # Garantir que os dados sejam em inglês
            "with_genres": ','.join(map(str, generos)),
            "primary_release_date.gte": f"{ano_inicio}-01-01",
            "sort_by": ordenacao,
            "page": pagina,
        }
        
        resposta = requests.get(url_base, params=parametros)
        if resposta.status_code == 200:
            dados = resposta.json()
            filmes.extend(dados.get("results", []))
            if not dados.get("results"):  # Se não houver mais resultados, parar
                break
            pagina += 1  # Avançar para a próxima página
        else:
            print(f"Erro na página {pagina}: {resposta.status_code}")
            break

    return filmes[:limite]  # Limitar a lista de filmes ao número máximo desejado

# Função para coletar dados detalhados dos filmes
def coletar_detalhes_filmes(filmes, chave_api):
    detalhes_filmes = []
    for filme in filmes:
        id_filme = filme["id"]
        url_detalhes = f"https://api.themoviedb.org/3/movie/{id_filme}/credits?api_key={chave_api}&language=en-US"
        resposta = requests.get(url_detalhes)
        if resposta.status_code == 200:
            dados_creditos = resposta.json()
            artistas = [
                {
                    "personagem": ator.get("character"),
                    "nome_artista": ator.get("name"),
                    "genero_artista": ator.get("gender")
                }
                for ator in dados_creditos.get("cast", [])
            ]
            detalhes_filmes.append({
                "titulo_original": filme["original_title"],
                "ano_lancamento": filme["release_date"],
                "genero": filme["genre_ids"],  # IDs dos gêneros
                "nota_media": filme["vote_average"],
                "numero_votos": filme["vote_count"],
                "artistas": artistas
            })
    return detalhes_filmes

# Função para salvar os resultados em um arquivo JSON
def salvar_resultados(dados, nome_arquivo):
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)
    print(f"Resultados salvos no arquivo: {nome_arquivo}")

# Função principal
def main():
    chave_api = "69ffc9d18f474342b528dea570e23a23"  # Substitua pela sua chave de API do TMDb
    generos_ids = [80, 10752]  # IDs dos gêneros "crime" (80) e "guerra" (10752)
    ano_inicio = datetime.now().year - 50  # Últimos 50 anos
    
    # Buscar filmes dos gêneros crime e guerra, mais votados
    filmes_votados = buscar_filmes(chave_api, generos_ids, ano_inicio, "vote_average.desc")
    
    # Coletar detalhes dos filmes
    detalhes_filmes = coletar_detalhes_filmes(filmes_votados, chave_api)
    
    # Salvar resultados
    salvar_resultados(detalhes_filmes, "filmes_crime_guerra.json")
    
    # Contabilizar quantos filmes foram encontrados
    total_filmes_encontrados = len(detalhes_filmes)
    print(f"Total de filmes encontrados: {total_filmes_encontrados}")
    
    # Imprimir lista de anos dos filmes encontrados
    anos_filmes = [filme["ano_lancamento"][:4] for filme in detalhes_filmes]
    print("Anos dos filmes encontrados:", anos_filmes)

# Executar o script
if __name__ == "__main__":
    main()