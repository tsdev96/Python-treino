"""Traz o mês em inglês com base no número que você digitou."""
month = int(input())

months_dict = {'1' : 'January', '2' : 'February', '3' : 'March', '4' : 'April', '5' : 'May', '6' : 'June', '7' : 'July', 
'8' : 'August', '9' : 'September', '10' : 'October', '11' : 'November', '12' : 'December'
}

if month <= 12:
  month = str(month) #Transformo em string 
  print(f"{months_dict[month].title()}" ) #Edito chamadno o dicionário, na chave eu chamo o próprio month
else:                                     # .tittle para buscar o valor do mês.
  print("Digite um número de mês válido por favor.")