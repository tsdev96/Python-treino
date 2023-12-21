#
# Arquivo de exemplo para uso da classe timedeltas
#
#Importando as classes que precisamos do módulo datetime

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

def QuantosDiasFaltam(ano, mes, dia): #Função recebendo 3 parâmetros
    hoje = date.today()
    dataProcurada = date(ano, mes, dia)

    qtosDias = dataProcurada - hoje
    #A função replace troca uma formatação e neste caso estamos trocando por uma string vazia
    mensagemRetorno = "Faltam " + str(qtosDias).replace("days, 0:00:00", "") + " dias para a data " + dataProcurada.strftime("%d/%m/%y")

    print(mensagemRetorno)

QuantosDiasFaltam (2019, 10, 29)