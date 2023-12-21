#Fatiamento de string. Slicing utilizando o índice.

#Start, Stop e Step
nome = "Guilherme Arthur de Carvalho"

print(nome[0])       #Saída G
print(nome[-2])      #Pega o índice negativo, serve para pegar do fim para o começo
print(nome[:9])      #Start posição 0, porque não foi preenchida. O segundo ele para no caracter 9.
print(nome[10:])     #Começa no 10 e vai até o final.
print(nome[10:16])   #substring, pegando um pedaço da string.
print(nome[10:16:2]) #Passando o step, ele da passo 2, pula 2.
print(nome[:])       #Sem stop e step ele pega tudo.
print(nome[::-1])    #Espelhamento de string. Sem start sem stop e passar o step -1. Cria uma cópia invertida.
