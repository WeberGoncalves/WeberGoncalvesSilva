import pandas as pd
# Carregar o arquivo CSV
df = pd.read_csv('googleplaystore.csv')
linhas_antes = df.shape[0]
# Remover linhas duplicadas
df = df.drop_duplicates()
linhas_depois = df.shape[0]
# Salvar o arquivo CSV sem duplicatas
df.to_csv('googleplaystore_sem_duplicatas.csv', index=False)
print("Linhas duplicadas removidas e arquivo salvo como 'googleplaystore_sem_duplicatas.csv'")
