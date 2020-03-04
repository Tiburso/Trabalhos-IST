def conta_palavras(cc):
   def salta_espacos(cc, i):
       while i < len(cc) and cc[i] == ' ':
           i += 1
       return i 
   d ={}
   i = salta_espacos(cc, 0)
   while i < len(cc):
       p = '' 
       while i < len(cc) and cc[i] != ' ':
           p += cc[i]
           i += 1
       if not p in d:
           d[p] = 1
       else:
           d[p] += 1
       i = salta_espacos(cc,i)
   return d


        
   
       