# DESAFIO
>[!INFO]
>Em preparação foi baixado o arquivo dados_de_vendas.csv no diretório Downloads.
>Foi criado o diretório ecommerce, como evidenciado na imagem abaixo.

![weber](EVIDÊNCIAS/12_a_criado_ecommerce.png)

## Script Processamento de vendas
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