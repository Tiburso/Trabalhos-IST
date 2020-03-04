def maior_inteiro(limite):
    def maior_inteiro_aux(soma,n):
        if soma > limite:
            return n-2
        else:
            return maior_inteiro_aux(soma+n,n+1)
    if not isinstance(limite,int) or limite <= 0:
        raise ValueError('argumento invalido')
    else:
        return maior_inteiro_aux(0,0)