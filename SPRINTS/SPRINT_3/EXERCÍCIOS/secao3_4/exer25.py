class Aviao:
    cor = "Azul"  # Atributo de classe para definir a cor como "Azul" para todas as instâncias

    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade

# Entradas fornecidas
entradas = [
    {"modelo": "BOIENG456", "velocidade_maxima": "1500 km/h", "capacidade": "400 passageiros"},
    {"modelo": "Embraer Praetor 600", "velocidade_maxima": "863 km/h", "capacidade": "14 passageiros"},
    {"modelo": "Antonov An-2", "velocidade_maxima": "258 km/h", "capacidade": "12 passageiros"}
]

# Lista para armazenar as instâncias de Aviao
avioes = []

# Instanciando objetos da classe Aviao com base nas entradas
for entrada in entradas:
    aviao = Aviao(entrada["modelo"], entrada["velocidade_maxima"], entrada["capacidade"])
    avioes.append(aviao)

# Iterando pela lista e imprimindo as informações de cada avião
for aviao in avioes:
    print(f"O avião de modelo {aviao.modelo} possui uma velocidade máxima de {aviao.velocidade_maxima}, capacidade para {aviao.capacidade} e é da cor {Aviao.cor}.")