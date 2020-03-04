def eh_labirinto(maze):
    #Verifica a validade do labirinto 
    if type(maze) is not tuple:
        return False
    if len(maze) == 0 or len(maze) < 3:
        return False
    for check_int in maze:
        if type(check_int) is int:
            return False
    for tuplo_ext in (maze[0],maze[-1]):
        if len(tuplo_ext) != len(maze[0]) or len(tuplo_ext) < 3\
        or type(tuplo_ext) is not tuple:
            return False
        for check in tuplo_ext:
             if check != 1 or not isinstance(check,int):
                return False
    for tuplo_int in (maze[1:len(maze)-1]):
        if len(tuplo_int) != len(maze[0])\
        or tuplo_int.count(0) + tuplo_int.count(1) != len(tuplo_int) or len(tuplo_int) < 3\
        or type(tuplo_int) is not tuple:
            return False
        for check_1 in (tuplo_int[0],tuplo_int[-1]):
            if check_1 != 1 or not isinstance(check_1,int):
                return False
        for check_2 in (tuplo_int[1:len(tuplo_int)-1]):
            if not isinstance(check_2,int):
                return False
    return True

def eh_posicao(pos):
    #confirma se e uma posição valida
    if type(pos) is not tuple:
        return False
    if len(pos) != 2:
        return False
    for i in pos:
        if not isinstance(i,int) or i < 0:
            return False
    return True

def eh_conj_posicoes(conj_p):
    #verifica se e um conjunto de posicoes validas 
    if type(conj_p) is not tuple:
        return False
    if len(conj_p) == 0:
        return True
    for i_ in range(len(conj_p)):
        if eh_posicao(conj_p[i_]) == False:
            return False
        else:
            if conj_p[i_] in conj_p[i_+1:]:
                return False
    return True 

def tamanho_labirinto(maze):
    #conferir o tamanho do labirinto
    if eh_labirinto(maze):
        maze_xy = (len(maze),len(maze[0]))
        return maze_xy 
    else:
        raise ValueError('tamanho_labirinto: argumento invalido')
        
def posicao_no_mapa(maze,pos):
    #verifica se a posicao esta dentro dos limites
    if pos[0] > tamanho_labirinto(maze)[0] or pos[1] > tamanho_labirinto(maze)[1]\
    or maze[pos[0]][pos[1]] == 1:
        return False
    return True
        
def eh_mapa_valido(maze,conj_p):
    #verifica se as coordenadas estao dentro do mapa
    if not eh_labirinto(maze) or not eh_conj_posicoes(conj_p):
        raise ValueError('eh_mapa_valido: algum dos argumentos e invalido')
    for cord in conj_p:
        if not posicao_no_mapa(maze,cord):
            return False
    return True

def eh_posicao_livre(maze,conj_p,pos):
    #confirmar se a posicao esta livre
    if not eh_conj_posicoes(conj_p) or not eh_posicao(pos)\
    or not eh_labirinto(maze) or not eh_mapa_valido(maze,conj_p):
        raise ValueError('eh_posicao_livre: algum dos argumentos e invalido') 
    if pos in conj_p or not posicao_no_mapa(maze,pos):
        return False
    return True

def posicoes_adjacentes(pos):
    #devolve um tuplo correspondente as coordenadas adjacentes da posicao 
    if not eh_posicao(pos):
        raise ValueError('posicoes_adjacentes: argumento invalido')
    pos_adjacentes_t = (((pos[0],pos[1]-1),(pos[0]-1,pos[1]),(pos[0]+1,pos[1]),(pos[0],pos[1]+1)))
    pos_adjacentes_f = ()
    for check_ in pos_adjacentes_t:
        if eh_posicao(check_):
            pos_adjacentes_f += (check_,)
    return pos_adjacentes_f

def mapa_str(maze,conj_p):
    #desenha o mapa  
    if not eh_conj_posicoes(conj_p) or not eh_labirinto(maze)\
    or not eh_mapa_valido(maze,conj_p):
        raise ValueError('mapa_str: algum dos argumentos e invalido')
    parede = tamanho_labirinto(maze)[0]*'#'
    i = 1
    interior = ''
    while i < len(maze[0])-1:#faz as linhas interiores
        str_int = ''
        for linhas_i in maze:
            str_int = str_int + str(linhas_i[i])
        str_int = str_int.replace('1','#')
        str_int = str_int.replace('0','.')
        for check_pos in conj_p:
            if check_pos[1] == i:
                str_int = str_int[:check_pos[0]] + 'O' + str_int[check_pos[0]+1:]
        interior = interior + str_int + '\n'
        i += 1
    return parede + '\n' + interior + parede

def obter_objetivos(maze,conj_p,pos):
    #obtem todos os valores adjacentes das varias coordenadas em relacao a colocada
    if not (pos in conj_p) or not eh_labirinto(maze)\
    or not eh_conj_posicoes(conj_p) or not eh_mapa_valido(maze,conj_p):
        raise ValueError('obter_objetivos: algum dos argumentos e invalido')
    pos_objetivo = ()
    for posicao in conj_p:
        if posicao != pos:
            for check in posicoes_adjacentes(posicao):
                if eh_posicao_livre(maze,pos_objetivo,check)\
                and check != pos and not check in conj_p:
                    pos_objetivo = pos_objetivo + (check,)
    return pos_objetivo

def obter_caminho(maze,conj_p,pos):
    #devolve as posicoes do caminho mais curto para uma das posicoes do conjunto
    if not eh_labirinto(maze) or not eh_conj_posicoes(conj_p)\
    or not (pos in conj_p) or not eh_mapa_valido(maze,conj_p):
        raise ValueError('obter_caminho: algum dos argumentos e invalido')
    visited_nodes = (pos,)
    path = [(pos,)]
    while len(path) != 0:
        for adjacentes in posicoes_adjacentes(path[0][-1]):
            if eh_posicao_livre(maze,visited_nodes,adjacentes):
                possible_path = path[0] + (adjacentes,) 
                visited_nodes = visited_nodes + (adjacentes,)
                path = path + [possible_path]
                if adjacentes in obter_objetivos(maze,conj_p,pos):
                    return possible_path
        del(path[0])
    return tuple(path)

def mover_unidade(maze,conj_p,pos):
    #move a unidade pretendida para a proxima posicao do caminho mais curto ate uma das outras posicoes do conjunto
    if not eh_labirinto(maze) or not eh_conj_posicoes(conj_p)\
     or not eh_mapa_valido(maze,conj_p) or not (pos in conj_p):
        raise ValueError('mover_unidade: algum dos argumentos e invalido')
    for coord in conj_p:
        if pos in posicoes_adjacentes(coord):
            return conj_p
    if len(obter_caminho(maze,conj_p,pos)) == 0:
        return conj_p
    i = 0 
    while conj_p[i] != pos:#encontra o indice da posicao
        i += 1 
    return conj_p[:i] + (obter_caminho(maze,conj_p,pos)[1],) + conj_p[i+1:]