# 
# Arquivo com exemplos para manipulação de dados na Internet
#

import urllib.request #Este módulo contém todas as classes que precisamos para trabalhar com sites

def ConectaInternet():
    objUrl = urllib.request.urlopen("http://www.google.com")

    if objUrl.getcode() == 200: #Verifica o código que é retornado pela página. 200 é o código para conexão com sucesso
        dados = objUrl.read() #Armazenando os dados da página numa variável
        print(dados)

ConectaInternet()


