def eh_primo(n):
    if n == 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
            return True
        
def filtra(lst,fn):
    if lst == []:
        return []
    elif fn(lst[0]):
        return [lst[0]] + filtra(lst[1:],fn)
    else:
        return filtra(lst[1:],fn)

def nao_primos(n):
    return filtra(lambda x: not eh_primo(x)),list(range(1,n+1))