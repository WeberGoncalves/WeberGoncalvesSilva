palavras = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']


def e_palindromo(palavra):
    return palavra == palavra[::-1]


for palavra in palavras:
    if e_palindromo(palavra):
        print(f"A palavra: {palavra} é um palíndromo")
    else:
        print(f"A palavra: {palavra} não é um palíndromo")
