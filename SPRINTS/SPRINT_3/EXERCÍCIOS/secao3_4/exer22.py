class Pessoa:
    def __init__(self, identificador):
        self.id = identificador
        self.__nome = None

    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def get_nome(self):
        return self.__nome

    nome = property(get_nome, set_nome)

# Exemplo de uso
pessoa = Pessoa(0)
pessoa.nome = 'Fulano De Tal'
print(pessoa.nome)