def pertence(conjunto,elemento):
    if conjunto == []:
        return False
    elif conjunto[0] == elemento:
        return True
    else:
        return pertence(conjunto[1:],elemento)