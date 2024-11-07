# Imagem base do Python
FROM python:3.9-slim

# Diretório de trabalho dentro do container
WORKDIR /app
VOLUME ["/app/sprint6"]

# Copiar os arquivos de requisitos e o código para o diretório de trabalho
COPY requirements.txt .
COPY criarBucket.py /app/sprint6/criarBucket.py
COPY series.csv /app/sprint6/series.csv
COPY movies.csv /app/sprint6/movies.csv

# Instala as dependências do Python
RUN pip install -r requirements.txt

# Comando para executar o script Python
CMD ["python", "/app/sprint6/criarBucket.py"]
