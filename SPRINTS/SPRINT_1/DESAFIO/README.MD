# DESAFIO da Sprint 01
**Para esse desafio foi necessário criar repositório no Git, sistema de controle de versão, é baseado em repositórios, que contêm todas as versões do código e também as cópias de cada desenvolvedor.**
**Eu usei o VS Code como editor durante o curso de Git, ele possui um terminal integrado, facilitando as nossas ações com o Git, O GitHub gerencias as versões e envia por meio de código  para servidor.**  

**Consegui Configurar a chave SSH no GitHub, que é Protocolo de comunicação de dados com segurança. Avancei nas minhas habilidades do GitHub.**

## As Evidências
>[!NOTE]
**Nessa imagem mostra, quais comandos foram  utilizados para cria o repositorio local e depois fazer a sicronização no github.**
**OBS: as figuras a segui mostram a interface do VS Code**
![weber](/SPRINTS/SPRINT_1/EVIDÊNCIAS/1_criado_repositorio.png)

>[!NOTE]
**Nessa imagem mostra, Adicionando arquivo Commit e mostra o status.**
![weber](/SPRINTS/SPRINT_1/EVIDÊNCIAS/2-Adicionando_Commits.png)

>[!NOTE]
>**Adicionando arquivo Commit com mensagem explicando a modificação e o push para sincronizar com repositorio github.**
![weber](/SPRINTS/SPRINT_1/EVIDÊNCIAS/3_repositorio_remoto.png)

>[!NOTE]
>**Aqui mostra a primeira etapa da criação da estruturas de pasta SPRINTS.**
![weber](/SPRINTS/SPRINT_1/EVIDÊNCIAS/5-criando_estrutura_pastas-sprints.png)

>[!NOTE]
>**Formatação dos nomes das pastas SPRINTS, e a inserção dos links.**
![weber](/SPRINTS/SPRINT_1/EVIDÊNCIAS/8-Editando_inserindo_links.png)

>[!NOTE]
>**Edição e Formatação da readme do sprint 01 inserção das figuras.**
![weber](/SPRINTS/SPRINT_1/EVIDÊNCIAS/10-B-edição-formatação-readme-sprint01.png)

## Começa o desafio
>* Em preparação foi baixado o arquivo dados_de_vendas.csv no diretório Downloads.Foi criado o diretório ecommerce, como evidenciado na imagem abaixo.
![weber](/SPRINTS/SPRINT_1/EVIDÊNCIAS/12_a.png)

* Em sequência foi usado comando CD para entrar na diretório Downloads e foi copiado com CP para  diretório ecommerce,  o TREE foi usado ver o arquivo copiado. 
![weber](/SPRINTS/SPRINT_1/EVIDÊNCIAS/12-b-copiado-dados-ecommerce.png)

### Etapa 1 Desenvovimento Script 1
* Inicia a edição do script do processamento de vendas, foi utilizado NANO para confecção. 
![weber](/SPRINTS/SPRINT_1/EVIDÊNCIAS/12-c-edição-script-processamento.png)

### Etapa 2 Explicação Script 1
* Foi usado "mkdir vendas" Cria um diretório chamado “vendas”. 
Com "cp ecommerce/dados_de_vendas.csv vendas/" Copiou o arquivo 
dados_de_vendas.csv do diretório ecommerce para o diretório vendas,
depois usou CD para entrar no diretorio vendas.
![weber](/SPRINTS/SPRINT_1/EVIDÊNCIAS/13-a.png)

### Etapa 3 criação subdiretório e varial data
* Aqui usando "mkdir backup/", Criou um subdiretório chamado backup dentro de vendas. com este comando "data_atual=$(date +"%Y%m%d")" Armazena a data atual no formato YYYYMMDD na variável data_atual.
cp dados_de_vendas.csv backup/dados-vendas-$data_atual.csv: Copia o arquivo dados_de_vendas.csv para o diretório backup com um nome que inclui a data atual.
![weber](/SPRINTS/SPRINT_1/EVIDÊNCIAS/13-b.png)

### Etapa 4 Extração dsa Datas
* neste trecho "data_so=$(date +"%Y%m%d %HH:%MM")",é feito Armazenamento da data e hora atuais no formato" YYYYMMDD HH:MM" para a variável "data_so".
ja aqui "primeira_data=$(head -n 2 backup-dados-$data_atual.csv |cut -d "," -f 5)" é feita extração da data da primeira venda do arquivo "backup-dados-$data_atual.csv."
"ultima_data=$(tail -n 1 backup-dados-$data_atual.csv |cut -d "," -f 5)" neste trecho é feita extração da data última venda do arquivo.
![weber](/SPRINTS/SPRINT_1/EVIDÊNCIAS/13-c.png)

### Etapa 5 insenrindo dados no relatorio final
* Neste trecho do código que ira concatenar as informações do Arquivo relatorio-data-atual.txt, fara isso por Escreve a data e hora do sistema operacional no relatório,  data da primeira venda,data da última venda, quantidade de itens vendidos.
![weber](/SPRINTS/SPRINT_1/EVIDÊNCIAS/13-d.png)

