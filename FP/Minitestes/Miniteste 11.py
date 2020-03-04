def junta_ordenados(f1,f2,f3):
    f1 = open(f1,'r')
    f2 = open(f2,'r')
    f3 = open(f3,'w')
    l1 = f1.readline()
    l2 = f2.readline()
    while l1 != '' and l2 != '':
        if l1 < l2:
          f3.write(l1)
          l1 = f1.readline()
        else:
            f3.write(l2)
            l2 = f2.readline()
    f3.write('\n')
    if l1 == '':
        while l2 != '' :
            f3.write(l2)
            l2 = f2.readline()
    else:
        while l1 != '':
            f3.write(l1)
            l1 = f1.readline()
    f1.close()
    f2.close()
    f3.close()
        
    