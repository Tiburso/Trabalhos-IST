def filtra(lst,fn):
    if lst == []:
        return []
    elif fn(lst[0]):
        return [lst[0]] + filtra(lst[1:],fn)
    else:
        return filtra(lst[1:],fn)
    
def transforma(lst,fn):
    if lst == []:
        return []
    else:
        return [fn(lst[0])] + transforma(lst[1:],fn)

def acumula(lst,fn):
    if lst == []:
        return 0
    else:
        return fn(lst[0],acumula(lst[1:],fn))
    
def soma_quadrados_impares(lst):
    return acumula(transforma(filtra(lst,lambda x: x % 2 != 0),lambda x: x**2),lambda x,y:x + y)