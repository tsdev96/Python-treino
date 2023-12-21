#Funções são blocos de códigos que executam determinada tarefa quantas vezes for preciso.
#Quando criamos uma função, podemos chamá-la quando quiser sem ter que reescrever o código todo novamente.

def hello(meu_nome):
    print('Olá', meu_nome)
#Esta função tem como parâmetro/argumento meu_nome que será passado depois na chamada da função.

#Abaixo chamamos a função

hello('Thiago')

#Também podemos definir funções com vários ou nenhum argumento

def hello(meu_nome, idade):
    print('Olá', meu_nome, '\nSua idade é: ', idade)

hello('Thiago', 25)

def calcular_pagamento(qtd_horas, valor_hora): #Os argumentos são passados em outra variável que a torna float
    horas = float(qtd_horas)
    taxa = float(valor_hora)
    if horas <= 40: #Se horas for menor ou igual a 40 então:
        salario = horas*taxa #Pega salário vezes taxa
    else:
        h_excd = horas - 40 #Se não for maior então tira 40 de horas e guarda em h_excd
        salario = 40*taxa+(h_excd*(1.5*taxa)) #Salário faz 1.5 * taxa vezes h_excd 40 vezes taxa mais h_excd
    return salario #Uma função sempre retorna um valor

str_horas = input('Digite as horas: ') #Os inputs armazenam o dado inserido na variável que é argumentada na chamada da função
str_taxa = input('Digite a taxa: ')
total_salario = calcular_pagamento(str_horas, str_taxa) #O valor retornado da função calcular é guardado em Salario.
print('O valor de seus rendimentos é R$', total_salario)

def calculo_imc(peso, altura):
    peso = float(peso)
    altura = float(altura)
    print(peso / altura ** 2)

str_peso = input('Digite seu peso: ')
str_altura = input('Digite sua altura: ')
calculo_imc(str_peso, str_altura) #Também poderíamos usar a funcionalidade de parâmetros nomeados. calcular_imc(altura = 1.73, peso = 51) Neste exemplo mesmo que troquemos a ordem dos argumentos não teremos problemas.

#Funções Builtin no Python
#max() float() input() int() são funções builtin que não precisam importação

#Já a função de matemática do Python precisa ser importada como abaixo

import math
exponencial = math.exp(3)
print(exponencial)

#Função que verifica se o número é par ou ímpar

def verifica_numero(num):
    if (num%2) == 0:
        print("Este número é par")
    else:
        print("Este número é ímpar")

numero = int(input("Digite um número: "))

verifica_numero(numero)

