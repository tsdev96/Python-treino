lista = ["p", "y", "t", "h", "o", "n"]
#         0    1    2    3    4    5    
print(lista[2:])  # start 2["t", "h", "o", "n"]
print(lista[:2])  # stop em 2 ["p", "y"]
print(lista[1:3])  # start e stop ["y", "t"]
print(lista[0:3:2])  # start 0, stop em 3 e step em 2, vai de 2 em 2["p", "t"]
print(lista[::])  #Vazio, sem start sem stop. Vai normal. ["p", "y", "t", "h", "o", "n"]
print(lista[::-1])  #Sem start sem stop, mas o step vai negativo. Então espelha. ["n", "o", "h", "t", "y", "p"]
