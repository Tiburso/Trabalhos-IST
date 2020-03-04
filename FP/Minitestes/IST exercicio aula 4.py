def primo(x):
    if isinstance(x,int) and x > 1:
        from math import sqrt
        i = 2
        while i <= sqrt(x):
            zero = x % i
            if zero == 0:
                return False
            i += 1
        return True
    else:
        raise ValueError('O número escolhido tem de ser inteiro')
       
x = int(input('Escreva um número inteiro superior a um: '))

print(primo(x))