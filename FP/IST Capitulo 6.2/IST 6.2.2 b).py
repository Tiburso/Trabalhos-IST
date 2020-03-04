def piatorio(l_inf,l_sup,calc_termo):
    produto = 1
    while l_inf <= l_sup:
        produto *= calc_termo(l_inf)
        l_inf += 1
    return produto

def fatorial(n):
    return piatorio(1,n,lambda x: x)