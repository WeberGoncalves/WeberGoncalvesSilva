class Passaro:
    def voar(self):
        print("Passaro Voando...")

    def emitir_som(self):
        print("Passaro emitindo som...")


class Pato(Passaro):
    def emitir_som(self):
        super().emitir_som()
        print("Quack Quack")


class Pardal(Passaro):
    def emitir_som(self):
        super().emitir_som()
        print("Piu Piu")


# Testando as classes
pato = Pato()
pato.voar()
pato.emitir_som()

pardal = Pardal()
pardal.voar()
pardal.emitir_som()