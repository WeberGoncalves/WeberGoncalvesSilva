import json
import requests
from datetime import datetime
import boto3
import os

# Função para buscar filmes pelo TMDb
def buscar_filmes(chave_api, genero_id, ano_inicio, ordenacao="vote_average.desc", limite=100):
    url_base = "https://api.themoviedb.org/3/discover/movie"
    filmes = []
    pagina = 1
    while len(filmes) < limite:
        parametros = {
            "api_key": chave_api,
            "language": "pt-BR",
            "with_genres": genero_id,
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

    return filmes[:limite]

# Função para salvar resultados em arquivos JSON agrupados no S3
def salvar_arquivos_json_agrupados(filmes, bucket_name, s3_client):
    data_processamento = datetime.now().strftime("%Y/%m/%d")
    prefixo_s3 = f"Raw/TMDB/json/{data_processamento}/"
    print(f"Prefixo S3: {prefixo_s3}")
    
    for i in range(0, len(filmes), 100):
        chunk = filmes[i:i+100]
        nome_arquivo = f"filmes_{i // 100 + 1}.json"
        caminho_local = f"/tmp/{nome_arquivo}"
        
        # Salvar o arquivo temporariamente no /tmp
        try:
            with open(caminho_local, "w", encoding="utf-8") as arquivo:
                json.dump(chunk, arquivo, ensure_ascii=False, indent=4)
            print(f"Arquivo criado localmente: {caminho_local}")
        except Exception as e:
            print(f"Erro ao salvar arquivo localmente: {e}")
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
        bucket_name = os.environ.get("S3_BUCKET_NAME")
        if not chave_api or not bucket_name:
            raise ValueError("As variáveis de ambiente TMDB_API_KEY e S3_BUCKET_NAME devem estar configuradas.")

        genero_drama_id = 18
        genero_historico_id = 36
        ano_inicio = datetime.now().year - 60

        # Cliente S3
        s3_client = boto3.client("s3")

        # Buscar filmes
        filmes_drama = buscar_filmes(chave_api, genero_drama_id, ano_inicio, "vote_average.desc", 100)
        filmes_historico = buscar_filmes(chave_api, genero_historico_id, ano_inicio, "vote_average.desc", 100)
        todos_filmes = filmes_drama + filmes_historico
        bucket_name = 'data-lake-do-weber' 
        # Salvar arquivos no S3
        salvar_arquivos_json_agrupados(todos_filmes, bucket_name, s3_client)
        
        print(f"Processamento concluído. Total de filmes processados: {len(todos_filmes)}")
        return {
            "statusCode": 200,
            "body": json.dumps({"mensagem": "Processamento concluído.", "total_filmes": len(todos_filmes)}),
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
