#Estrutura de condição IF

idade = 18
if idade < 20:
    print("Você é jovem")

#Operadores de comparação. Utilizamos no código acima o menor que <

#Temos o igual ==, != diferente, > maior que, < menor que, >= maior ou igual que, <= menor ou igual que

#IF e ELSE

senha = "admin"
if (senha == 'admin'):
    print("Olá Administrador")
elif (senha == "user"):
    print("Olá usuário")
else:
    print("Acesso negado. Verifique sua senha")

#Outro exemplo
idade = int(input('Digite sua idade: '))
if idade >= 10 and idade < 20:
    print('Você é adolescente')
elif idade >= 20 and idade <30:
    print('Você é jovem')
elif idade >= 30 and idade <= 100:
    print('Você é adulto')
else:
    print('Valor não encontrado')

    