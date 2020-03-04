def agrupa_por_chave(lst):
    dc = {}
    if not isinstance(lst,list):
        raise ValueError('argumento invalido')
    for i in lst:
        if not isinstance(i[0],str) or not isinstance(i[1],int) or len(i) != 2:
            raise ValueError('argumentos invalidos')
        elif i[0] not in dc:
            dc[i[0]] = [i[1]]
        else:
            dc[i[0]] = dc[i[0]] + [i[1]]
    return dc