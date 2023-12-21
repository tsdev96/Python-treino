#For é usado quando sabemos quantas vezes ele precisa ser executado.
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"


# Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else: #else neste caso pertence ao for. Executa no final do laço.
    print()  # adiciona uma quebra de linha


# Exemplo utilizando a função built-in range
#range(start, stop, step) No exemplo abaixo, dizemos que começa no 0, termina no 51 (exclusivo) e o
#5. Ele vai de 5 em 5.
for numero in range(0, 51, 5):
    print(numero, end=" ")
