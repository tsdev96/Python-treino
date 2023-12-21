#
# Lendo arquivos com funções do Python
#

def leituraArquivo():
    arquivo = open ("NovoArquivo.txt", "r") #Método open para fazer a leitura do arquivo e r para read modo de leitura
    if (arquivo.mode == "r"): #Validando se ele realmente está aberto em modo de leitura
        conteudo = arquivo.read() #Armazenando todo o conteúdo na variável
        print (conteudo)

    arquivo.close()

#leituraArquivo()

def leituraArquivoGrande(): #Se o arquivo for muito grande pode não ser uma boa ideia colocar tudo em uma variável
    arquivo = open ("NovoArquivo.txt", "r")
    if (arquivo.mode == "r"):
        conteudoTotal = arquivo.readlines() #A variável armazena as linha do arquivo

        for conteudo in conteudoTotal: #Para processador linha a linha é utilizado o for
            print (conteudo) 

    arquivo.close()

leituraArquivoGrande()