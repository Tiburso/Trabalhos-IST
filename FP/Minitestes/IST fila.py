import random

class fila:

    def __init__(self, *fila_inicial):
        self.f = list(fila_inicial)

    def inicio (self):
        if self.f == []:
            raise ValueError ('inicio: fila vazia')
        else:
            return self.f[0]

    def comprimento(self):
        return len(self.f)

    def coloca(self, elemento):        
        self.f = self.f + [elemento]
        return self

    def retira (self):
        if self.f == []:
            raise ValueError ('retira: fila vazia')
        else:
            del(self.f[0])
            return self

    def fila_vazia(self):
        return self.f == []

    def filas_iguais(self, outra):
        outra_lista = outra.fila_para_lista()
        if len(self.f) != len(outra_lista):
            return False
        else:
            for i in range(len(self.f)):
                if self.f[i] != outra_lista[i]:
                    return False
        return True

    def __repr__(self):
        if self.f == []:
            return '<<'
        else:
            res = '< '
            for i in range(len(self.f)-1):
                res = res + self.f[i].__repr__() + ', '
            res = res + self.f[-1].__repr__() + ' <'
        return res
    
def soma_aleatorios():
    def soma_aleatorios_create(lst,i):
        if i == 0:
            return lst
        else:
            return soma_aleatorios_create(lst.coloca(random.randint(0,100)),i-1)
    lista = soma_aleatorios_create(fila(),20)
    soma = 0
    while not lista.fila_vazia():
        soma += lista.inicio()
        lista.retira()
    return soma
    
      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
    

