larg = float(input('Digite a largura da parede que deseja pintar: '))
alt = float(input('Digite a altura da parede: '))
area = larg * alt
print('A área total da parede é {}m². Tendo em vista que cada litro de tinta rende 2m², você precisará de {} litros de tinta.'.format(area, area/2 ))