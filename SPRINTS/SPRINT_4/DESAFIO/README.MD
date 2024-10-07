
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

**Para Executa o container a partir da imagem criada, utilizei o comando ``docker run --name carguru-container carguru-image``.**
**Evidência da utilização do comando.**

![weber](/SPRINTS/SPRINT_4/EVIDÊNCIAS/Criar_Imagem02.png)