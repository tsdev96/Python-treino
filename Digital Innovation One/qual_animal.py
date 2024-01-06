# Lê as três palavras
palavra1 = input().strip()
palavra2 = input().strip()
palavra3 = input().strip()

# Mapeia as palavras para os animais correspondentes
animais = {
    ('vertebrado', 'ave', 'carnivoro'): 'aguia',
    ('vertebrado', 'ave', 'onivoro'): 'pomba',
    ('vertebrado', 'mamifero', 'onivoro'): 'homem',
    ('vertebrado', 'mamifero', 'herbivoro'): 'vaca',
    ('invertebrado', 'inseto', 'hematofago'): 'pulga',
    ('invertebrado', 'inseto', 'herbivoro'): 'lagarta',
    ('invertebrado', 'anelideo', 'hematofago'): 'sanguessuga',
    ('invertebrado', 'anelideo', 'onivoro'): 'minhoca'
}

# Imprime o animal correspondente ou 'desconhecido' se não encontrar correspondência
print(animais.get((palavra1, palavra2, palavra3), 'desconhecido'))