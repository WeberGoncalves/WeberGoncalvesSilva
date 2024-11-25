import json
import pandas as pd

# Função para carregar os filmes do JSON
def carregar_filmes_json(caminho_json):
    try:
        with open(caminho_json, "r", encoding="utf-8") as arquivo:
            print(f"Lendo o arquivo JSON: {caminho_json}")
            dados = json.load(arquivo)
            filmes = []
            for categoria, lista_filmes in dados.items():
                filmes.extend([filme["title"] for filme in lista_filmes if "title" in filme])
            print(f"Filmes carregados do JSON: {filmes}")
            return filmes
    except FileNotFoundError:
        print(f"Arquivo JSON {caminho_json} não encontrado.")
        return []
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar o arquivo JSON {caminho_json}: {e}")
        return []

# Função para carregar os filmes do CSV usando pandas
def carregar_filmes_csv(caminho_csv):
    try:
        print(f"Lendo o arquivo CSV: {caminho_csv}")
        
        # Tentar diferentes delimitadores automaticamente
        delimitadores = [",","|" ,";", "\t"]  # Vírgula, ponto e vírgula, tabulação
        for delimitador in delimitadores:
            try:
                df = pd.read_csv(caminho_csv, encoding="utf-8", sep=delimitador, on_bad_lines="skip")
                print(f"Delimitador detectado: '{delimitador}'")
                break
            except pd.errors.ParserError:
                continue  # Tentar o próximo delimitador

        # Conferir se o DataFrame foi carregado
        if df.empty:
            print("Arquivo CSV carregado, mas está vazio.")
            return []

        # Verificar a existência da coluna 'title'
        if "title" in df.columns:
            filmes = df["title"].dropna().tolist()
            print(f"Filmes carregados do CSV: {filmes}")
            return filmes
        else:
            print("Coluna 'title' não encontrada no arquivo CSV.")
            print(f"Colunas disponíveis: {df.columns.tolist()}")
            return []
    except FileNotFoundError:
        print(f"Arquivo CSV {caminho_csv} não encontrado.")
        return []
    except pd.errors.EmptyDataError:
        print(f"Arquivo CSV {caminho_csv} está vazio.")
        return []
    except pd.errors.ParserError as e:
        print(f"Erro ao ler o arquivo CSV {caminho_csv}: {e}")
        return []

# Função principal
def verificar_filmes_existentes():
    caminho_json = "analise3_filmes_historicos.json"
    caminho_csv = "movies.csv"
    caminho_resultado = "resultado.txt"

    # Carregar os filmes
    filmes_json = carregar_filmes_json(caminho_json)
    filmes_csv = carregar_filmes_csv(caminho_csv)

    if not filmes_json:
        print("Não foi possível carregar os dados do JSON. Verifique o arquivo.")
        return

    if not filmes_csv:
        print("Não foi possível carregar os dados do CSV. Verifique o arquivo.")
        return

    # Verificar filmes presentes no CSV
    filmes_encontrados = [filme for filme in filmes_json if filme in filmes_csv]

    # Salvar resultados no arquivo TXT
    try:
        with open(caminho_resultado, "w", encoding="utf-8") as arquivo_resultado:
            arquivo_resultado.write("Filmes encontrados no CSV:\n")
            for filme in filmes_encontrados:
                arquivo_resultado.write(f"{filme}\n")
        print(f"Filmes encontrados: {filmes_encontrados}")
        print(f"Processo concluído. Resultados salvos em {caminho_resultado}")
    except IOError as e:
        print(f"Erro ao escrever o arquivo de resultados: {e}")

# Executar o algoritmo
if __name__ == "__main__":
    verificar_filmes_existentes()
