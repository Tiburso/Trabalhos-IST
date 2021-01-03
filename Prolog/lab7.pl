nao_membro(_,[]):- !.
nao_membro(N,[P|R]):-
    N \== P,
    nao_membro(N,R).

insere_ordenado(N, [],[N]).
insere_ordenado(N,[P|R],[N,P|R]):-
    N < P,
    !.
insere_ordenado(N,[P|R],[P|Temp]):-
    N >= P,
    insere_ordenado(N,R,Temp).

junta_novo_aleatorio(L1, Lim_inf, Lim_sup, L2):-
    random_between(Lim_inf, Lim_sup, N),
    nao_membro(N, L1),
    insere_ordenado(N, L1, L2).

n_aleatorios(N,L_inf,L_sup,L):-
    n_aleatorios(N,L_inf,L_sup,L,[]).
n_aleatorios(N,_,_,L,L):- length(L,N). /* tentar fazer com decremento de N */
n_aleatorios(N,L_inf,L_sup,L,Aux):-
    junta_novo_aleatorio(Aux,L_inf, L_sup, N_aux),
    n_aleatorios(N,L_inf, L_sup, L, N_aux).

chave_euromilhoes(Numeros,Estrelas):-
    n_aleatorios(5,1,50,Numeros),
    n_aleatorios(2,1,12,Estrelas).


comp_maior_lista([P|R],C):-
    length(P,Temp),
    comp_maior_lista(R,C,Temp).
comp_maior_lista([],C,C).
comp_maior_lista([P|R],C, Aux):-
    length(P,N),
    N > Aux,
    comp_maior_lista(R,C,N).
comp_maior_lista([P|R],C, Aux):-
    length(P,N),
    N =< Aux,
    comp_maior_lista(R,C,Aux).


duplica_elementos(L1,L2):-
    duplica_elementos(L1,L2,[]).
duplica_elementos([],L,L).
duplica_elementos([P|R],L,L_aux):-
    append(L_aux,[P,P],N_aux),
    duplica_elementos(R,L,N_aux).

/*duplica_elementos([],[]).
duplica_elementos([P|R],L):-
    duplica_elementos(R,R_aux),
    L = [P,P|R_aux].*/



