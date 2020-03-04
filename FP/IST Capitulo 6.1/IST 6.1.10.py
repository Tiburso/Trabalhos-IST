def maior(lista):
    def search_maior(lista,num):
        if lista == []:
            return num
        elif lista[0] > num:
            return search_maior(lista[1:],lista[0])
        else:
            return search_maior(lista[1:],num)
    return search_maior(lista,lista[0])
    

