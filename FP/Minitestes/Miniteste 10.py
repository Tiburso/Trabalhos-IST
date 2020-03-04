def cria_rel(h,m,s):
    if isinstance(h,int) and isinstance(m,int) and isinstance(s,int) and\
    h >= 0 and h < 24 and m >= 0 and m < 60 and s >= 0 and s < 60:
        return 2**h * 3**m * 5**s
    else:
        raise ValueError('argumento invalido')

def horas(r):
    def horas_aux(r,contador):
        if r % 2 != 0:
            return contador
        else:
            return horas_aux(r//2, contador+1)
    return horas_aux(r,0)

def minutos(r):
    def minutos_aux(r,contador):
        if r % 3 != 0:
            return contador
        else:
            return minutos_aux(r//3,contador+1)
    return minutos_aux(r,0)

def segundos(r):
    def segundos_aux(r,contador):
        if r % 5 != 0:
            return contador
        else:
            return segundos_aux(r//5,contador+1)
    return segundos_aux(r,0)

def eh_relogio(arg):
    return isinstance(arg,int) and isinstance(horas(arg),int) \
    and isinstance(minutos(arg),int) and isinstance(segundos(arg),int) and\
    horas(arg) >= 0 and horas(arg) < 24\
    and minutos(arg) >= 0 and minutos(arg) < 60\
    and segundos(arg) >= 0 and segundos(arg) < 60
    
def eh_meia_noite(r):
    return horas(r) == 0 and minutos(r) == 0 and segundos(r)

def eh_meio_dia(r):
    return horas(r) == 12 and minutos(r) == 0 and segundos(r) == 0

def mesmas_horas(r1,r2):
    return r1 == r2

def depois(r1,r2):
    if mesmas_horas(r1,r2):
        return False
    elif horas(r2) > horas(r1):
        return True
    elif horas(r2) == horas(r1):
        if minutos(r2) > minutos(r1):
            return True
        elif minutos(r2) == minutos(r1):
            if segundos(r2) > segundos(r1):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


























