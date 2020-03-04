from random import random

def euromilhoes():
    def insere_ordenado(lista,n):
        if n < lista[0]:
            return [n] + lista[0]
        else:
    numeros = []
    estrelas = []
    while len(numeros) != 5:
        num = round(random()*100)+1
        if not(num > 50 or num in numeros):
            numeros += [num]
    while len(estrelas) != 2:
        num = round(random()*100)+1
        if not(num > 12 or num in estrelas):
            estrelas += [num]
    return [numeros,estrelas]
        