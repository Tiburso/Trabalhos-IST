def junta_ordenados(t1,t2):
    def junta_ordenados_aux(t1,t2,t_f):
        if t1 == ():
            return t_f + t2
        elif t2 == ():
            return t_f + t1
        elif t1[0] < t2[0]:
            return junta_ordenados_aux(t1[1:],t2, t_f+(t1[0],))
        else:
            return junta_ordenados_aux(t1,t2[1:], t_f+(t2[0],))
    return junta_ordenados_aux(t1,t2,())