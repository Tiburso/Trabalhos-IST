def somatorio(l_inf,l_sup,calc_termo,prox):
    soma = 0 
    while l_inf <= l_sup:
        soma += calc_termo(l_inf)
        l_inf = prox(l_inf)
    return soma