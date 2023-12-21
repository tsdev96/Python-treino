n = int(input('Digite um número: ')) #int obriga converter dados de input para número inteiro
print('O dobro de {} vale {}.'.format(n, (n*2)))
print('O triplo de {} vale {}. \n A raiz quadrada de {} é igual a {:.2f}'.format(n, (n*3), n, pow(n, (1/2)))) #Função power para achar potência. :.2f formata para 2 casas float