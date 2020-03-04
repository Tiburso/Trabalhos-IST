'''Comeca aqui o TAD posicao'''

def cria_posicao(x,y):
    '''cria_posicao(x,y) recebe dois valores x e y inteiros positivos
       devolve uma posicao se todos os argumentos forem validos se nao 
       da raise ValueError'''
    if not isinstance(x,int) or not isinstance(y,int)\
    or x< 0 or y< 0:
        raise ValueError('cria_posicao: argumentos invalidos')
    else:
        return (x,y)
    
def cria_copia_posicao(pos):
    '''cria_copia_posicao(pos) recebe uma posicao e devolve uma posicao igual '''
    if eh_posicao(pos):
        return cria_posicao(obter_pos_x(pos),obter_pos_y(pos))

def obter_pos_x(pos):
    '''obter_pos_x(pos) recebe uma posicao e devolve o valor x das coordenadas '''
    return pos[0]

def obter_pos_y(pos):
    '''obter_pos_y(pos) recebe uma posicao e devolve o valor y das coordenadas '''
    return pos[1]

def eh_posicao(arg):
    '''eh_posicao(arg) recebe um argumento qualquer e devolve um booleano
    devolve True se o argumento corresponder a um TAD unidade e False caso 
    contrario '''
    return isinstance(arg,tuple) and len(arg) == 2 and \
    isinstance(arg[0],int) and isinstance(arg[1],int)\
    and arg[0]>= 0 and arg[1]>= 0
    
def posicoes_iguais(pos1,pos2):
    '''posicoes_iguais(pos1,pos2) recebe duas posicoes validas e devolve
    um booleano, True so forem iguais e False caso contrario ''' 
    if eh_posicao(pos1) and eh_posicao(pos2):
        return pos1 == pos2
    else:
        return False
    
def posicao_para_str(pos):
    '''posicao_para_str(pos) recebe uma posicao e devolve uma string da posicao'''
    return str(pos)

def obter_posicoes_adjacentes(pos):
    '''obter_posicoes_adjacentes(pos) recebe uma posicao e devolve um conjunto
    de posicoes adjacentes ''' 
    return tuple(pos for pos in (((pos[0],pos[1]-1),(pos[0]-1,pos[1]),\
                    (pos[0]+1,pos[1]),(pos[0],pos[1]+1))) if eh_posicao(pos))                

'''Comeca aqui o TAD unidade'''

def cria_unidade(pos,v,f,equipa):
    '''cria_unidade(pos,v,f,equipa) recebe quatro argumentos ,
     o primeiro corresponde a posicao que tem de ser valida ,
     o segundo corresponde a forca que tem de ser inteiro e positivo 
     o terceiro corresponde a vida que tem de ser inteiro e positivo 
     e o quarto corresponde a equipa que tem de ser uma string nao vazia 
     se todos os argumentos forem corretos devolve uma unidade se nao 
     da raise ValueError'''
    if not eh_posicao(pos) or v <=0 or f <=0 or not isinstance(v,int) or not isinstance(f,int)\
    or not isinstance(equipa,str) or len(equipa) == 0:
        raise ValueError('cria_unidade: argumentos invalidos')
    else:
        return {'posicao':pos,
                'vida':v ,
                'forca':f,
                'equipa': equipa
                }
    
def cria_copia_unidade(unidade): 
    '''cria_copia_unidade(unidade) recebe uma unidade e devolve
    uma copia da unidade '''
    return cria_unidade(obter_posicao(unidade), obter_vida(unidade), 
            obter_forca(unidade),obter_exercito(unidade))

def obter_posicao(unidade):
    '''obter_posicao(unidade) recebe uma unidade e devolve a sua posicao '''
    return unidade['posicao']

def obter_exercito(unidade):
    '''obter_exercito(unidade) recebe uma unidade e devolve a string
    correspondente a sua  equipa '''
    return unidade['equipa']

def obter_forca(unidade):
    '''obter_forca(unidade) recebe uma unidade e devolve o inteiro
    correspondente a sua forca  '''
    return unidade['forca']

