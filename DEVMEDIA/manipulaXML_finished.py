# 
# Arquivo com exemplo de tratamento de XML
#

import xml.dom.minidom
#Importando o módulo minidom

def manipulaXML():
    doc = xml.dom.minidom.parse("exemploXML.xml") #Criando um objeto com o conteúdo do XML. Passando para a função parse a localização do arquivo(path)

    print("Nome da primeira tag: ", str(doc.firstChild.tagName))#Buscando a primeira TAG do documento
    primeiroNome = doc.getElementsByTagName("firstname")#Buscando o conteúdo da tag 
    print("O primeiro nome é: ", primeiroNome[0].firstChild.nodeValue) #Comando retorna um array com todas as ocorrências dessa tag. Como temos apenas uma então buscamos a posição 0

    for skill in doc.getElementsByTagName("skill"): #Buscando o conteúdo das tag com skill
        print("Skill encontrado: " , skill.getAttribute("name")) #Buscando pelo atributo name

manipulaXML()