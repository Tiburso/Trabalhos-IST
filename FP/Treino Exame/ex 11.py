def inverte_dic(dc):
    res = {}
    for a in dc:
        for i in dc[a]:
            if i in res:
                res[i] += [a]
            else:
                res[i] = [a]
    return res