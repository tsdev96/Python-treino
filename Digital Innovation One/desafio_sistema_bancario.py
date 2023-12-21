menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0 
limite = 500 #Trata-se de um limite diário.
extrato = "" #String vazia que depois vamos preencher para exibição
numero_saques = 0 #Servirá para contar quantos saques fez, não pode passar de 3.
LIMITE_SAQUES = 3 #Por convenção declarada uma constante para limitar a quantidade de saques.

while True: #Loop infinito porque é um while sempre True.

    opcao = input(menu) #Pega o que o cliente escolheu. Dentro tem a variável menu que possui o informativo das opções.

    if opcao == "d": #Se for igual a d
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0: #Se for maior que 0, para o cliente não colocar número negativo.
            saldo += valor #Soma saldo com o valor depositado.
            extrato += f"Depósito: R$ {valor:.2f}\n" #Adiciona a operação no extrato.

        else: #Se não for maior que 0
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s": # Se for igual a s de saque
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo #Se saque for maior que saldo

        excedeu_limite = valor > limite # Se saque for maior que limite diário de 500

        excedeu_saques = numero_saques >= LIMITE_SAQUES #Se número de saque excedeu a 3

        if excedeu_saldo: #Se excedeu o saldo
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite: #Se excedeu a limite diário
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:  #Se excedeu o limite de 3 saques
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0: #Se valor é maior que 0 no saque
            saldo -= valor #Subtrai saque do saldo.
            extrato += f"Saque: R$ {valor:.2f}\n" #Adiciona operação feita no extrato
            numero_saques += 1 #Desconta a quantidade de saque.

        else: # Se não for maior que 0 o valor do saque
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e": #Se for e de Extrato
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q": # Se digitar q sai do loop.
        break

    else: # Se não for uma das opções dá a mensagem e sai do programa.
        print("Operação inválida, por favor selecione novamente a operação desejada.")
