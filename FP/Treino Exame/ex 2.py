def h_m_s(num):
    if isinstance(num,int) and num > 0:
        return (num//3600,num%3600//60,num%3600%60)
    else:
        raise ValueError('argumento invalido')