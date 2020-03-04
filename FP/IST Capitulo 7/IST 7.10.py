def soma_divisores(n):
    def divisores_aux(d,soma):
        if d == n:
            return soma
        elif n % d == 0:
            return divisores_aux(d+1,soma+d)
        else:
            return divisores_aux(d+1,soma)
    return divisores_aux(1,0)

def perfeito(n):
    if soma_divisores(n) == n:
        return True 
    else:
        return False
    
def perfeitos_entre(inf,sup):
    def perfeitos_aux(perfeito_list,num):
        if num > sup:
            return perfeito_list
        elif perfeito(num):
            return perfeitos_aux(perfeito_list+[num],num+1)
        else:
            return perfeitos_aux(perfeito_list,num+1)
    return perfeitos_aux([],inf)