def junta_ordenados(t1,t2):
    i1 = 0 
    i2 = 0
    t3 = ()         
    while (i1 < len(t1) and i2 < len(t2)):
        if t1[i1] < t2[i2]:
            t3 = t3 + (t1[i1],)
            i1 += 1
        elif t1[i1] > t2[i2]:
            t3 = t3 + (t2[i2],)
            i2 += 1
    return t3 + t1[i1:] + t2[i2:]
        