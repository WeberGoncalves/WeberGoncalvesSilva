# DESAFIO sprint 07

**Nesse desafio tive a oportunidade de utiliza uma nova biblioteca, a TMDB, pude praticar criar um layer para essa biblioteca, criei algoritmo de busca de filmes no vs code e depois reescrever para usara-lo no aws lambda.**

**Evidência 01 - foi necessario criar conta no site TMDB para poder utilizar cheve apiTmdb.**

![weber](/SPRINTS/SPRINT_7/EVIDÊNCIAS/TestandoCredencias_01-API_TMDB.png)

**Evidência 02 - Com script simples para testar a chave tmdb.** 

![weber](/SPRINTS/SPRINT_7/EVIDÊNCIAS/TestandoCredencias_02-API_TMDB.png)

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
### **A proxima etapa do desafio foi criar algoritmo que buscasse com biblioteca TMDB, filmes Crime e guerra.**
**Nessa fase realizei testes do algoritmo `VScodeLambda.py` no vs code, e gerou resultados com nome `analise_filmes_historicos_dramas.json`como pode observa os arquivos na pasta desafio.**

**Algoritmo utilizado no vs code.**

```yaml annotate
import requests
import json
from datetime import datetime

def buscar_filmes(chave_api, generos, ano_inicio, ordenacao="vote_average.desc", limite=100):
    url_base = "https://api.themoviedb.org/3/discover/movie"
    filmes = []
    pagina = 1
    while len(filmes) < limite: 
        parametros = 
        {
            "api_key": chave_api,
            "language": "en-US",  
            "with_genres": ','.join(map(str, generos)),
            "primary_release_date.gte": f"{ano_inicio}-01-01",
            "sort_by": ordenacao,
            "page": pagina,
        }
        
        resposta = requests.get(url_base, params=parametros)
        if resposta.status_code == 200:
            dados = resposta.json()
            filmes.extend(dados.get("results", []))
            if not dados.get("results"):  
                break
            pagina += 1  
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
            artistas = 
            [
                {
                    "personagem": ator.get("character"),
                    "nome_artista": ator.get("name"),
                    "genero_artista": ator.get("gender")
                }
                for ator in dados_creditos.get("cast", [])
            ]
            detalhes_filmes.append(
            {
                "titulo_original": filme["original_title"],
                "ano_lancamento": filme["release_date"],
                "genero": filme["genre_ids"],  
                "nota_media": filme["vote_average"],
                "numero_votos": filme["vote_count"],
                "artistas": artistas
            })
    return detalhes_filmes

def salvar_resultados(dados, nome_arquivo):
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)
    print(f"Resultados salvos no arquivo: {nome_arquivo}")

# Função principal
def main():
    chave_api = "########"  
    generos_ids = [80, 10752]  
    ano_inicio = datetime.now().year - 50  
    
    filmes_votados = buscar_filmes(chave_api, generos_ids, ano_inicio, "vote_average.desc")
    
    detalhes_filmes = coletar_detalhes_filmes(filmes_votados, chave_api)
    
    salvar_resultados(detalhes_filmes, "filmes_crime_guerra.json")
    
    total_filmes_encontrados = len(detalhes_filmes)
    print(f"Total de filmes encontrados: {total_filmes_encontrados}")
    
    # Imprimir lista de anos dos filmes encontrados
    anos_filmes = [filme["ano_lancamento"][:4] for filme in detalhes_filmes]
    print("Anos dos filmes encontrados:", anos_filmes)

if __name__ == "__main__":
    main()
```

### **Para executar a função aws lambda, foi necessario criar uma camada 'Layer' com as bibliotecas requests e Tmdb **

```yaml annotate
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
```
**Evidência 03- criação do diretório onde ocorrera instalações das bibliotecas.**

![weber](/SPRINTS/SPRINT_7/EVIDÊNCIAS/Layer_01_A-criandoPath.png)

