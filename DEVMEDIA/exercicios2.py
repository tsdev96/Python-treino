temperatura_celsius = int(input('Digite a temperatura em graus celsius: '))

def celsius_fahrenheit(temp_celsius):
    temp_fahrenheit = (temp_celsius * 9/5) + 32
    return temp_fahrenheit

temperatura_fahrenheit = celsius_fahrenheit(temperatura_celsius)

print(temperatura_celsius, "ºC equivalem a : ", temperatura_fahrenheit, "ºF")

def retorna_soma(valores):
    soma = 0
    for valor in valores:
        soma = soma + valor
    return soma

numeros = [5, 10, 15, 25]

soma_numeros = retorna_soma(numeros)

print(soma_numeros)