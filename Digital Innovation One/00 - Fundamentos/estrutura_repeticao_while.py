#Faz sentido usar o while quando não sabemos até quando deve ser executado.
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else: #Quando for igual a 0.
    print("Obrigado por usar nosso sistema bancário, até logo!")
