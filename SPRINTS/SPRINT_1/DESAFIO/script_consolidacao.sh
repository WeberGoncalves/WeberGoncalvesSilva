#!/bin/bash

# Caminho base dos arquivos de relatório
caminho="/home/weber/vendas/backup/"

# Lista de arquivos de relatório (ajuste conforme necessário)
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

