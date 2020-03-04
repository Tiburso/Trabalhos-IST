def triangular(n):
    aux = 0
    i = 1
    if n == 0:
        return False
    else:
        while aux < n:
            aux += i
            i += 1
    return aux == n

def nesimo_triangular(n):
    #TODO
        