import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('googleplaystore_sem_duplicatas.csv')

# Filtrar os aplicativos classificados como 'Mature 17+'
mature_apps = df[df['Content Rating'] == 'Mature 17+']

# Remover linhas duplicadas com base na coluna 'App'
mature_apps = mature_apps.drop_duplicates(subset='App')

# Contar o número de aplicativos 'Mature 17+'
num_mature_apps = mature_apps.shape[0]

# Exibir o resultado
print(f"Há {num_mature_apps} aplicativos classificados como 'Mature 17+'.")