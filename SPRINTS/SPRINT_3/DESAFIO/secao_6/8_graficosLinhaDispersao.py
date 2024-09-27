import pandas as pd
import matplotlib.pyplot as plt

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

# Gráfico de Linhas para os top 10 aplicativos por número de reviews
plt.figure(figsize=(12, 6))
plt.plot(top_10_apps_reviews['App'], top_10_apps_reviews['Reviews'], marker='o')
plt.xticks(rotation=90)
plt.xlabel('Aplicativos')
plt.ylabel('Número de Reviews')
plt.title('Top 10 Aplicativos por Número de Reviews')
plt.grid(True)
plt.show()

# Converter a coluna 'Price' para numérico, removendo o símbolo de dólar
df['Price'] = df['Price'].str.replace('$', '').astype(float, errors='ignore')

# Filtrar apenas os aplicativos pagos e com preço não nulo
df_paid = df[(df['Type'] == 'Paid') & (df['Price'].notna())]

# Gráfico de Dispersão para mostrar a relação entre o preço e o número de reviews dos aplicativos pagos
plt.figure(figsize=(12, 6))
plt.scatter(df_paid['Price'], df_paid['Reviews'], alpha=0.5)
plt.xlabel('Preço ($)')
plt.ylabel('Número de Reviews')
plt.title('Relação entre Preço e Número de Reviews dos Aplicativos Pagos')
plt.grid(True)
plt.show()
