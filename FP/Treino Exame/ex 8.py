def junta_ordenados(t1,t2):
    i1 = 0
    i2 = 0
    t_f = ()
    while i1 < len(t1) and i2 < len(t2):
        if t1[i1] < t2[i2]:
            t_f += (t1[i1],)
            i1 += 1
        else:
            t_f += (t2[i2],)
            i2 += 1
    if t1 == ():
        return t_f + t2[i2:]
    else:
        return t_f + t1[i1:]