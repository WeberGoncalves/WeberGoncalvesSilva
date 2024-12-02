animais = ["Cachorro", "Gato", "Elefante", "Girafa", "Leão", "Tigre", "Cavalo", "Vaca", "Baleia", "Golfinho",
           "Coelho", "Panda", "Rinoceronte", "Canguru", "Pinguim", "Urso", "Lobo", "Macaco", "Zebra", "Hipopótamo"]

animais_ordenados = sorted(animais)
[print(animal) for animal in animais_ordenados]

with open('animais.csv', 'w') as file:
    for animal in animais_ordenados:
        file.write(f"{animal}\n")