### Etapa 6 Compactação e arquivos apagados
* Ainda é adiconado  as primeiras 10 linhas do arquivo de backup ao relatório. 
Faz Compacta o arquivo de backup em um arquivo zip.
Remove o arquivo de backup original e Volta para o diretório vendas.
![weber](/SPRINTS/SPRINT_1/EVIDÊNCIAS/13-e.png)

### Etapa 7 agendamento do Script Processamento
* Para esta agendamento foi Necessario programar crontab para quatro dias as 15:27, para processamento_de_vendas.sh
![weber](/SPRINTS/SPRINT_1/EVIDÊNCIAS/12-script-agendamento.png)

### Etapa 8 Execução do Script Processamento no Primeiro Dia
![weber](/SPRINTS/SPRINT_1/EVIDÊNCIAS/12-script-dia1.png)

### Etapa 9 Execução do Script Processamento no Segundo Dia
![weber](/SPRINTS/SPRINT_1/EVIDÊNCIAS/12-script-dia2.png)

### Etapa 10 Execução do Script Processamento no terceiro Dia
![weber](/SPRINTS/SPRINT_1/EVIDÊNCIAS/12-script-dia3.png)

### Etapa 11 Execução do Script Processamento no quarto Dia
![weber](/SPRINTS/SPRINT_1/EVIDÊNCIAS/12-script-dia4.png)



### Notas Explicativas
>[!IMPORTANT]
>* O comando **cut**é utilizado para cortar seções de cada linha de arquivos. Ele é útil para extrair colunas de dados.
>* O comando **head** é usado para exibir as primeiras linhas de um arquivo. Por padrão, ele mostra as primeiras 10 linhas.
>* O comando **tail** exibe as últimas linhas de um arquivo. Por padrão, ele mostra as últimas 10 linhas.
>* O comando **uniq** é usado para remover linhas duplicadas consecutivas em um arquivo. Ele é frequentemente usado em conjunto com o comando sort.
>* Para contar as ocorrências de linhas duplicadas, use a **opção -c**
>* O comando **wc (word count)** é usado para contar linhas, palavras e caracteres em um arquivo.

### Script completo de Processamento_de_dados_de_vendas
```yaml annotate 
#criando diretorio vendas e depois acessando ele
mkdir vendas
cp ecommerce/dados_de_vendas.csv vendas/
cd vendas/
#criando diretorio backup e atribuindo a data do sistema na varial data atual
mkdir backup/
data_atual=$(date +"%Y%m%d")
cp dados_de_vendas.csv backup/dados-vendas-$data_atual.csv
mv backup/dados-vendas-$data_atual.csv backup-dados-$data_atual.csv
mv backup-dados-$data_atual.csv backup
cd backup
#atribuindo a data do sistema na varial data SO
data_so=$(date +"%Y%m%d %HH:%MM")
primeira_data=$(head -n 2 backup-dados-$data_atual.csv |cut -d "," -f 5)
ultima_data=$(tail -n 1 backup-dados-$data_atual.csv |cut -d "," -f 5)
qtd_vendidos=$(cut -d"," -f 2 backup-dados-$data_atual.csv | tail -n +2 | uniq | wc -l)
relatorio="relatorio-$data_atual.txt"

#Criar o arquivo de relatório e escrever os resultado
echo "Data do sistema operacional: "$data_so>>"$relatorio"
echo "Data da primeira venda: "$primeira_data>>"$relatorio"
echo "Data da ultima da venda: "$ultima_data>>"$relatorio"
echo "Quantidade vendida: "$qtd_vendidos>>"$relatorio"

#gerando as 10 primeiras linhas
head -n 10 backup-dados-$data_atual.csv >>"$relatorio"

#compactando arquivos backup e apagando
zip -r backup-dados-$data_atual.zip backup-dados-$data_atual.csv
rm backup-dados-$data_atual.csv
cd .. 
rm dados_de_vendas.csv
#foi usado para testes=> cat backup/"$relatorio"
```

## Consolidador de Processamento de vendas
```yaml annotate
#!/bin/bash

# Caminho base dos arquivos de relatório
caminho="/home/weber/vendas/backup/"

# Lista de arquivos de relatório 
arquivos_relatorios=("$caminho"relatorio-20240826.txt "$caminho"relatorio-20240827.txt "$caminho"relatorio-20240828.txt "$caminho"relatorio-20240829.txt)

# Arquivo de saída
touch "/$caminho"relatorio_final.txt
arquivo_final="$caminho"relatorio_final.txt

# Limpa o arquivo final antes de começar
> "$arquivo_final"
# Itera sobre cada arquivo de relatório e adiciona ao arquivo final
for arquivo in "${arquivos_relatorios[@]}"
do
  cat "$arquivo" >> "$arquivo_final"
done

# Mensagem de conclusão
echo "Relatórios consolidados em" "$arquivo_final"


```