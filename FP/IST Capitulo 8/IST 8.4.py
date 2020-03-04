def resumo_FP(dc):
    passados = 0
    soma = 0
    total = 0
    for i in dc:
        if i < 10:
            passados += len(dc[i])
        else:
            soma += i*len(dc[i])
            total += len(dc[i])
    return (soma/total, passados)
        