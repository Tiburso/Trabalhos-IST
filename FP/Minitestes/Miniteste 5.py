def posicoes_lista(lista,n):
    final = []
    for i in range(len(lista)):
       if lista[i] == n:
           final = final + [i]
    return final