**Evidência 04- continuação da criação do diretório.**

![weber](/SPRINTS/SPRINT_7/EVIDÊNCIAS/Layer_01_B-criandoPath.png)

**Evidência 05- instalada Biblioteca requests.**

![weber](/SPRINTS/SPRINT_7/EVIDÊNCIAS/Layer_03_isntall_requests.png)

**Evidência 06- instalada Biblioteca tmdbv3api.**

![weber](/SPRINTS/SPRINT_7/EVIDÊNCIAS/Layer_04_isntall_tmdbv3api.png)

**Evidência 07- usando o terminal do Windows para Compactar todos os arquivos das Bibliotecas instaladas na pasta Python.**

![weber](/SPRINTS/SPRINT_7/EVIDÊNCIAS/Layer_05_Zip_tmdbv3api.png)

**Evidência 08- upload do layer criado para lambda.**

![weber](/SPRINTS/SPRINT_7/EVIDÊNCIAS/Layer_06_upload_tmdb3api.png)

**Evidência 09- configurando as permissões necessarias para usa lambda.**

![weber](/SPRINTS/SPRINT_7/EVIDÊNCIAS/Layer_07_permissoes-necessarias-lambda-s3.png)

**Evidência 10- configurando as variáveis de ambientes no lambda.**

![weber](/SPRINTS/SPRINT_7/EVIDÊNCIAS/Desafio-2A-script-antes-execultado.png)

**Evidência 11- algoritmo sendo execultado no lambda.**

![weber](/SPRINTS/SPRINT_7/EVIDÊNCIAS/Desafio-2B-script-execultado.png)

**Evidência 12- resultado da execução do algoritmo.**

![weber](/SPRINTS/SPRINT_7/EVIDÊNCIAS/Desafio-2C-script-final-execução.png)

**Evidência 13- foi enviados as pesquisa dos filmes para diretorio dentro do bucket s3.**

![weber](/SPRINTS/SPRINT_7/EVIDÊNCIAS/Desafio-2D-arquivos-gerados-S3.png)

**Evidência 14- foi ajuste no diretorio dentro do bucket s3.**

![weber](/SPRINTS/SPRINT_7/EVIDÊNCIAS/Desafio-2E-arquivos-gerados-S3.png)

