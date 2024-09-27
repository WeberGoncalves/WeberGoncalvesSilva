class Lampada:
    def __init__(self, ligada=False):
        self.ligada = ligada

    def liga(self):
        self.ligada = True

    def desliga(self):
        self.ligada = False

    def esta_ligada(self):
        return self.ligada

# Testando a classe Lampada
minha_lampada = Lampada()

# Ligar a lâmpada
minha_lampada.liga()

# Imprimir se a lâmpada está ligada
print("A lâmpada está ligada?", minha_lampada.esta_ligada())

# Desligar a lâmpada
minha_lampada.desliga()

# Imprimir se a lâmpada ainda está ligada
print("A lâmpada ainda está ligada?", minha_lampada.esta_ligada())