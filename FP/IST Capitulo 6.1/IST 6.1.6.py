def inverte(n):
    if str(n) == '':
        return 0 
    else:
        return int(str(n)[0]) + 10*inverte(str(n)[1:])