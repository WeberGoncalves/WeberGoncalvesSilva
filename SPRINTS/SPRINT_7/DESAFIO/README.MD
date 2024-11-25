# DESAFIO sprint 07

**NNesse desafio tive a oportunidade de utiliza uma nova biblioteca, a TMDB, pude praticar criar um layer para essa biblioteca, criei algoritmo de busca de filmes no vs code e depois reescrever para usara-lo no aws lambda.**

**Evidência 01 - foi necessario criar conta no site TMDB para poder utilizar cheve apiTmdb.**

![weber](/SPRINT_7/EVIDÊNCIAS/TestandoCredencias_01-API_TMDB.png)

**Evidência 02 - Com script simples para testar a chave tmdb.** 

![weber](/SPRINT_7/EVIDÊNCIAS/TestandoCredencias_02-API_TMDB.png)

**Algoritmo utilizado para teste**

```yaml annotate
import requests
import pandas as pd
from IPython.display import display

api_key = "**********"
url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=pt-BR"

response = requests.get(url)
data = response.json()

filmes = []

for movie in data['results']:
    df = 
    {
        'Titulo': movie['title'],
        'Data de lançamento': movie['release_date'],
        'Visão geral': movie['overview'],
        'Votos': movie['vote_count'],
        'Média de votos': movie['vote_average']
    }
    filmes.append(df)

df = pd.DataFrame(filmes)
display(df)
```
### **A proxima etapa do desafio foi criar algoritmo que buscasse com biblioteca TMDB, filmes dramas históricos.**
**Nessa fase realizei testes do algoritmo `VScodeLambda.py` no vs code, e gerou resultados com nome `analise_filmes_historicos_dramas.json`como pode observa os arquivos na pasta desafio.**

**Algoritmo utilizado no vs code.**
```yaml annotate
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
```

### **Para executar a função aws lambda, foi necessario criar uma camada 'Layer' com as bibliotecas requests e Tmdb **

´´´ 
cd ~		    #comando muda o diretório atual para o diretório home do usuário.
mkdir layer_dir  #cria um diretório chamado layer_dir no diretório atual
cd layer_dir/    #muda o diretório atual para o diretório layer_dir
mkdir python     #muda o diretório atual para o diretório python
cd python/       #comando muda o diretório atual para o diretório python
pwd              #o comando para imprimir o diretório de trabalho atual
pip3 install requests -t . # Este comando instala a biblioteca requests usando o pip3, o instalador de pacotes para Python 3. 
pip3 install tmdbv3api -t . #comando para instalar a biblioteca tmdbv3api e a colocará no seu diretório de trabalho atual.
cd ..
Compress-Archive -Path "\Users\webgs\layer_dir\python" -DestinationPath "\Users\webgs\layer_dir\tmdbLayer.zip" #comando para terminal do Windows para Compactar todos os arquivos em um arquivo chamado tmdbLayer.zip
docker container ls
´´´
**Evidência 03- criação do diretório onde ocorrera instalações das bibliotecas.**

![weber](/SPRINT_7/EVIDÊNCIAS/Layer_01_A-criandoPath.png)

**Evidência 04- continuação da criação do diretório.**

![weber](/SPRINT_7/EVIDÊNCIAS/Layer_01_B-criandoPath.png)

**Evidência 05- instalada Biblioteca requests.**

![weber](/SPRINT_7/EVIDÊNCIAS/Layer_03_isntall_requests.png)

**Evidência 06- instalada Biblioteca tmdbv3api.**

![weber](/SPRINT_7/EVIDÊNCIAS/Layer_04_isntall_tmdbv3api.png)

**Evidência 07- usando o terminal do Windows para Compactar todos os arquivos das Bibliotecas instaladas na pasta Python.**

![weber](/SPRINT_7/EVIDÊNCIAS/Layer_05_Zip_tmdbv3api.png)

**Evidência 08- upload do layer criado para lambda.**

![weber](/SPRINT_7/EVIDÊNCIAS/Layer_06_upload_tmdb3api.png)

**Evidência 09- configurando as permissões necessarias para usa lambda.**

![weber](/SPRINT_7/EVIDÊNCIAS/Layer_07_permissoes-necessarias-lambda-s3.png)

**Evidência 10- configurando as variáveis de ambientes no lambda.**

![weber](/SPRINT_7/EVIDÊNCIAS/Desafio-2A-script-antes-execultado.png)

**Evidência 11- algoritmo sendo execultado no lambda.**

![weber](/SPRINT_7/EVIDÊNCIAS/Desafio-2B-script-execultado.png)

**Evidência 12- resultado da execução do algoritmo.**

![weber](/SPRINT_7/EVIDÊNCIAS/Desafio-2C-script-final-execução.png)

**Evidência 13- foi enviados as pesquisa dos filmes para diretorio dentro do bucket s3.**

![weber](/SPRINT_7/EVIDÊNCIAS/Desafio-2D-arquivos-gerados-S3.png)