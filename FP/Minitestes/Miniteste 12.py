class garrafa:
    def __init__(self,cap):
        if isinstance(cap,float) and cap > 0:
            self.cap = cap
            self.niv = 0
        else:
            raise ValueError('argumentos invalidos')
            
    def capacidade(self):
        return self.cap
    
    def enche(self,valor):
        if self.niv + valor <= self.cap:
            self.niv += valor
        else:
            self.niv = self.cap
        
    def despeja(self,valor):
        if self.niv - valor > 0:
            self.niv -= valor
        else:
            self.niv = 0
        
    def nivel(self):
        return self.niv
        
    