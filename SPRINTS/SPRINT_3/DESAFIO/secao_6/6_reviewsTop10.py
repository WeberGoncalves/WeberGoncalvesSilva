import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('googleplaystore_sem_duplicatas.csv')

# Converter a coluna 'Reviews' para numérico
df['Reviews'] = pd.to_numeric(df['Reviews'], errors='coerce')

# Remover linhas com valores NaN na coluna 'Reviews'
df = df.dropna(subset=['Reviews'])

# Ordenar os aplicativos pelo número de reviews em ordem decrescente
df_sorted = df.sort_values(by='Reviews', ascending=False)

# Selecionar os top 10 aplicativos
top_10_apps = df_sorted.head(10)

# Exibir o resultado
print("Top 10 aplicativos por número de reviews:")
for i, row in top_10_apps.iterrows():
    print(f"{row['App']} - {int(row['Reviews'])} reviews")