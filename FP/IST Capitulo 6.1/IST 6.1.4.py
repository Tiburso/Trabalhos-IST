def soma_n_vezes(x,y,n):
    def soma_auxiliar(n):
        if n == 0:
            return x
        else:
            return y + soma_auxiliar(n-1)
    if n < 0 or not isinstance(x,int) or not isinstance(y,int):
        raise ValueError('argumentos invalidos')
    else:
        return soma_auxiliar(n)
    