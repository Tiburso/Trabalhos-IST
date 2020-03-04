def soma_divisores(n):
    def divisores_aux(d,soma):
        if d == n:
            return soma
        elif n % d == 0:
            return divisores_aux(d+1,soma+d)
        else:
            return divisores_aux(d+1,soma)
    return divisores_aux(1,0)