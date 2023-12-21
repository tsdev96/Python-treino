nome = "Guilherme"
idade = 28
profissao = "Progamador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Guilherme", "idade": 28}

print("Nome: %s Idade: %d" % (nome, idade))       #O uso dessa não é mais recomendado. %s é de str e %d é de número. Old style.

print("Nome: {} Idade: {}".format(nome, idade))   #Chamo apenas as variáveis com chave, semelhante ao método anterior.

print("Nome: {1} Idade: {0}".format(idade, nome)) #{} serve para chamar pelo índice. 0 é idade e 1 é nome.
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade)) #Chamando pelo nome da variável. Mais nítido.
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome)) #Mesma ideia do que cima.
print("Nome: {nome} Idade: {idade}".format(**dados)) #Usado um dicionário dados. Puxando tudo o que tinha.

print(f"Nome: {nome} Idade: {idade}") #f string parecido com o .format. É possível nele passar diretamente a variável. Simples.
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}") #f com formação. 2f número de casas para puxar do float.
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.1f}") #passando 10 espaços em branco e usando 1 casa decimal.
