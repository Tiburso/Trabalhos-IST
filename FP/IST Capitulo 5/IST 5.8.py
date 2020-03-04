def seq_racaman(n):
    lista = [0]
    for i in range(1,n):
        if lista[i-1] > i and \
           lista[i-1]-i not in lista:
               lista = lista + [lista[i-1]-i]
        else:
            lista = lista + [lista[i-1]+i]
    return lista