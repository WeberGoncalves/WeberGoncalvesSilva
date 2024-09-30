# DESAFIO
### **Esse desafio me ajudou a introduzi no conhecimento das bibliotecas pandas e matplotlib.pyplot, embora recebi ajuda do monitor e dos colegas das squads, mas foi preciso muitas pesquisas para consegui execultar as atividades do desafio, estou ciente que preciso melhorar mais no uso destas bibliotecas, noentanto gostei muito de usa-las, por isso vou continuar aprofundando no uso do python e com essas e outras bibliotecas.**
**Segue a baixo a execução das atividades do desafio.**

## **Exercício 01**
**O algoritmo carrega um arquivo CSV, remove as linhas duplicadas e salva o resultado em um novo arquivo, garantindo que os dados estejam limpos e sem duplicatas.**
```yaml annotate
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
```
## **Exercício 02**
**Com ajuda das Importações das bibliotecas pandas e matplotlib.pyplot. sendo, a pandas é usada para manipulação e análise de dados, enquanto a matplotlib.pyplot é usada para criar visualizações gráficas. Assim foi possível Carregar o arquivo CSV, Converter a coluna de instalações para numérica, Obter os top 5 apps por número de instalações e por último Criar o gráfico de barras.**
```yaml annotate
import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo CSV
df = pd.read_csv('googleplaystore_sem_duplicatas.csv')

# Converter a coluna de instalações para numérica (remover '+' e ',')
df['Installs'] = df['Installs'].str.replace('+', '').str.replace(',', '')
df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')

# Obter os top 5 apps por número de instalações
top_5_apps = df.nlargest(5, 'Installs')

#print(top_5_apps)

# Criar o gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(top_5_apps['App'], top_5_apps['Installs'], color='skyblue')
plt.xlabel('Apps')
plt.ylabel('Número de Instalações')
plt.title('Top 5 Apps por Número de Instalações')
plt.xticks(rotation=45)
plt.show()
```
## **Exercício 03**
**Este algoritmo é útil para visualizar a distribuição das categorias de aplicativos na Google Play Store, ajudando a identificar quais categorias são mais comuns.**
```yaml annotate
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

```
## **Exercício 04**
**Este algoritmo carrega um arquivo CSV, filtra os aplicativos pagos, limpa e converte os preços, encontra o aplicativo mais caro e exibe essa informação.**
```yaml annotate
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
```
## **Exercício 05**
**Este algoritmo carrega um arquivo CSV, filtra os aplicativos com classificação ‘Mature 17+’, remove duplicatas e conta quantos desses aplicativos existem, exibindo o resultado final.**
```yaml annotate
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
```
## **Exercício 06**
**Neste algoritmo carrega um arquivo CSV, converte a coluna de reviews para numérico, remove linhas inválidas, ordena os aplicativos pelo número de reviews e exibe os 10 aplicativos mais revisados.**
```yaml annotate
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
```
## **Exercício 07**
**Neste algoritmo carrega um arquivo CSV, processa e limpa os dados, ordena os aplicativos pelo número de reviews, seleciona os 10 mais revisados, filtra os aplicativos pagos, encontra o mais caro e exibe essas informações.**
```yaml annotate
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
```
## **Exercício 08**
**Neste algoritmo realizar processos, que são: Carregar o arquivo CSV; Converter a coluna ‘Reviews’ para numérico; Remover linhas com valores NaN na coluna ‘Reviews; Ordenar os aplicativos pelo número de reviews em ordem decrescente; Selecionar os top 10 aplicativos por número de reviews; Gráfico de Linhas para os top 10 aplicativos por número de reviews; Converter a coluna ‘Price’ para numérico, removendo o símbolo de dólar; Filtrar apenas os aplicativos pagos e com preço não nulo; Gráfico de Dispersão para mostrar a relação entre o preço e o número de reviews dos aplicativos pagos.**
```yaml annotate
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

```
