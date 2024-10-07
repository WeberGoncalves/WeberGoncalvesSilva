from functools import reduce

def calcula_saldo(lancamentos):
    # Mapeando os lançamentos para valores positivos ou negativos
    valores = map(lambda x: x[0] if x[1] == 'C' else -x[0], lancamentos)
    
    # Reduzindo a lista de valores para calcular o saldo final
    saldo_final = reduce(lambda acc, x: acc + x, valores)
    
    return saldo_final

# Exemplo de uso
lancamentos = [
    (200, 'D'),
    (300, 'C'),
    (100, 'C')
]

print(calcula_saldo(lancamentos))  # Saída: 200