**Algoritmo utilizado no AWS Lambda.**
```yaml annotate
import json
import requests
from datetime import datetime
import boto3
import os

# Função para buscar filmes pelo TMDb
def buscar_filmes(chave_api, genero_id, ano_inicio, ordenacao="vote_average.desc", limite=5000):
    url_base = "https://api.themoviedb.org/3/discover/movie"
    filmes = []
    pagina = 1
    while len(filmes) < limite:
        parametros = {
            "api_key": chave_api,
            "language": "en-US",
            "with_genres": genero_id,
            "primary_release_date.gte": f"{ano_inicio}-01-01",
            "sort_by": ordenacao,
            "page": pagina,
            "include_adult": False,
            "with_original_language": "en",
            "vote_count.gte": 1,
        }

        resposta = requests.get(url_base, params=parametros)
        if resposta.status_code == 200:
            dados = resposta.json()
            filmes.extend(dados.get("results", []))
            if not dados.get("results"):
                break
            pagina += 1
        else:
            print(f"Erro na página {pagina}: {resposta.status_code}")
            break

    filmes_detalhados = []
    for filme in filmes[:limite]:
        filme_id = filme["id"]
        detalhes = buscar_detalhes_filme(chave_api, filme_id)
        if detalhes:
            if detalhes["orcamento"] > 1000 and detalhes["receita"] > 1000:
                filmes_detalhados.append(detalhes)

    return filmes_detalhados

# Função para buscar detalhes do filme pelo TMDb
def buscar_detalhes_filme(chave_api, filme_id):
    url_base = f"https://api.themoviedb.org/3/movie/{filme_id}"
    parametros = {"api_key": chave_api, "language": "en-US", "append_to_response": "credits"}

    resposta = requests.get(url_base, params=parametros)
    if resposta.status_code == 200:
        dados = resposta.json()
        return {
            "titulo": dados.get("title"),
            "ano": dados.get("release_date", "").split("-")[0],
            "genero": ", ".join([g["name"] for g in dados.get("genres", [])]),
            "numero_de_votos": dados.get("vote_count"),
            "nota_media": dados.get("vote_average"),
            "nome_artistico": ", ".join([p["name"] for p in dados.get("credits", {}).get("cast", []) if p["order"] == 0]),
            "ator_principal": dados.get("credits", {}).get("cast", [{}])[0].get("name") if dados.get("credits", {}).get("cast") else "Desconhecido",
            "orcamento": dados.get("budget"),
            "receita": dados.get("revenue"),
        }
    else:
        print(f"Erro ao buscar detalhes do filme {filme_id}: {resposta.status_code}")
        return None

# Função para salvar resultados em arquivos JSON agrupados no S3
def salvar_arquivos_json_agrupados(filmes, bucket_name, s3_client):
    data_processamento = datetime.now().strftime("%Y/%m/%d")
    prefixo_s3 = f"RAW/TMDB/json/{data_processamento}/"
    print(f"Prefixo S3: {prefixo_s3}")

    for i in range(0, len(filmes), 1000):
        chunk = filmes[i:i + 1000]
        nome_arquivo = f"filmes_{i // 1000 + 1}.json"
        caminho_local = f"/tmp/{nome_arquivo}"

        # Salvar o arquivo temporariamente no /tmp
        try:
            with open(caminho_local, "w", encoding="utf-8") as arquivo:
                json.dump(chunk, arquivo, ensure_ascii=False, indent=4)
            print(f"Arquivo criado localmente: {caminho_local}")
        except Exception as e:
            print(f"Erro ao salvar o arquivo localmente: {e}")
            raise

        # Enviar para o S3
        s3_path = f"{prefixo_s3}{nome_arquivo}"
        try:
            print(f"Enviando arquivo para o S3: {s3_path}")
            s3_client.upload_file(caminho_local, bucket_name, s3_path)
            print(f"Arquivo salvo no S3: {s3_path}")
        except Exception as e:
            print(f"Erro ao enviar o arquivo para o S3: {e}")
            raise

# Função principal para execução no Lambda
def lambda_handler(event, context):
    try:
        chave_api = os.environ.get("TMDB_API_KEY")
        bucket_name = os.environ.get("S3_BUCKET_NAME").strip()  # Remover espaços extras do nome do bucket
        if not chave_api or not bucket_name:
            raise ValueError("As variáveis de ambiente TMDB_API_KEY e S3_BUCKET_NAME devem estar configuradas.")

        genero_crime_id = 80  # ID do gênero Crime no TMDb
        ano_inicio = datetime.now().year - 50

        # Cliente S3
        s3_client = boto3.client("s3")

        # Buscar filmes
        filmes_crime = buscar_filmes(chave_api, genero_crime_id, ano_inicio, "vote_average.desc", 5000)

        # Salvar arquivos no S3
        salvar_arquivos_json_agrupados(filmes_crime, bucket_name, s3_client)

        print(f"Processamento concluído. Total de filmes processados: {len(filmes_crime)}")
        return {
            "statusCode": 200,
            "body": json.dumps({"mensagem": "Processamento concluído.", "total_filmes": len(filmes_crime)}),
        }

    except ValueError as ve:
        print(f"Erro de configuração: {ve}")
        return {
            "statusCode": 500,
            "body": json.dumps({"erro": f"Erro de configuração: {ve}"}),
        }
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return {
            "statusCode": 500,
            "body": json.dumps({"erro": f"Erro inesperado: {e}"}),
        }

```