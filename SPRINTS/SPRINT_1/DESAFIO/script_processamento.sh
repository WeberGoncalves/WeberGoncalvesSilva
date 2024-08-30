#criando pasta vendas
mkdir vendas
cp ecommerce/dados_de_vendas.csv vendas/
cd vendas/
mkdir backup/
data_atual=$(date +"%Y%m%d")
cp dados_de_vendas.csv backup/dados-vendas-$data_atual.csv
mv backup/dados-vendas-$data_atual.csv backup-dados-$data_atual.csv
mv backup-dados-$data_atual.csv backup
cd backup
#buscando 1ª e ultima linha e quantidade do arq dados-vendas
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
#cat backup/"$relatorio"