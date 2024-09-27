import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('googleplaystore_sem_duplicatas.csv')

# Converter a coluna 'Reviews' para numérico
df['Reviews'] = pd.to_numeric(df['Reviews'], errors='coerce')

# Remover linhas com valores NaN na coluna 'Reviews'
df = df.dropna(subset=['Reviews'])

# Ordenar os aplicativos pelo número de reviews em ordem decrescente
df_sorted_reviews = df.sort_values(by='Reviews', ascending=False)

# Selecionar os top 10 aplicativos por número de reviews
top_10_apps_reviews = df_sorted_reviews.head(10)

# Converter a coluna 'Price' para numérico, removendo o símbolo de dólar
df['Price'] = df['Price'].str.replace('$', '').astype(float, errors='ignore')

# Filtrar apenas os aplicativos pagos e com preço não nulo
df_paid = df[(df['Type'] == 'Paid') & (df['Price'].notna())]

# Encontrar o aplicativo mais caro
app_mais_caro = df_paid.loc[df_paid['Price'].idxmax()]

# Exibir os resultados
print("Top 10 aplicativos por número de reviews:")
for i, row in top_10_apps_reviews.iterrows():
    print(f"{row['App']} - {int(row['Reviews'])} reviews")

print(f"\nO aplicativo mais caro é '{app_mais_caro['App']}'\n da categoria '{app_mais_caro['Category']}' com o preço de ${app_mais_caro['Price']:.2f}.")