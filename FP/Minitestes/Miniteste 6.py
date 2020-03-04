def conta_pares(lst):
    if lst == []:
        return 0
    elif lst[0] % 2 == 0:
        return 1 + conta_pares(lst[1:])
    else:
        return conta_pares(lst[1:])