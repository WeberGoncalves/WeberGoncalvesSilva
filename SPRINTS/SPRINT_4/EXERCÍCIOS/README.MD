# Exercícios da Sprint 04
### Aqui encontra os exercícios das seções 2,  como evidências que foram lançado no Udemy e foram aprovados, tem as imagens a baixo.
### **Imagem do Udemy**
 ![weber](/SPRINTS/SPRINT_4/EVIDÊNCIAS/exerciciosProntos.png)

## Começa aqui lista dos scripts dos exercícios
## **Exercício 01**
**A chamada da função pessoa100() com a idade fornecida pelo usuário. Exibe uma mensagem informando o ano em que o usuário completará 100 anos.**
```yaml annotate 
# Abrindo o arquivo e lendo os números
with open('number.txt', 'r') as file:
    numeros = list(map(int, file.readlines()))

# Filtrando os números pares
pares = list(filter(lambda x: x % 2 == 0, numeros))

# Ordenando os números pares em ordem decrescente e pegando os 5 maiores
maiores_pares = sorted(pares, reverse=True)[:5]

# Calculando a soma dos 5 maiores números pares
soma_maiores_pares = sum(maiores_pares)

# Exibindo os resultados
print(maiores_pares)
print(soma_maiores_pares)
```