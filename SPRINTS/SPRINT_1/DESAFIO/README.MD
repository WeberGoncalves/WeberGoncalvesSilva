# DESAFIO
>>**Nesse sprint 01 tive a oportunidade de aprender novos comandos do Linux e GitHub, também me conduziu a pesquisar mais formatações do markdown.**
**Recebi o estímulo para usar uma distribuição do linux, embora eu usei a distruição do Mint um periodo atrás, mas para esse cusrso usei Ubuntu.**  

>**Consegui Configurar a chave SSH no GitHub, que é Protocolo de comunicação de dados com segurança. Avancei nas minhas habilidades do GitHub.**

## Evidências
>[!NOTE]
>**Nessa imagem mostra, quais comandos foram  utilizados para cria o repositorio local e depois fazer a sicronização no github.**
**OBS: as figuras a segui mostram a interface do VS Code**
![weber](EVIDÊNCIAS/1_criado_repositorio.png)

>[!NOTE]
>**Nessa imagem mostra, Adicionando arquivo Commit e mostra o status.**
![weber](EVIDÊNCIAS/2-Adicionando_Commits.png)

>[!NOTE]
>**Adicionando arquivo Commit com mensagem explicando a modificação e o push para sincronizar com repositorio github.**
![weber](EVIDÊNCIAS/3_repositorio_remoto.png)

>[!NOTE]
>**Aqui mostra a primeira etapa da criação da estruturas de pasta SPRINTS.**
![weber](EVIDÊNCIAS/5-criando_estrutura_pastas-sprints.png)

>[!NOTE]
>**Formatação dos nomes das pastas SPRINTS, e a inserção dos links.**
![weber](EVIDÊNCIAS/8-Editando_inserindo_links.png)

>[!NOTE]
>**Edição e Formatação da readme do sprint 01 inserção das figuras.**
![weber](EVIDÊNCIAS/10-B-edição-formatação-readme-sprint01.png)
>* Em preparação foi baixado o arquivo dados_de_vendas.csv no diretório Downloads.
>Foi criado o diretório ecommerce, como evidenciado na imagem abaixo.
![weber](/SPRINTS/SPRINT_1/EVIDÊNCIAS/12_a.png)

* Em sequência foi usado comando CD para entrar na diretório Downloads e foi copiado com CP para  diretório ecommerce,  o TREE foi usado ver o arquivo copiado. 
![weber](/SPRINTS/SPRINT_1/EVIDÊNCIAS/12-b-copiado-dados-ecommerce.png)

### Etapa 1 Desenvovimento Script 1
* Inicia a edição do script do processamento de vendas, foi utilizado NANO para confecção. 
![weber](/SPRINTS/SPRINT_1/EVIDÊNCIAS/12-c-edição-script-processamento.png)

### Etapa 2 Explicação Script 1
* No inicia a edição 
![weber](/SPRINTS/SPRINT_1/EVIDÊNCIAS/13-a-pasta-vendas.png)

### Etapa 2 Explicação Script 1
* No inicia a edição 
![weber](/SPRINTS/SPRINT_1/EVIDÊNCIAS/13-bs.png)

### Etapa 2 Explicação Script 1
* No inicia a edição 
![weber](/SPRINTS/SPRINT_1/EVIDÊNCIAS/13-c.png)

### Etapa 2 Explicação Script 1
* No inicia a edição 
![weber](/SPRINTS/SPRINT_1/EVIDÊNCIAS/13-d.png)

### Etapa 2 Explicação Script 1
* No inicia a edição 
![weber](/SPRINTS/SPRINT_1/EVIDÊNCIAS/13-e.png)

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