def media_chave(dc,chave):
    if chave not in dc:
        raise ValueError('argumento invalido')
    total = 0
    for i in dc[chave]:
        total += i 
    return total/len(dc[chave])