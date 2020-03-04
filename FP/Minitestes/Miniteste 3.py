def maior_elemento(t):
    t_f = t[0]
    for i in range(len(t)):
        if t[i] > t_f:
            t_f = t[i]
    return t_f
        