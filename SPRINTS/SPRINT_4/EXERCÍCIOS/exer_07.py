#def pares_ate(n:int):
def pares_ate(n: int):
    for i in range(2, n + 1):
        if i % 2 == 0:
            yield i

# Exemplo de uso
for par in pares_ate(10):
    print(par)
