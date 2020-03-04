def reconhece(strn):
    if isinstance (strn,str):
        i = 0
        while strn[i] in 'ABCD' and i < len(strn):
            i += 1
        if i == 0 or i == len(strn):
            return False
        while i < len(strn) and strn[i] in '1234' :
            i += 1
        return i == len(strn)
    else:
        raise TypeError('O argumento colocado tem de ser uma string')