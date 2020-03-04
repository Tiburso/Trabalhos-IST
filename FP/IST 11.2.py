class racional:
    def __init__(self,n,d):
        if isinstance(n,int) and isinstance(d,int) and d != 0:
            self.num = n
            self.den = d
        else:
            raise ValueError('argumentos invalidos')
            
    def numerador(self):
        return self.num
    
    def denominador(self):
        return self.den
    
    def eh_zero(self):
        return self.num == 0
    
    def racionais_iguais(self,outro):
        return self.num*outro.denominador == self.den*outro.numerador
        
    def __add__(self,outro):
        return racional(self.num*outro.denominador+self.den+outro.numerador,\
                        self.den*outro.denominador)
        
    def __repr__(self):
        def mdc(n1,n2):
            if n2 == 0:
                return n1
            else:
                return mdc(n2,n1%n2)
        maxdc = mdc(self.num,self.den)
        return str(self.num//maxdc) +'/' + str(self.den//maxdc)
        
        