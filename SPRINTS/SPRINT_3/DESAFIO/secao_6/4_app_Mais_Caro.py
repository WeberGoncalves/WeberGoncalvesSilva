import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('googleplaystore_sem_duplicatas.csv')

# Filtrar apenas os aplicativos pagos e com preço não nulo
df = df[(df['Type'] == 'Paid') & (df['Price'].notna())]

# Remover o símbolo de dólar e converter a coluna 'Price' para numérico
df['Price'] = df['Price'].str.replace('$', '').astype(float)

# Encontrar o aplicativo mais caro
app_mais_caro = df.loc[df['Price'].idxmax()]

# Exibir o resultado
print(f"O aplicativo mais caro é '{app_mais_caro['App']}'\nda categoria '{app_mais_caro['Category']}' com o preço de ${app_mais_caro['Price']:.2f}.")