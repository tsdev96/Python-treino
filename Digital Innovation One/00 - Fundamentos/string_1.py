nome = "tHIago"

print(nome.upper()) #Faz tudo ficar maiúsculo
print(nome.lower()) #Faz tudo ficar minúsculo
print(nome.title()) #Faz apenas a primeira letra maiúscula e o resto minúsculo.

texto = "  Olá mundo!    "

print(texto + ".")          #Adiciona um ponto no final
print(texto.strip() + ".")  #Retira espaços dos dois lados.
print(texto.rstrip() + ".") #Retira apenas espaço da direita, Right Strip
print(texto.lstrip() + ".") #Retira apenas espaço da esquerda, left strip

menu = "Python"

print("####" + menu + "####") #Maneira muito manual
print(menu.center(14))        #Coloca a string no meio, mas totalizando 14 caracteres
print(menu.center(14, "#"))   #14 caracteres e informamos o que vai ser preenchido.
print("-".join(menu))         #Percorre a variável como se fosse uma lista adicionando o caractere que pedimos. 

#O que fizemos com o join poderia ser feito manualmente ou com um laço (for). Mas não é prático e consome recursos.
