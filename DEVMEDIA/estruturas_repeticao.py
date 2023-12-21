#Loops For e While

#For permite percorrer os tens de uma coleção. While executa um conjunto de instruções várias vezes enquanro uma condição é atendida.

nomes = ['Pedro', 'João', 'Letícia']
for n in nomes:
    print(n)

#A repetição sempre exige que seja criada uma variável para acompanhar o loop.
#No caso do for foi o n que recebeu os valores da lista em nomes.

contador = 0
while contador < 5:
    print(contador)
    contador = contador + 1

#No while inicializamos uma variável que vai acompanhar e no final do bloco de instruções vamos acrescentar um valor para uma hora a condição deixar de ser atendida

