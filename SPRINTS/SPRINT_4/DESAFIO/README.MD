
# DESAFIO
### **Esse desafio me ajudou a aplicar os conhecimentos adquiridos no curso de Docker, ao criar uma imagem diferentes dos exemplos do curso, levou a solidificar o aprendizado.**

**Segue a baixo a execução das atividades do desafio.**

## **Etapa 01**
**Nessa fase baixei o arquivo carguru, criei um arquivo de instruções Dockerfile que construiu uma imagem para executar o código carguru.py e depois executou um container a partir dessa imagem..**

### **Arquivo de instruções**
```yaml annotate
# Use uma imagem base do Python
FROM python:3.12
# Defina o diretório de trabalho dentro do container
WORKDIR /etapa1
# Copie o arquivo carguru.py para o diretório de trabalho
COPY carguru.py .
# Execute o script Python quando o container iniciar
CMD ["python", "carguru.py"]
```
**Para Construir a imagem no Docker, foi utilizado o comando ``docker build -t carguru-image .``.**
**Evidência da utilização do comando.**

![weber](/SPRINTS/SPRINT_4/EVIDÊNCIAS/Criar_Imagem01.png)

**Para Executa o container a partir da imagem criada, utilizei o comando ``docker run --rm carguru``.**
**Evidência da utilização do comando.**

![weber](/SPRINTS/SPRINT_4/EVIDÊNCIAS/Criar_Imagem02.png)

## **Etapa 02**
### **É possível reutilizar um container?**
**Sim, é possível reutilizar um container Docker,pois só reiniciar um container que já foi criado e parado, você pode usar o comando ``docker start``.**
**``docker start meu-container``**
**Se tambom foi relazidads, fez alterações no estado do container e deseja criar uma nova imagem a partir dele, você pode usar o comando ``docker commit``.**
**docker commit meu-container nova-imagem:versao, fica assim: ``docker commit meu-container nova-imagem:versao``**

## **Etapa 03**
**Foi necessario criar algoritmo "SHA-1" em python, O principal uso do SHA-1 é verificar se um arquivo foi alterado. Ao calcular o hash de um arquivo e compará-lo com um hash previamente calculado e armazenado, é possível detectar qualquer modificação, mesmo que seja uma única letra.Entretanto, Devido às suas vulnerabilidades, o SHA-1 foi substituído por algoritmos mais seguros.**

### Criado algoritmo SHA-1
```yaml annotate
import hashlib

# Recebe a string do usuário
input_string = input("Digite a string para gerar o hash: ")

# Gera o hash SHA-1 da string
hash_object = hashlib.sha1(input_string.encode())
hex_dig = hash_object.hexdigest()

# Imprime o hash na tela
print("O hash SHA-1 da string é:", hex_dig)
```
**Criado um arquivo chamado Dockerfile no mesmo diretório, foi utilizado o comando para criar a imagem ``docker build -t hash-image .``.**

![weber](/SPRINTS/SPRINT_4/EVIDÊNCIAS/etapa2_hash-1.png)

**Executei o container a partir da imagem criada, permitindo inputs durante a execução, comando utilizado, ``docker run -it --name hash-container hash-image``.**

![weber](/SPRINTS/SPRINT_4/EVIDÊNCIAS/etapa2_hash-2.png)

## **Etapa 04**

