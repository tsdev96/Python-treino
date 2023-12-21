lista_programadores = ['Thiago', 'Rafaela', 'Aylan']

def imprime_maiusculo(programadores):
    for programador in programadores:
        print(programador.upper())

imprime_maiusculo(lista_programadores)

nome = "Lúcia Cavalcante"
print(nome[6:9]) #Imprimirá Cav. A partir do 6 antes do 9. Espaços contam.

def soma (num_1, num_2):
    return num_1 + num_2

numero_1 = 10
numero_2 = 5

soma_numeros = soma(numero_1, numero_2)

print(soma_numeros)

import math

def calcula_area(raio):
    area = math.pi * raio ** 2
    print(area)

valor = 5.65
calcula_area(valor)

nota_1 = int(input('Digite a 1ª nota: '))
nota_2 = int(input('Digite a 2ª nota: '))
nota_3 = int(input('Digite a 3ª nota: '))

media = (nota_1 + nota_2 + nota_3) / 3

if media >= 7:
    print('Aprovado')
elif media >= 6 and media < 7:
    print('Recuperação')
else:
    print('Reprovado')

def soma(num_1, num_2):
    return num_1 + num_2
numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo número: '))

soma_numeros = soma(numero_1, numero_2)

print(soma_numeros)
        
def calcula_desconto(preco, desconto):
    novo_preco = preco - (preco * desconto)
    return novo_preco

preco = 50
desconto = 0.1

preco_com_desconto = calcula_desconto(preco, desconto)

print("O preço do produto é: ", preco)
print("O preço do produto com desconto é: ", preco_com_desconto)

idade = 17

if idade <= 12:
    print("criança")
elif idade > 12 and idade <= 17:
    print("adolescente")
elif idade >= 18 and idade <= 59:
    print("adulto")
else:
    print("idoso")

temperatura_celsius = int(input('Digite a temperatura em graus Celsius: '))

def celsius_fahrenheit(temp_celsius):
    temp_fahrenheit = (temp_celsius * 9 / 5) + 32
    return temp_fahrenheit

temperatura_fahrenheit = celsius_fahrenheit(temperatura_celsius)

print(temperatura_celsius, "°C equivalem a: ", temperatura_fahrenheit, "Fº")

def imprime_tamanho(texto):
    print(len(texto))

texto = "Eu sou programador Python"

imprime_tamanho(texto)

paises = ['Portugal', 'Brasil', 'Jamaica']

for pais in paises:
    print(pais)