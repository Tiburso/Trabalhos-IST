import random

def euromilhoes():
    def gera(n,maximo):
        def insere(m,lst):
            i = 0
            while i < len(lst) and lst[i] < c:
                i +=1
            return lst[:i] + [c] + lst[i:]
        res = []
        i = 0 
        while i < n:
            c = int(random.random()*maximo + 1)
            if c not in res:
                res = insere(c,res)
                i += 1
                