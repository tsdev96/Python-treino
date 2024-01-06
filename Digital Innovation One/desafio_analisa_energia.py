C = int(input()) 

def analisa_energia(energia):
    if energia <= 8000:
        return "Inseto!"
    else:
        return "Mais de 8000!"
    

for i in range (C): 
  entrada_energia = int(input())
  resultado = analisa_energia(entrada_energia)
  print(resultado)