def obter_vida(unidade):
    '''obter_vida(unidade) recebe uma unidade como
    argumento e devolve o inteiro correspondente a sua vida '''
    return unidade['vida']

def muda_posicao(unidade,nova_pos):
    '''muda_posicao(unidade,nova_pos) recebe uma unidade e uma posicao
    e devolve uma unidade com uma nova posicao correspondente
    a posicao introduzida'''
    unidade['posicao'] = nova_pos
    return unidade

def remove_vida(unidade,dano):
    '''remove_vida(unidade,dano) recebe uma unidade e um inteiro correspondente
    ao dano e devolve uma unidade em que se retirou a vida o valor do dano'''
    unidade['vida'] -= dano
    return unidade
    
def eh_unidade(unidade):
    '''eh_unidade(unidade) recebe um argumento qualquer e devolve um booleano,
    True se corresponder a uma unidade valida e False caso contrario'''
    return isinstance(unidade,dict) and len(unidade) == 4\
    and all(tuple(i in ('posicao','vida','forca','equipa') for i in unidade))\
    and eh_posicao(obter_posicao(unidade))\
    and isinstance(obter_vida(unidade),int) and obter_vida(unidade) > 0 \
    and isinstance(obter_forca(unidade),int) and obter_forca(unidade) > 0\
    and isinstance(obter_exercito(unidade),str) and len(obter_exercito(unidade)) > 0
    
def unidades_iguais(u1,u2):
    '''unidades_iguais(u1,u2) recebe duas unidades e devolve True se forem iguais
    ou False caso contrario'''
    if eh_unidade(u1) and eh_unidade(u2):
        return u1 == u2
    else:
        return False
    
def unidade_para_char(unidade):
    '''unidade_para_char(unidade) recebe uma unidade e devolve uma string 
    correspondente a primeira letra do seu exercito em maiuscula'''
    return obter_exercito(unidade).title()[0]

def unidade_para_str(unidade):
    '''unidade_para_str(unidade) recebe uma unidade e devolve uma string 
    correspondente a primeira letra do seu exercito com uma lista 
    que contem a sua vida e a sua forca e por fim a sua posicao num tuplo'''
    return unidade_para_char(unidade) +\
     str([obter_vida(unidade),obter_forca(unidade)]) + '@' + posicao_para_str((obter_posicao(unidade)))

def unidade_ataca(u1,u2):
    '''unidade_ataca(u1,u2) recebe duas unidades, retira a vida do segundo a 
    forca do primeiro e devolve um booleano, True se a 
    segunda tiver vida negativa ou False caso contrario '''
    remove_vida(u2,obter_forca(u1))
    return obter_vida(u2) <= 0
    
def ordenar_unidades(tuplo):
    '''ordenar_unidades(tuplo) recebe um tuplo composto por unidades e devolve
    um tuplo com as unidades ordenadas pela sua posicao'''
    return tuple(sorted(tuplo,key=lambda x: obter_posicao(x)[::-1]))
        
''' Comeca aqui o TAD mapa '''

def cria_mapa(dim,walls,e1,e2):
    '''cria_mapa(dim,walls,e1,e2) recebe quatro argumentos, 
    o primeiro corresponde a um tuplo de 2 inteiros positivos maiores que 3
    o segundo corresponde a um tuplo de posicoes validas que 
    estao dentro dos limites das dimensoes,
    o terceiro e o quarto correspondem a um tuplo de unidades validas nao vazio
    se algumas dos argumentos nao for valido da raise ValueError se nao 
    devolve um mapa
    '''
    if not isinstance(dim,tuple) or not eh_posicao(dim) or dim[0]<3 or dim[1]<3\
    or not isinstance(walls,tuple) or not all(list(eh_posicao(w) for w in walls if len(walls) > 0))\
    or True in tuple((obter_pos_x(w) <= 0 or obter_pos_x(w) > dim[0]) for w in walls)\
    or True in tuple((obter_pos_y(w) <= 0 or obter_pos_y(w) > dim[1]) for w in walls)\
    or not isinstance(e1,tuple) or e1 == () or not all(list(eh_unidade(u1) for u1 in e1))\
    or not isinstance(e2,tuple) or e2 == () or not all(list(eh_unidade(u2) for u2 in e2)):
        raise ValueError('cria_mapa: argumentos invalidos')
    else:
        return {'tamanho':dim,
                'paredes':walls,
                obter_exercito(e1[0]):e1,
                obter_exercito(e2[0]):e2}
                
