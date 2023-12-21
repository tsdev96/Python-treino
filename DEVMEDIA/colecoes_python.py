#LISTAS, TUPLAS E DICIONÁRIOS

#Listas é uma coleção de valores indexados, em que cada valor é identificado por um índice.

programadores = ['Victor', 'Juliana', 'Samuel', 'Caoi', 'Luana']
print(type(programadores)) # type 'list'
print(len(programadores)) # 5 tamanho da lista
print(programadores[4]) #Buscando o item do índice 4 Luana

#Alterando o item de uma lista
programadores = ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']
print(programadores)

programadores[1] = 'Carolina'
print(programadores)
#Acima alteramos o valor do ítem 1

#Podemos adicionar um item a lista
programadores.append('Renato')
print(programadores) #Renato será adicionado no último índice disponível

#Com insert argumentamos a posição do índice e em seguida o novo ítem
programadores.insert(1, 'Rafael')

print(programadores) #Rafael foi adicionado no índice 1 sem substituir o que já estava lá

programadores.remove('Rafael')#Remove pelo valor do ítem
programadores.pop(2)#Remove pela posição no índice
print(programadores)

#Armazenamos strings, inteiros, flutuantes, booleanos e outros
aluno = ['Murilo', 19, 1.79] # Nome idade e altura

print(type(aluno)) #type 'list'
print(aluno)

#TUPLAS tem a estrutura de dados semelhantes à listas, porém são imutáveis.
times_rj = ('Botafogo', 'Flamengo', 'Fluminense', 'Vasco') 

print(type(times_rj))
print(times_rj)

#Assim como nas litas, podemos acessar determinado valor através de seu índice

print(times_rj[2]) #Fluminense

#Se conter apenas um ítem, devemos colocar vírgula para que não seja apenas uma string
#Úteis para dias da semana, meses, ano e outros que não mudam.

#DICIONÁRIOS representam coleções de dados que contém na sua estrutura um conjunto de pares chave/valor, nos quais cada chave individual tem um valor associado
#Esse objeto representa a ideia de um mapa, que entendemos como uma coleção associativa desordenada. A associação nos dicionários é feita por meio de uma chave que faz referência a um valor.

dados_cliente = {
    'Nome': 'Renan',
    'Endereço': 'Rua Cruzeiro do Sul',
    'Telefone': '9825036345'
}

print(dados_cliente['Nome']) #Renan

#Para adicionar elementos num dicionário basta associar uma nova chave e atribuir um valor a ser associado a ela

dados_cliente['idade'] = 40
print(dados_cliente)
  
#Nos dicionários podemos utilizar o método pop() para remover algo utilizando a chave como identificador
dados_cliente.pop('Telefone', None)
print(dados_cliente)

#A chamada do None seve para que a mensagem keyerror não seja exibida por existir uma chave com valor vazio

#Poderíamos usar o del para remove uma chave com seu valor

del dados_cliente['Telefone']

#FUNÇÕES PARA COLEÇÕES
#min() max()

numeros = [15, 5, 0, 20, 10]
nomes = ['Caio', 'Alex', 'Renata', 'Patrícia', 'Bruno']

print(min(numeros)) #0
print(max(numeros)) #20
print(min(nomes)) #Alex
print(max(nomes)) # Renata
#Temos acima o exemplo das funções buscando o maior e o menor valor de suas listas

#sum() retorna a soma de todos os elementos da coleção.

numeros = [1, 3, 6]

print(sum(numeros)) #10

#Essa função não trabalha com string não sendo possível realizar a soma

#len() retorna o tamanho de um objeto

paises = ['Alemanha', 'Brasil', 'Colômbia', 'Uruguai']

print(len(paises)) #4

#type() retorna o tipo do objeto

professores =['Carla', 'Daniel', 'Ingrid', 'Roberto']
estacoes = ('Primavera', 'Verao', 'Outono', 'Inverno')
cliente = {
    'Nome': 'Fábio Garcia',
    'email': 'fabio_garcia_9@outlook.com'
}

print(type(professores)) #type
print(type(estacoes)) #tuple
print(type(cliente)) # dict


