class Calculo:#Criando a class com primeira letra maiúscula
    def __init__(self):#Recebe método construtor com atributos privados com valores declarados
        self.__valor_gasolina = 4.80
        self.__valor_alcool = 3.80
        self.__valor_diesel = 3.90

#método abaixo recebe distancia e consumo como parâmetro e faz verificação
    def calcular_gasto(self, distancia, consumo):
        if (distancia <= 0 or consumo <= 0):
            raise Exception( #Estamos relançando um exceção própria, um erro próprio para ser informado
                'o valor recebido não pode ser menor ou igual a zero')
#Se o if não tiver a condição atendido, o aplicativo segue com os cálculos
        gasto_gasolina = round(#O round arredonda a expressão
            (distancia / consumo) * self.__valor_gasolina, 2)#Realizando os cálculos com os atributos privados da classe
        gasto_alcool = round(
            (distancia / consumo) * self.__valor_alcool, 2)
        gasto_diesel = round(
            (distancia / consumo) * self.__valor_diesel, 2)

        return """
        O valor total gasto será de:

        Gasolina: R$ {}
        Álcool:   R$ {}
        Diesel:   R$ {}
        """.format( #Usando o format para anexar as variáveis que foram calculadas acima.
            gasto_gasolina, gasto_alcool, gasto_diesel
        )