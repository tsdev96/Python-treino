class Calculadora:
    __area_paredes: float #2 underscore tornamos o atributo privado
    __area_teto: float #TypeHint dá uma dica de que tipo de dado será colocado
    #Com TypeHint não precisamos inicializar a variável

    #Abaixo os métodos da classe Calculadora. Todo método é uma função pertencente a uma classe
    def calcular_area_paredes(self, comodo):#Dentro de comodo temos larg e prof 
#Podemos utilizar os atributos de comodo usando ponto/Atributos de comodo são tratados no property
        self.__area_paredes = 2 * (comodo.largura + comodo.profundidade) * comodo.altura
        return self.__area_paredes
#Em todo método é obrigatório o uso do self que irá chamar os atributos dentro do método.
#self é utilizado apenas internamente dentro da classe. Ele é um referenciador.
    def calcular_area_teto(self, comodo):
        self.__area_teto = comodo.largura * comodo.profundidade
        return self.__area_teto

#Abaixo utilizamos uma validação para evitar erros no que o usuário inseriu
    def calcular_litragem_necessaria(self):#
        if self.__area_paredes <= 0 or self.__area_teto <= 0:
            print(
                'Não é possível calcular a litragem com os valores informados'
            )
            exit()#Ao fazer a validação se atender a condição ele finaliza a aplicação
        return (self.__area_paredes + self.__area_teto) / 10