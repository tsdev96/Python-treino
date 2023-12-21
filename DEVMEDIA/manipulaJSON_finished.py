# 
# Exemplo de como processar dados provenientes de um JSON
#

import urllib.request  
import json #O módulo JSON possui todas as classes para conseguirmos manipular arquivos JSON

def ManipulaJSON():
    endereco = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    webURL = urllib.request.urlopen(endereco)
    if (webURL.getcode() == 200):
        dados = webURL.read() #Carregar os dados da página na variável dados
        oJSON = json.loads(dados) #Criando o dicionário e armazenando o conteúdo do JSON
#Os dados estão em um dicionário que é o conjunto de dados e valores, precissamos dizer na chave meta dada e dentro da chave procuramos a chave count
#Esses dados geralmente ficam no output do JSON
        contagem = oJSON["metadata"]["count"]
        print ("Contagem: " + str(contagem))
#Com contagem estamos navegando nas propriedades dos dados
        for local in oJSON["features"]:
            if local["properties"]["place"] == "190km ENE of Olonkinbyen, Svalbard and Jan Mayen" : #Filtrando para local desejado
                print("****Encontrado registro especial*****")
            else:
                print(local["properties"]["place"])

ManipulaJSON()






