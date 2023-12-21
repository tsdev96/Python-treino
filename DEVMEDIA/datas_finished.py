#
# Arquivo com exemplos de manipulação de  datas
#
#Inicialmente importamos classes que já existem para manipular data e hora
from datetime import date
from datetime import time 
from datetime import datetime

def ManipulaDataHora(): #Criando uma função para mostrar como funcionam essas classes
    hoje = date.today() #Buscando a data de hoje
    print ("Hoje é: " , hoje)
    print ("Partes da data: " , hoje.day, hoje.month, hoje.year) #Dividindo partes da data com parâmetros
    print ("Número do dia da semana: " , hoje.weekday()) #Exibir o número do dia da semana
    dias = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"] #Criando array para mostrar abreviação do dia de hoje
    print("Nome abreviado do dia da semana: ", dias[hoje.weekday()]) #Aqui foi usada a função weekday para que ela mesma acione o índice do array e mostre o nome do dia abreviado

    data = datetime.now() #Buscando a data atual
    print ("Data e hora: ", data)

    tempo = datetime.time(data) #Buscando a hora atual usando como parâmetro a variável data
    print ("Hora atual: ", tempo)
ManipulaDataHora()
