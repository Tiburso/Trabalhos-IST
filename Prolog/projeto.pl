:-[codigo_comum].

/*
autor: Manuel Costa n956224

Titulo: Selecionador palavras cruzadas

*/

/* predicado que recebe uma lista de palavras e devolve uma lista organizada com as letras de cada palavra da lista original  */
obtem_letras_palavras(L,LF):- %cria uma nova lista com as palavras organizadas
    sort(L,N_L),
    obtem_letras_palavras(N_L,LF,[]).

obtem_letras_palavras([],LF,LF).

obtem_letras_palavras([P|R],LF,Temp):-
    atom_chars(P,Chars),
    append(Temp,[Chars],N_Temp),
    obtem_letras_palavras(R,LF,N_Temp).

/* predicado que recebe uma lista que representa uma linha ou coluna e devolve os espacos livres */
espaco_fila(Fila,Esp):-
    append([Pref, Esp, Suf],Fila),
    check_pontas(Suf,Pref),
    nao_membro(#,Esp),
    check_tamanho(Esp).

check_pontas([Suf|_],Pref):-  % verificam se as pontas contem # ou sao vazias
    Suf == #,
    last(Pref,NPref),
    NPref == #,
    !.
check_pontas([],Pref):-
    last(Pref,NPref),
    NPref == #,
    !.
check_pontas([Suf|_],[]):-
    Suf == #,
    !.
check_pontas([],[]):- !.

check_tamanho(L):- % verifica se os espacos tem tamanho 3
    length(L,N),
    N >= 3.

nao_membro(_,[]):- !. %verifica se um elemento e membro da lista
nao_membro(N,[P|R]):-
    N \== P,
    nao_membro(N,R).

/* predicado que recebe um Fila e coloca todas as linhas com espacos livres numa lista */
espacos_fila(Fila,[]):- \+ espaco_fila(Fila,_), !.

espacos_fila(Fila,Espacos):-
    bagof(N,espaco_fila(Fila,N),Espacos).

/* predicado que recebe uma grelha de listas e devolve os espacos vazios */
espacos_puzzle(Grelha,Espacos):-
    espacos_puzzle(Grelha,L1,[]),
    mat_transposta(Grelha,G2),
    espacos_puzzle(G2,L2,[]),
    append(L1,L2,Espacos).

espacos_puzzle([],LF,LF):-!.
espacos_puzzle([P|R],Espacos,Temp):-
    espacos_fila(P,Aux),
    append(Temp,Aux,N_Temp),
    espacos_puzzle(R,Espacos,N_Temp).

/* predicado que recebe uma lista de espacos e um espaco e devolve uma lista com variaveis em comum */
espacos_com_posicoes_comuns(Espacos,Es,L):-
    espacos_com_posicoes_comuns(Espacos, Es, L, []),
    !.

espacos_com_posicoes_comuns([], _, Final, Final).
espacos_com_posicoes_comuns([Espaco|R],Es, L, Temp):-
    Espaco \== Es, %verifica se nao sao iguais
    intersecao(Espaco, Es, Aux),
    Aux \== [], %verifica se intersetam
    append(Temp, [Espaco], N_Temp),
    espacos_com_posicoes_comuns(R, Es, L, N_Temp).
espacos_com_posicoes_comuns([_|R], Es, L, Temp):-
    espacos_com_posicoes_comuns(R, Es, L, Temp).

intersecao(L1, L2, Aux):-  %nao vazio se as listas intersetarem
    findall(M1, (member(M1, L1), member(M2, L2), M1 == M2), Aux).


/* predicado que recebe uma lista de letras, um espaco, uma lista de espacos e uma lista de letras e devolve se a palavra e uma palavra possivel para o espaco */
palavra_possivel_esp(Pal, Esp, Espacos, Letras):-
    Esp = Pal,
    espacos_com_posicoes_comuns(Espacos,Esp,Comuns),
    valido(Comuns, Letras).

copia(X,C):-    %copia listas
    maplist(copia_el, X, C).

copia_el(X,_):- var(X), !.
copia_el(X,X).

valido([],_).   %verifica se a palavra adicionada e valida
valido([P|R],Letras):-
    unifica_lst(P,Letras),
    valido(R,Letras),
    !.

unifica_lst(L,[P|_]):-  %verifica se uma lista unifica com um conjunto de listas
    unifica_el(L,P).
unifica_lst(L,[_|R]):-
    unifica_lst(L, R).

unifica_el(P1,P2):- %verifica se o elemento unifica com outro
    copia(P1,Copia),
    Copia = P2.

/* predicado que recebe um conjunto de letras, um conjunto de espacos e um espaco desse conjunto
e devolve as palavras validas para esse espaco */
palavras_possiveis_esp(Letras, Espacos, Esp, Possiveis):-
    findall(Pal,(member(Pal,Letras),palavra_possivel_esp(Pal, Esp, Espacos, Letras)), Possiveis).


/* predicado que recebe uma lista de letras e uma lista de espacos e devolve as palavras possiveis
para cada espaco */
palavras_possiveis(Letras, Espacos, Possiveis):-
    palavras_possiveis(Letras, Espacos, Espacos, Possiveis, []).

palavras_possiveis(_, _,[], LF, LF):-!.
palavras_possiveis(Letras, Espacos, [Esp|R], Possiveis, Temp):-
    palavras_possiveis_esp(Letras, Espacos, Esp, Poss),
    append([Esp],[Poss], Aux),
    append(Temp,[Aux], Res),
    palavras_possiveis(Letras, Espacos, R, Possiveis, Res).

/* predicado que recebe uma lista de palavras e devolve as letras em comum */
letras_comuns(Palavras, Comuns):-
    nth1(1,Palavras,Pal),
    subtract(Palavras, [Pal], LF), %divide a lista na primeira palavra e nas restantes
    letras_comuns(LF, Comuns, Pal, 0, []),
    !.

letras_comuns( _, Comuns, Pal, N, Comuns):- length(Pal,N).
letras_comuns(Palavras, Comuns, Pal, N, Aux):-
    nth0(N, Pal, Letter),
    maplist(letras_comuns_aux(N, Letter), Palavras), %ve a letra e igual em todas as palavras
    N1 is N+1, %indice do elemento
    append(Aux,[(N1,Letter)], Temp),
    letras_comuns(Palavras, Comuns, Pal, N1, Temp).
letras_comuns(Palavras, Comuns, Pal, N, Aux):-
    N1 is N+1,
    letras_comuns(Palavras, Comuns, Pal, N1, Aux).

letras_comuns_aux(N,Letter,L):- %auxiliar que verifica se as letras sao iguais em todas as palavras
    nth0(N, L, X),
    X == Letter.

/* predicado que recebe uma lista de palavras possiveis e atualiza a lista com as letras comuns */
atribui_comuns([]).
atribui_comuns([P|R]):-
    nth1(1,P,Espaco),
    nth1(2,P,Possiveis),
    letras_comuns(Possiveis, Comuns),
    maplist(atribui_comuns_aux(Espaco), Comuns),
    atribui_comuns(R).

atribui_comuns_aux(Espaco,Comum):- %auxiliar que unifica os espacos com as letras
    Comum = (I, Letra),
    nth1(I, Espaco, Pos),
    Pos = Letra.

/* predicado que recebe uma lista de palavras possiveis e devolve uma nova lista de palavras possiveis
sem as impossiveis */
retira_impossiveis(Pals_Possiveis, N_Pals_Possiveis):-
    maplist(retira_impossiveis_aux,Pals_Possiveis, N_Pals_Possiveis).

retira_impossiveis_aux(Possiveis, Final):- %verifica se as palavras sao possiveis e cria uma lista nova com elas
    Possiveis = [Espaco, Palavras],
    findall(X, (member(X, Palavras), unifica_el(Espaco, X)), Pal_F),
    Final = [Espaco, Pal_F].

/* predicado que recebe uma lista de palavras possiveis e devolve uma lista com as palavras unicas */
obtem_unicas(Possiveis, Unicas):-
    obtem_unicas(Possiveis, Unicas, []).

obtem_unicas([],LF, LF).
obtem_unicas([Espaco|R],Unicas,Temp):-
    nth1(2, Espaco, Palavra),
    length(Palavra, 1),
    append(Temp, Palavra, N_Temp),
    obtem_unicas(R,Unicas,N_Temp).
obtem_unicas([Espaco|R],Unicas, Temp):-
    nth1(2, Espaco, Palavras),
    length(Palavras, N),
    N \== 1,
    obtem_unicas(R, Unicas, Temp).


/* predicado que recebe uma lista de palavras possiveis e devove uma nova lista de palavras possiveis
sem as palavras unicas */
retira_unicas(Possiveis, N_Possiveis):-
    obtem_unicas(Possiveis, Unicas),
    maplist(retira_unicas_aux(Unicas),Possiveis,N_Possiveis),
    !.

retira_unicas_aux(_, Possivel, Possivel):-
    nth1(2, Possivel, Palavras),
    length(Palavras, 1).
retira_unicas_aux(Unicas, Possivel, N_Possivel):-
    Possivel = [Espaco, Palavras],
    findall(Pal,(member(Pal,Palavras), nao_membro(Pal, Unicas)), Pal_F),
    N_Possivel = [Espaco, Pal_F].

/* predicado que recebe uma lista de palavras possiveis e devolve a mesma lista simplificada */
simplifica(Possiveis, N_Possiveis):-
    copia_puzzle(Possiveis, Copia_Possiveis), %copia o inicial
    atribui_comuns(Possiveis),
    retira_impossiveis(Possiveis, Aux),
    retira_unicas(Aux, Novo),
    Novo \= Copia_Possiveis, %ve se houve uma alteracao no inicial
    !,
    simplifica(Novo, N_Possiveis).

simplifica(Possiveis, N_Possiveis):- %nao ha alteracao devolve a lista
    atribui_comuns(Possiveis),
    retira_impossiveis(Possiveis, Aux),
    retira_unicas(Aux, N_Possiveis).

copia_puzzle(Inicio, Copia):-
    copia_puzzle(Inicio, Copia, []). %cria uma copia do tabuleiro no momento
copia_puzzle([],Copia, Copia).
copia_puzzle([P|R],Final, Temp):-
    P = [Espacos,Palavras],
    copia(Espacos, N_Espacos),
    append(Temp,[[N_Espacos,Palavras]],N_Temp),
    copia_puzzle(R,Final,N_Temp).

/* predicado que recebe um puzzle e devolve uma lista possivel de palavras simplificada */
inicializa(Puzzle, Possiveis):-
    Puzzle = [Palavras, Grelha],
    obtem_letras_palavras(Palavras, L_Letras),
    espacos_puzzle(Grelha, L_Espacos),
    palavras_possiveis(L_Letras, L_Espacos, Pal_Possiveis),
    simplifica(Pal_Possiveis, Possiveis).

/* predicado que recebe uma lista simplificada e devolve o primeiro espaco com menos palavras */
escolhe_menos_alternativas([P|R], Escolha):-
    P = [_, Palavras],
    length(Palavras, 1),
    escolhe_menos_alternativas(R, Escolha),
    !.
%continua em loop ate encontrar uma lista de tamanho maior que 1
escolhe_menos_alternativas([P|R], Escolha):-
    P = [_, Palavras],
    \+ length(Palavras, 1),
    escolhe_menos_alternativas(R, Escolha, P).

/* se houver maior que 1 adiciona a uma lista e vai comparando ficando
sempre com o mais pequeno */
escolhe_menos_alternativas([], Escolha, Escolha):-
    Escolha = [_, Palavras],
    \+ length(Palavras, 1).
escolhe_menos_alternativas([Poss|R], Escolha, Temp):-
    Poss = [_, Palavras_Poss],
    Temp = [_, Palavras_Atuais],
    length(Palavras_Poss, N),
    length(Palavras_Atuais, T),
    N < T,
    escolhe_menos_alternativas(R, Escolha, Poss).
escolhe_menos_alternativas([_|R], Escolha, Temp):-
    escolhe_menos_alternativas(R, Escolha, Temp).


/* predicado que recebe uma lista com as palavras possiveis para um espaco e uma lista de espacos possiveis
e devolve varias as terntativas de resolver o puzzle */
experimenta_pal(Escolha, Possiveis, N_Possiveis):-
    Escolha = [Esp, Lst_Pals],
    member(Pal, Lst_Pals),
    Esp = Pal,
    maplist(lista_unica(Escolha,Pal), Possiveis, N_Possiveis). %procura o espaco nos possiveis e retira os restantes

lista_unica(Escolha,_,Possivel, Possivel):- Escolha \== Possivel.
lista_unica(Escolha, Pal, Possivel, N_Possivel):- %auxiliar que retira os restantes a lista se o espaco for igual a escolha
    Escolha == Possivel,
    Possivel = [Espaco, Palavras],
    include(=(Pal), Palavras, N_Palavras),
    N_Possivel = [Espaco, N_Palavras].


/* predicado que recebe uma lista de palavras possiveis e devolve o puzzle resolvido */
resolve_aux(Puz, Resolvido):-
    escolhe_menos_alternativas(Puz, Escolha),
    experimenta_pal(Escolha, Puz, Possibilidade),
    simplifica(Possibilidade, Poss_Resolvido),
    resolve_aux(Poss_Resolvido, Resolvido),
    !.
resolve_aux(Puz, Puz):-  %se nao houver mais opcoes devolve o puzzle resolvido
   \+ escolhe_menos_alternativas(Puz, _).

/* predicado que recebe um puzzle e devolve a solucao */

