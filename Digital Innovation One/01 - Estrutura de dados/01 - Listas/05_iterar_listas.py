carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)


for indice, carro in enumerate(carros): #Enumerate para mostrar o índice.
    print(f"{indice}: {carro}")
