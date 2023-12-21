preco = float(input('Qual o preço do produto? '))
desconto = float(input('Qual o desconto pretendido? '))
print('Com desconto de {}% o produto sai por {:.2f} reais/centavos. ' .format(desconto, preco*desconto/100 - preco))