tamanho([P|_],P):-
    length(P,N),
    N >= 3.

tamanho([_|R],L):-
    tamanho(R,L).

add_list(Inicial,Final):-
    add_list(Inicial,Final,[],[]).

add_list([],Final,Final,[]).

add_list([P],Final,Temp,Aux):-
    P \== #,
    append(Aux,[P],Aux1),
    append(Temp,[Aux1],N_Temp),
    add_list([],Final,N_Temp,[]).
add_list([P|R],Final,Temp,Aux):-
    P == #,
    append(Temp,[Aux],N_Temp),
    add_list(R,Final,N_Temp,[]).

add_list([P|R],Final,Aux,Temp):-
    P \== #,
    append(Temp,[P],N_Temp),
    add_list(R,Final,Aux,N_Temp).


espaco_fila(Fila,Esp):-
    append([Pref, Esp, Suf],Fila),
    check_pontas(Suf,Pref),
    nao_membro(#,Esp),
    check_tamanho(Esp).

check_pontas([P|_],Pref):-
    P == #,
    last(Pref,NPref),
    NPref == #,
    !.
check_pontas([],Pref):-
    last(Pref,NPref),
    NPref == #,
    !.
check_pontas([P|_],[]):-
    P == #,
    !.

check_tamanho(L):-
    length(L,N),
    N >= 3.

nao_membro(_,[]):- !.
nao_membro(N,[P|R]):-
    N \== P,
    nao_membro(N,R).

/* Funcao para ver que elementos sao iguais entre duas palavras */
respeita(P1,P2):-
    copia(P1,Copia),
    Copia = P2.

copia(Esp,Copia):-
    maplist(copia_el, Esp, Copia).

copia_el(El,_):- var(El), !.
copia_el(El,El).


/* seleciona as listas com tamanho maior que 3 */
espaco_fila([],Espaco,[Espaco|_],[]):-
    length(Espaco,N),
    N >= 3.
espaco_fila([],Espaco,[_|R],[]):-
    espaco_fila([],Espaco,R,[]).

/* cria uma lista com todas os intervalos de espaco */
espaco_fila([P],L,LF,Temp):- %verifica se o ultimo elemento e um # senao chega ao fim da lista
    P \== #,
    append(Temp,[P],Aux),
    append(LF,[Aux],N_Temp),
    espaco_fila([],L,N_Temp,[]).

espaco_fila([P|R],L,LF,Temp):-
    P == #,
    append(LF,[Temp],N_Temp),
    espaco_fila(R,L,N_Temp,[]).

espaco_fila([P|R],L,LF,Temp):- %cria a lista temporaria
    P \== #,
    append(Temp,[P],N_Temp),
    espaco_fila(R,L,LF,N_Temp).



lista_listas(Lista,A):-
    lista_listas(Lista,A,[]).

lista_listas([],A,A):-!.
lista_listas([P|R],A,Temp):-
    append(Temp,[P],Aux),
    lista_listas(R,A,Aux).


espacos_com_posicoes_comuns(Espacos,Es,L_Es):-
    espacos_com_posicoes_comuns(Espacos,Es,L_Es,[]).

espacos_com_posicoes_comuns([],_,LF,LF):-!.
espacos_com_posicoes_comuns([P|R],Es,L_Es,Temp):-
    intersection(Es,P,Aux),
    (Aux \== Es ; Aux \== []),
    !,
    append(Temp,[P],N_Temp),
    espacos_com_posicoes_comuns(R,Es,L_Es,N_Temp).

/* intersect sem atribuicao */
intersecao(L1,L2,X):-
    findall(L1,(member(I,L1),member(J,L2),I == J), X).

obtem_pares(L,Final):-
    findall(X,(member(X,L),nth1(Final,L,X)),Final).


obtem_comuns(Palavras, Comuns):-
    nth1(1,Palavras,Pal),
    subtract(Palavras, [Pal], LF),
    obtem_comuns(LF, Comuns, Pal, 0, []),
    !.
obtem_comuns( _, Comuns, Pal, N, Comuns):-length(Pal, N).
obtem_comuns(Palavras, Comuns, Pal, N, Aux):-
    nth0(N, Pal, Letter),
    maplist(obtem_comuns_aux(N, Letter), Palavras),
    N1 is N+1,
    append(Aux,[(N1,Letter)], Temp),
    obtem_comuns(Palavras, Comuns, Pal, N1, Temp).
obtem_comuns(Palavras, Comuns, Pal, N, Aux):-
    N1 is N+1,
    obtem_comuns(Palavras, Comuns, Pal, N1, Aux).

obtem_comuns_aux(N,Letter,L):-
    nth0(N, L, X),
    X == Letter.