def cria_copia_mapa(mapa):
    '''cria_copia_mapa(mapa) recebe um mapa devolve uma copia do mapa '''
    return cria_mapa(mapa['tamanho'],mapa['paredes'],\
         tuple(cria_copia_unidade(u) for u in mapa[obter_nome_exercitos(mapa)[0]])\
         ,tuple(cria_copia_unidade(u) for u in mapa[obter_nome_exercitos(mapa)[1]]))

def obter_tamanho(mapa):
    '''obter_tamanho(mapa) recebe um mapa como argumento e devolve um tuplo
    correspondente as suas dimensoes'''
    return mapa['tamanho']

def obter_nome_exercitos(mapa):
    '''obter_nome_exercitos(mapa) recebe um mapa e devolve os nomes dos dois
    exercitos que o constituem ordenados '''
    return tuple(sorted(tuple(exercitos for exercitos in mapa\
                      if exercitos != 'tamanho' and exercitos != 'paredes')))

def obter_unidades_exercito(mapa,nome):
    '''obter_unidades_exercito(mapa,nome) recebe um mapa e uma string
    correspondente a um dos exercitos do mapa e devolve um tuplo com todas 
    as unidades desse exercito'''
    return ordenar_unidades(mapa[nome])
    
def obter_todas_unidades(mapa):
    '''obter_todas_unidades(mapa) recebe um mapa e devolve um tuplo com todas
    as unidades do mapa '''
    def obter_todas_unidades_aux(equipa,total):
        if equipa == ():
            return total
        else:
            return obter_todas_unidades_aux(equipa[1:],total+obter_unidades_exercito(mapa,equipa[0]))
    return ordenar_unidades(obter_todas_unidades_aux(obter_nome_exercitos(mapa),()))                           
        
def obter_unidade(mapa,pos):
    '''obter_unidade(mapa,pos) recebe um mapa e uma posicao e devolve a unidade
    que se encontra na posicao pedida'''
    def obter_unidade_aux(unidades,e):
        if obter_posicao(e) == pos:
            return e
        else:
            return obter_unidade_aux(unidades[1:],unidades[1])
    return obter_unidade_aux(obter_todas_unidades(mapa),obter_todas_unidades(mapa)[0])

def eliminar_unidade(mapa,u):
    '''eliminar_unidade(mapa,u) recebe um mapa e uma unidade e devolve o mapa 
    sem a unidade '''
    def eliminar_unidade_aux(unidades,unidades_f,equipa):
        if unidades[0] == u:
            return unidades_f + unidades[1:]
        else:
            return eliminar_unidade_aux(unidades[1:],unidades_f+(unidades[0],),equipa)
    mapa[obter_exercito(u)] = eliminar_unidade_aux(obter_unidades_exercito\
    (mapa,obter_exercito(u)),(),obter_exercito(u))
    return mapa

def mover_unidade(mapa,u,nova_pos):
    '''mover_unidade(mapa,u,nova_pos) recebe um mapa uma unidade do mapa e uma
    posicao e altera a posicao da unidade pela nova posicao 
    devolve o mapa com a unidade atualizada'''
    def mover_unidade_aux(unidades,unidades_f,equipa):
        if unidades[0] == u:
            return unidades_f + (muda_posicao(unidades[0],nova_pos),)\
            + unidades[1:]
        else:
            return mover_unidade_aux(unidades[1:],unidades_f+(unidades[0],),equipa)
    mapa[obter_exercito(u)] = mover_unidade_aux(obter_unidades_exercito\
    (mapa,obter_exercito(u)),(),obter_exercito(u))
    return mapa
    
