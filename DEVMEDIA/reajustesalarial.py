salario = float(input('Digite o salário atual: '))
novo = (salario * 15 / 100)
print('Um funcionário(a) que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}. Isso foi um aumento de R${:.2f}'.format(salario, salario + novo, novo))
