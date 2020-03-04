def soma_fn(n,fn):
    soma = 0 
    for x in range(n+1):
        soma += fn(x)
    return soma

def soma_fn_(n,fn):
    if n == 1:
        return fn(n)
    else:
        return fn(n) + soma_fn_(n-1,fn)