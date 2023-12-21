#
# Exemplo de como usar os comando Break e Continue
#

def loopBreak(): #Criando uma função 
    for x in range(5,10): # x para iterar. range(start, stop)
        if x == 7: #Quando chegar o 7, para o for.
            break
        print ("O valor de x é: " , x)

#loopBreak()

def loopContinue():
    for x in range(5,10):
        if x == 7: #Quando for 7 continue, ele pula.
            continue
        print("O valor de x é: ", x)

loopContinue()
