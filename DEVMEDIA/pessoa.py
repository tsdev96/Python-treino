class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome #Temos os atributos das classes.
        self.idade = idade

#Abaixo usamos o get para receber valor e set para mudar valor. 
#Métodos getters e setters são importante para encapsulamento; Deixando assim as classe protegidas.
#Dessa forma os atributos das classes nunca são alterados ou acessados publicamente e diretamente

    def getNome(self): #Recebemos e mostramos esses valores
        return self.nome

    def setNome(self, nome):#No main é possível utilizar este método para alterar o valor do atributo
        self.nome = nome

    def getIdade(self):
        return self.idade

    def setIdade(self, idade):
        self.idade = idade





        