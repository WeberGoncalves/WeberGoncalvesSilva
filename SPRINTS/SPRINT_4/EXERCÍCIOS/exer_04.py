def calcular_valor_maximo(operadores, operandos):
    # Função para realizar a operação
    def aplicar_operacao(op, operando1, operando2):
        if op == '+':
            return operando1 + operando2
        elif op == '-':
            return operando1 - operando2
        elif op == '*':
            return operando1 * operando2
        elif op == '/':
            return operando1 / operando2 if operando2 != 0 else float('inf')  # Evitar divisão por zero
        elif op == '%':
            return operando1 % operando2 if operando2 != 0 else float('inf')  # Evitar divisão por zero
        else:
            raise ValueError(f"Operador desconhecido: {op}")

    # Usar zip para combinar operadores e operandos
    resultados = map(lambda x: aplicar_operacao(x[0], x[1][0], x[1][1]), zip(operadores, operandos))
    
    # Retornar o maior valor
    return max(resultados)

# Exemplo de uso
operadores = ['+', '-', '*', '/', '+']
operandos = [(3, 6), (-7, 4.9), (8, -8), (10, 2), (8, 4)]

maior_valor = calcular_valor_maximo(operadores, operandos)
print(maior_valor)  # Saída: 12