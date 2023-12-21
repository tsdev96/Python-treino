while True: #Vai executar enquanto for verdade. Vai executar para sempre.
    numero = int(input("Informe um número: "))

    if numero == 10: #Se for igual a 10 vai parar a execução do programa.
        break 

    if numero % 2 == 0: 
        continue #Desviar de alguma condição esperada.

    print(numero)


# for numero in range(100):

#     if numero % 2 == 0:
#         continue

#     print(numero, end=" ")
