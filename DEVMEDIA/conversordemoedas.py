real = float(input('Quantos reais você possui disponível para câmbio? R$'))

print('Com R${:.2f} você pode comprar US${:.2f}' .format(real, real/5.51))