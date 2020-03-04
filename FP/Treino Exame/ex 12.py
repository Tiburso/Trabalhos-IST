def vetor(x,y):
    return (x,y)

def abcissa(v):
    return v[0]

def ordenada(v):
    return v[1]

def eh_vetor(arg):
    return isinstance(arg,tuple) and isinstance(abcissa(arg),int) and\
    isinstance(ordenada(arg),int) and abcissa(arg) >= 0 and ordenada(arg) >= 0
    
def eh_vetor_nulo(v):
    return abcissa(v) == 0 and ordenada(v) == 0

def vetores_iguais(v1,v2):
    return abcissa(v1) == abcissa(v2) and ordenada(v1) == ordenada(v2)

def soma_vetores(v1,v2):
    return vetor(abcissa(v1)+abcissa(v2),ordenada(v1)+ordenada(v2))