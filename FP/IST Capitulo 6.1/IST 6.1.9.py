def parte(lista,n):
    def maiores(lista,el,n):
        if lista == []:
            return []
        elif lista[0] >= n:
            return [lista[0]] + maiores(lista[1:],el,n)
        else:
            return maiores(lista[1:],el,n)
    def menores(lista,el,n):
        if lista == []:
            return []
        elif lista[0] < n:
            return [lista[0]] + menores(lista[1:],el,n)
        else:
            return menores(lista[1:],el,n)
    if lista == []:
        return []
    else:
        return [menores(lista,lista[0],n),maiores(lista,lista[0],n)]
        
    