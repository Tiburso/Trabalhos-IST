def codifica(num):
    n_f = 0 
    i = 0
    while num > 0:
        if (num % 10) % 2 == 0:
            if num % 10 != 8:
                n_f += (num % 10 + 2)*10**i
        else:
            if num % 10 == 1:
                n_f += 9*10**i
            else:
                n_f += (num%10-2)*10**i
        i += 1
        num //= 10
    return n_f