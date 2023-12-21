# Desafio
# Paulinho tem em suas mãos um novo problema. Agora a sua professora lhe pediu que construísse um programa para verificar, 
# à partir de dois valores muito grandes A e B, se B corresponde aos últimos dígitos de A.

# Entrada
# A entrada consiste de vários casos de teste. A primeira linha de entrada contém um inteiro N que indica a quantidade 
# de casos de teste. Cada caso de teste consiste de dois valores A e B maiores que zero, cada um deles podendo ter até 
# 1000 dígitos.

# Saída
# Para cada caso de entrada imprima uma mensagem indicando se o segundo valor encaixa no primeiro valor, confome exemplo 
# abaixo.

N = int(input())

while N > 0:
    entrada = input().split(" ") #Dividiu a variável entrada. E depois atribiui o que foi dividido por um espaço usando
    #o índice da varíavel e atribuindo a A e B.

    A = entrada[0]
    B = entrada[1]

    if len(B) > len(A): #Verifica se B tem o mesmo cumprimento de A
        print("nao encaixa")
    elif A.endswith(B): #Verifica se B é sufixo de A. Se sim imprime encaixa.
        print("encaixa")
    else: # Se não imprime não encaixa.
        print("nao encaixa")

    N -= 1 #Itera dimiuindo valor de N até zerar o número de testes de caso.