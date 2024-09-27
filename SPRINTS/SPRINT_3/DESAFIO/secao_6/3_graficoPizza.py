import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo CSV
df = pd.read_csv('googleplaystore_sem_duplicatas.csv')

# Contar a frequência de cada categoria
categoria_freq = df['Category'].value_counts()

# Criar uma lista de rótulos numerados
labels = [f'{i+1}' for i in range(len(categoria_freq))]

# Criar o gráfico de pizza
plt.figure(figsize=(10, 8))
wedges, texts, autotexts = plt.pie(categoria_freq, labels=labels, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 10})

# Adicionar legenda
plt.legend(wedges, [f'{i+1}. {label}' for i, label in enumerate(categoria_freq.index)], title="Categorias", loc="center left", bbox_to_anchor=(1, 0, 1, 1))

plt.title('Distribuição de Categorias de Apps no Google Play Store')
plt.axis('equal')  # Assegura que o gráfico de pizza seja um círculo
plt.show()
