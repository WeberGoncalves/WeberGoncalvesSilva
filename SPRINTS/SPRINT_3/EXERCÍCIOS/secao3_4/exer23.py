class Calculo:
    def somar(self, x, y):
        return x + y

    def subtrair(self, x, y):
        return x - y

# Valores para teste
x = 4
y = 5

# Criando uma instância da classe Calculo
calculo = Calculo()

# Realizando as operações de soma e subtração
soma = calculo.somar(x, y)
subtracao = calculo.subtrair(x, y)

# Imprimindo os resultados
print(f"Somando: {x}+{y} = {soma}")
print(f"Subtraindo: {x}-{y} = {subtracao}")