def eh_posicao_unidade(mapa,pos):
    '''eh_posicao_unidade(mapa,pos) recebe um mapa e uma posicao e devolve um 
    booleano, True se estiver uma unidade na posicao ou False caso contrario'''
    return True in list(obter_posicao(u) == pos for u in obter_todas_unidades(mapa))
    
def eh_posicao_corredor(mapa,pos):
    '''eh_posicao_corredor(mapa,pos) recebe um mapa e uma posicao e devolve um 
    booleano, True se a posicao for um espaco livre do mapa ou False caso
    contrario'''
    return not (0 in pos or (mapa['tamanho'][0]-1) == obter_pos_x(pos)\
    or (mapa['tamanho'][1]-1) == obter_pos_y(pos) or pos in mapa['paredes'])

def eh_posicao_parede(mapa,pos):
    '''eh_posicao_parede(mapa,pos) que recebe um mapa e uma posicao e devolve um
    booleano, True se a posicao for uma parede ou False caso contrario '''
    return 0 in pos or (mapa['tamanho'][0]-1) == obter_pos_x(pos)\
    or (mapa['tamanho'][1]-1) == obter_pos_y(pos) or pos in mapa['paredes']

def mapas_iguais(mapa1,mapa2):
    '''mapas_iguais(mapa1,mapa2) que recebe dois mapas e devolve um booleano,
    True se forem iguais ou False caso contrario '''
    return mapa1['tamanho'] == mapa2['tamanho'] and mapa1['paredes'] == mapa2['paredes']\
    and obter_nome_exercitos(mapa1) == obter_nome_exercitos(mapa2) and\
    all(tuple(obter_unidades_exercito(mapa1,equipa) == obter_unidades_exercito(mapa2,equipa)\
    for equipa in obter_nome_exercitos(mapa1)))

def mapa_para_str(mapa):
    '''mapa_para_str(mapa) recebe um mapa e devolve uma string que corresponde
    ao desenho do mapa'''
    paredes = mapa['tamanho'][0]*'#'
    interior = ''
    for i in range(1,mapa['tamanho'][1]-1):
        nova_linha = '#' + (mapa['tamanho'][0]-2)*'.' + '#'
        for check_walls in mapa['paredes']:
           if obter_pos_y(check_walls) == i:
               nova_linha = nova_linha[:obter_pos_x(check_walls)] \
               + '#' + nova_linha[obter_pos_x(check_walls)+1:]
        for unidade in obter_todas_unidades(mapa):
            if obter_pos_y(obter_posicao(unidade)) == i:
                nova_linha = nova_linha[:obter_pos_x(obter_posicao(unidade))]\
                + unidade_para_char(unidade) +\
                nova_linha[obter_pos_x(obter_posicao(unidade))+1:]
        interior += nova_linha + '\n'
    return paredes + '\n' + interior + paredes
    
def obter_inimigos_adjacentes(mapa,u):
    '''obter_inimigos_adjacentes(mapa,u) recebe um mapa e uma unidade e devolve
    um tuplo que corresponde a unidades do exercito inimigo 
    devolve vazio se nao houver nenhum inimigo adjacente '''
    for equipa in obter_nome_exercitos(mapa):
        if equipa != obter_exercito(u):
            return ordenar_unidades(tuple(u_inimiga for u_inimiga\
                    in obter_unidades_exercito(mapa,equipa)\
                    if obter_posicao(u_inimiga) in obter_posicoes_adjacentes(obter_posicao(u))))
                   

