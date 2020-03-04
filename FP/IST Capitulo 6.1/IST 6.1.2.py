def junta_ordenadas(lst1,lst2):
    if lst1 == [] and lst2 == []:
        return []
    elif len(lst1) > 0 and lst2 == []:
        return lst1
    elif len(lst2) > 0 and lst1 == []:
        return lst2
    elif lst1 < lst2:
        return [lst1[0]] + junta_ordenadas(lst1[1:],lst2) 
    else:
        return [lst2[0]] + junta_ordenadas(lst1,lst2[1:])
        