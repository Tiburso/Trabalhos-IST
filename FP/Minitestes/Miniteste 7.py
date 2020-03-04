def conta_p(p,n):
    if n == 1:
        return 0
    elif p(n):
        return 1 + conta_p(p,n-1)
    else:
        return conta_p(p,n-1)
    
    
