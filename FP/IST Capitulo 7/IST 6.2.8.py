def transforma(lst,fn):
    if lst == []:
        return []
    else:
        return [fn(lst[0])] + transforma(lst[1:],fn)

def lista_digitos(n):
    return transforma(list(str(n)), eval)

def produto_digitos(n):
    return lista_digitos