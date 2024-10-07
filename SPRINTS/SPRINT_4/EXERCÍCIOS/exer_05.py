import csv

def processar_notas(arquivo_csv):
    with open(arquivo_csv, 'r') as file:
        reader = csv.reader(file)
        estudantes = []

        for linha in reader:
            nome = linha[0]
            notas = list(map(int, linha[1:]))
            maiores_notas = sorted(notas, reverse=True)[:3]
            media_maiores_notas = round(sum(maiores_notas) / 3, 2)
            estudantes.append((nome, maiores_notas, media_maiores_notas))

        # Ordenar os estudantes pelo nome
        estudantes_ordenados = sorted(estudantes, key=lambda x: x[0])

        # Gerar o relatório
        for estudante in estudantes_ordenados:
            nome, maiores_notas, media = estudante
            print(f"Nome: {nome} Notas: {maiores_notas} Média: {media}")

# Exemplo de uso
processar_notas('estudantes.csv')
