numeros = list(range(10, 13, 1))  # Adiciona os números 1, 3, 5 à lista

for num in numeros:
    if num % 2 == 0:             # modulo % verifica se o resto é zero 
        print(f"Par: {num}")
    else:
        print(f"Ímpar: {num}")