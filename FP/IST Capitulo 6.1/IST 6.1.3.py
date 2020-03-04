def sublistas(lst):
    if len(lst) == 0:
        return 0
    elif isinstance(lst[0],list):
        return 1 + sublistas(lst[0]) + sublistas(lst[1:])
    else:
        return sublistas(lst[1:])
    
def recursive_list_counter(li):
  return 1 + sum(map(recursive_list_counter, li)) if isinstance(li, list) else 0

