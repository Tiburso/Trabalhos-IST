def implode(t):
    cont = 0
    num = 0 
    for i in t:
        if isinstance(i,int):
           num = num*10**cont + t[i]
           cont += 1
        else:
            raise ValueError('O seu número não é inteiro')
    return num 