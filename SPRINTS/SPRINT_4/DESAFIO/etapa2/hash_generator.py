import hashlib

# Recebe a string do usuário
input_string = input("Digite a string para gerar o hash: ")

# Gera o hash SHA-1 da string
hash_object = hashlib.sha1(input_string.encode())
hex_dig = hash_object.hexdigest()

# Imprime o hash na tela
print("O hash SHA-1 da string é:", hex_dig)
