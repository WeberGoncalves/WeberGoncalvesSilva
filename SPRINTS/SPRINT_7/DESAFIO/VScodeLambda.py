import requests
import json
from datetime import datetime

# Função para buscar filmes pelo TMDb
def buscar_filmes(chave_api, genero_id, ano_inicio, ordenacao="vote_average.desc", limite=100):
    url_base = "https://api.themoviedb.org/3/discover/movie"
    filmes = []
    pagina = 1
    while len(filmes) < limite:  # Continuar até encontrar o limite desejado
        parametros = {
            "api_key": chave_api,
            "language": "pt-BR",  # Garantir que os dados sejam em português
            "with_genres": genero_id,
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

# Função para filtrar dramas baseados em fatos reais (input manual ou flag externa)
def filtrar_baseados_em_fatos(filmes, baseados_ids):
    return [filme for filme in filmes if filme["id"] in baseados_ids]

# Função para salvar os resultados em um arquivo JSON
def salvar_resultados(dados, nome_arquivo):
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)
    print(f"Resultados salvos no arquivo: {nome_arquivo}")

# Função principal
def main():
    chave_api = "69ffc9d18f474342b528dea570e23a23"  # Substitua pela sua chave de API do TMDb
    genero_drama_id = 18  # ID do gênero "drama" no TMDb
    genero_historico_id = 36  # ID do gênero "histórico" no TMDb
    ano_inicio = datetime.now().year - 60  # Últimos 60 anos
    
    # Buscar filmes do gênero drama, mais votados
    filmes_drama_votados = buscar_filmes(chave_api, genero_drama_id, ano_inicio, "vote_average.desc")
    
    # Buscar filmes do gênero histórico, mais votados
    filmes_historicos_votados = buscar_filmes(chave_api, genero_historico_id, ano_inicio, "vote_average.desc")
    
    # Combinar os resultados de ambos os gêneros
    todos_filmes_votados = filmes_drama_votados + filmes_historicos_votados
    
    # IDs de filmes baseados em fatos reais (insira manualmente ou use outra lógica)
    baseados_em_fatos_ids = [123, 456]  # Substitua pelos IDs corretos
    
    # Filtrar baseados em fatos reais
    filmes_baseados = filtrar_baseados_em_fatos(todos_filmes_votados, baseados_em_fatos_ids)
    
    # Filtrar não baseados em fatos reais
    filmes_nao_baseados = [filme for filme in todos_filmes_votados if filme["id"] not in baseados_em_fatos_ids]
    
    # Ordenar por média de votos
    filmes_nao_baseados = sorted(filmes_nao_baseados, key=lambda x: x["vote_average"], reverse=True)

    # Identificar os mais populares
    filmes_populares = sorted(todos_filmes_votados, key=lambda x: x["popularity"], reverse=True)
    
    # Resultado final
    resultado = {
        "filmes_baseados_em_fatos": filmes_baseados,
        "filmes_nao_baseados_mais_votados": filmes_nao_baseados[:10],  # Top 10 mais votados
        "filmes_populares": filmes_populares[:10],  # Top 10 mais populares
    }
    
    # Salvar resultados
    salvar_resultados(resultado, "analise_filmes_historicos_drama.json")
    
    # Contabilizar quantos filmes foram encontrados
    total_filmes_encontrados = len(todos_filmes_votados)
    print(f"Total de filmes encontrados: {total_filmes_encontrados}")

# Executar o script
if __name__ == "__main__":
    main()