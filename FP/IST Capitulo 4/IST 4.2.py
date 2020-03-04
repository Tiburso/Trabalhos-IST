def explode(n):
    t = () 
    if isinstance(n,int):
        while n > 0:
            num = n % 10
            t = (num,) + t
            n //= 10
        return t
    else:
        raise ValueError ('Escreva um número inteiro')