def apenas_numeros_impares_teste(num):
    if num < 0 or not isinstance(num,int):
        raise ValueError('argumento invalido')   
    total = ''
    i = 0
    while i < len(str(num)):
        if int(str(num)[i]) % 2 != 0:
            total += str(num)[i]
        i += 1
    return int(total)

def apenas_numeros_impares(num):
    if num < 0 or not isinstance(num,int):
        raise ValueError('argumento invalido')
    if num == 0:
        return 0
    elif num % 10 % 2 != 0:
        return num % 10 + 10 * apenas_numeros_impares(num // 10) 
    else:
        return apenas_numeros_impares(num // 10)
    
