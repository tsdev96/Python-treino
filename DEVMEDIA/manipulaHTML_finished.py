# 
# Exemplo de processamento e parse de HTML
#
from html.parser import HTMLParser
#Importando módulo html.parser e buscando a classe htmlparser
class meuParser(HTMLParser): #classe que está herdando os métodos da classe htmlparser
    def handle_starttag (self, tag, attrs): #Substituindo alguns métodos da classe htmlparser
        print("Tag de abertura encontrada!")
        if attrs.__len__() > 0: #Se o objeto attrs contém valores queremos exibir esses valores também
            for a in attrs: #Fazendo um loop para imprimir cada um dos valores do objeto attrs
                print ("  Valores encontrados: ", a[0], " = ", a[1]) #Imprimindo o conteúdo da variável a que é um array

    def handle_endtag(self, tag): #Substituindo o método que manipula a tag de fechamento.
        print("Tag de fechamento encontrada")

    def handle_comment(self, data):
        print ("Comentário encontrado.")

    def handle_data(self, data): #Verifica se valores foram encontrados
        print("Valores encontrados.")
        if data.isspace(): #Verifica se este valor é apenas um espaço
            print("O valor encontrado é um espaço")
        else: #Senão, ele vai imprimir o valor na tela
            print("O valor encontrado é: ", data)

def meuObjeto():
    meuparser1 = meuParser()
    arquivo = open("exemplohtml.html", "r")
    dados = arquivo.read()
    meuparser1.feed(dados) #O feed vai executar os métodos que foram substituídos

meuObjeto()