def obter_movimento(mapa, unit):
    '''
    A funcao obter_movimento devolve a posicao seguinte da unidade argumento
    de acordo com as regras de movimento das unidades no labirinto.

    obter_movimento: mapa x unidade -> posicao
    '''
    ######################
    # Funcoes auxiliares #
    ######################
    def pos_to_tuple(pos):
        return obter_pos_x(pos), obter_pos_y(pos)
    def tuple_to_pos(tup):
        return cria_posicao(tup[0], tup[1])
    def tira_repetidos(tup_posicoes):
        conj_tuplos = set(tuple(map(pos_to_tuple, tup_posicoes)))
        return tuple(map(tuple_to_pos, conj_tuplos))
    def obter_objetivos(source):
        enemy_side = tuple(filter(lambda u: u != obter_exercito(source), obter_nome_exercitos(mapa)))[0]
        target_units = obter_unidades_exercito(mapa, enemy_side)
        tup_com_repetidos = \
            tuple(adj
                  for other_unit in target_units
                  for adj in obter_posicoes_adjacentes(obter_posicao(other_unit))
                  if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj))
        return tira_repetidos(tup_com_repetidos)
    def backtrack(target):
        result = ()
        while target is not None:
            result = (target,) + result
            target, _ = visited[target]
        return result

    ####################
    # Funcao principal #
    ####################
    # Nao mexer se ja esta' adjacente a inimigo
    if obter_inimigos_adjacentes(mapa, unit):
        return obter_posicao(unit)
    visited = {}
    # posicao a explorar, posicao anterior e distancia
    to_explore = [(pos_to_tuple(obter_posicao(unit)), None, 0)]
    # registro do numero de passos minimo ate primeira posicao objetivo
    min_dist = None
    # estrutura que guarda todas as posicoes objetivo a igual minima distancia
    min_dist_targets = []
    targets = tuple(pos_to_tuple(obj) for obj in obter_objetivos(unit))
    while to_explore:  # enquanto nao esteja vazio
        pos, previous, dist = to_explore.pop(0)
        if pos not in visited:  # posicao foi ja explorada?
            visited[pos] = (previous, dist)  # registro no conjunto de exploracao
            if pos in targets:  # se a posicao atual eh uma dos objetivos
                # se eh primeiro objetivo  ou se esta a  distancia minima
                if min_dist is None or dist == min_dist:
                    # acrescentor 'a lista de posicoes minimas
                    min_dist = dist
                    min_dist_targets.append(pos)
            else:  # nao 'e objetivo, acrescento adjacentes
                for adj in obter_posicoes_adjacentes(tuple_to_pos(pos)):
                    if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj):
                        to_explore.append((pos_to_tuple(adj), pos, dist + 1))
        # Parar se estou a visitar posicoes mais distantes que o minimo,
        # ou se ja encontrei todos os objetivos
        if (min_dist is not None and dist > min_dist) or len(min_dist_targets) == len(targets):
            break
    # se encontrei pelo menos uma posicao objetivo, 
    # escolhe a de ordem de leitura menor e devolve o primeiro movimento
    if len(min_dist_targets) > 0:
        # primeiro dos objetivos em ordem de leitura
        tar = sorted(min_dist_targets, key=lambda x: (x[1], x[0]))[0]
        path = backtrack(tar)
        return tuple_to_pos(path[1])
    # Caso nenhuma posicao seja alcancavel
    return obter_posicao(unit)
    
def calcula_pontos(mapa,nome):
    '''calcula_pontos(mapa,nome) recebe um mapa e uma string correspondente 
    a uma das equipas do mapa e devolve 
    um inteiro correspondente ao total de vida da equipa'''
    def calcula_pontos_aux(equipa,total):
        if equipa == ():
            return total
        else:
            return calcula_pontos_aux(equipa[1:],total+obter_vida(equipa[0]))
    return calcula_pontos_aux(obter_unidades_exercito(mapa,nome),0)

def simula_turno(mapa):     
    ''' simula_turno(mapa) recebe um mapa e devolve um mapa apos ter seguido todas 
    as regras de movimento e de ataque ,
    Todas as unidades movem se uma vez por ordem de leitura e se estiverem 
    ao lado de um inimigo atacam-no '''
    for posicao in obter_todas_unidades(mapa):
        if not eh_posicao_unidade(mapa,obter_posicao(posicao)):
            continue
        mover_unidade(mapa,posicao,obter_movimento(mapa,posicao))
        #verifica se ha unidades adjacentes para atacar 
        if obter_inimigos_adjacentes(mapa,posicao) != ():
           if unidade_ataca(posicao,obter_inimigos_adjacentes(mapa,posicao)[0]):
               eliminar_unidade(mapa,obter_inimigos_adjacentes(mapa,posicao)[0])
    return mapa

