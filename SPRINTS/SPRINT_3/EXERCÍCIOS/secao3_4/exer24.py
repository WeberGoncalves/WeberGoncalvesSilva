class Ordenadora:
    def __init__(self, lista):
        self.listaBaguncada = lista

    def ordenacaoCrescente(self):
        return sorted(self.listaBaguncada)

    def ordenacaoDecrescente(self):
        return sorted(self.listaBaguncada, reverse=True)

# Instanciando objetos com as listas fornecidas
crescente = Ordenadora([3, 4, 2, 1, 5])
decrescente = Ordenadora([9, 7, 6, 8])

# Ordenando as listas
resultado_crescente = crescente.ordenacaoCrescente()
resultado_decrescente = decrescente.ordenacaoDecrescente()

# Imprimindo os resultados das ordenações
print(resultado_crescente)
print(resultado_decrescente)