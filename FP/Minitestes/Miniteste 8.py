def troca_vals(lista,de,para):
    if lista == []:
        return []
    elif lista[0] == de:
        return [para] + troca_vals(lista[1:],de,para)
    else:
        return [lista[0]] + troca_vals(lista[1:],de,para)