def simula_batalha(file,State):
    '''simula_batalha(file,State) recebe uma string que corresponde
    a um ficheiro em que a primeira linha e a dimensao do mapa,
    a segunda e terceira linha e a equipa, vida, forca do primeiro e segundo 
    exercito a terceira linha corresponde as paredes do mapa
    e a quarta e quinta linha correspondem as coordenadas das unidades do 
    primeiro e segundo exercito e recebe um State que define a simulacao 
    como modo verboso se True, mostra cada iteracao da batalha,
    o modo silent se False, so mostra a primeira e ultima iteracao da batalha
    '''
    #Abre o ficheiro e le todas as linhas 
    f = open(file,'r')
    dim = eval(f.readline()[:-1])
    nome_v_f_e1 = eval(f.readline()[:-1])
    nome_v_f_e2 = eval(f.readline()[:-1])
    walls = eval(f.readline()[:-1])
    pos_e1 = eval(f.readline()[:-1])
    pos_e2 = eval(f.readline())
    e1 = tuple(cria_unidade(cria_posicao(p[0],p[1]),nome_v_f_e1[1],nome_v_f_e1[2],\
               nome_v_f_e1[0]) for p in pos_e1)
    e2 = tuple(cria_unidade(cria_posicao(p[0],p[1]),nome_v_f_e2[1],nome_v_f_e2[2],\
               nome_v_f_e2[0]) for p in pos_e2)
    mapa = cria_mapa(dim,tuple(cria_posicao(p[0],p[1]) for p in walls),e1,e2)
    #cria as duas partes do scoreboard
    scb1 = '[ '+ obter_nome_exercitos(mapa)[0] +':'
    scb2 = obter_nome_exercitos(mapa)[1] + ':' 
    print(mapa_para_str(mapa) + '\n' + scb1 + str(calcula_pontos(mapa,obter_nome_exercitos(mapa)[0]))\
          + ' ' + scb2 + str(calcula_pontos(mapa,obter_nome_exercitos(mapa)[1])) + ' ]')
    #loop que realiza a simulacao, so para quando uma das equipas perder
    while all(tuple(calcula_pontos(mapa,equipa) > 0 for equipa in obter_nome_exercitos(mapa))):
        copia_mapa = cria_copia_mapa(mapa)
        if State:
            simula_turno(mapa)
            if False in tuple(calcula_pontos(mapa,equipa) > 0 for equipa in obter_nome_exercitos(mapa))\
            or mapas_iguais(mapa,copia_mapa):
                break
            print(mapa_para_str(mapa) + '\n' + scb1 + str(calcula_pontos(mapa,obter_nome_exercitos(mapa)[0]))\
          + ' ' + scb2 + str(calcula_pontos(mapa,obter_nome_exercitos(mapa)[1])) + ' ]')
        else:
            simula_turno(mapa)
            if mapas_iguais(mapa,copia_mapa):
                break
    #devolve o vencedor e da o print da ultima iteracao da simulacao 
    print(mapa_para_str(mapa) + '\n' + scb1 + str(calcula_pontos(mapa,obter_nome_exercitos(mapa)[0]))\
          + ' ' + scb2 + str(calcula_pontos(mapa,obter_nome_exercitos(mapa)[1])) + ' ]')
    if calcula_pontos(mapa,nome_v_f_e2[0]) > 0 and calcula_pontos(mapa,nome_v_f_e1[0]) > 0:
        return 'EMPATE'
    elif calcula_pontos(mapa,obter_nome_exercitos(mapa)[1]) > 0:
        return obter_nome_exercitos(mapa)[1]
    else:
        return obter_nome_exercitos(mapa)[0]
    


    
    
    
    
   
    










































    
    
    