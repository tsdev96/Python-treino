T = int(input())

def calcular_garrafas_segundo_dia(compradas, vazias):
    trocadas_cheias = compradas // vazias #7 / 4 = 1
    restantes_vazias = compradas % vazias #7 % 4 = 3
    total_cheias = trocadas_cheias + restantes_vazias #trocadas_cheias 1 + restantes vazias 3
    
    return total_cheias #retorna 4

for _ in range(T):
    n, k = map(int, input().split()) #Ex 7 compradas, 4 para trocar por 1. map, serve para transformar em inteiro.
    resultado = calcular_garrafas_segundo_dia(n, k)
    print(resultado)