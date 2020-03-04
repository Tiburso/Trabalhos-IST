def soma_quadrados(n):
    if isinstance(n,int) and n >= 1:
        i = 1
        total = 0
        while i <= n:
            quadrado = i**2
            total += quadrado
            i += 1
        return total
    else:
        raise ValueError('O número tem de ser inteiro e positivo')