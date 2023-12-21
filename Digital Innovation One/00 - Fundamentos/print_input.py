nome = input("Informe o seu nome: ")
idade = input("Informe a sua idade: ")

print(nome, idade)
print(nome, idade, end="...\n") #/n quebra linha
print(nome, idade, sep="#", end="...\n") #sep é para mudar o separador padrão que é espaço.
print(nome, idade, sep="#")
