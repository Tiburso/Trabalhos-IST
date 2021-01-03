insere_ordenado(N, L1, L2):-
    findall(El,(member(El, L1), El < N), Menores),
    subtract(L1, Menores, Maiores),append([Menores,[N], Maiores], L2).

junta_novo_aleatorio(L1,L_inf,L_sup,LF):-
    findall(N , between(L_inf,L_sup, N), Todos),
    subtract(Todos, L1, Possiveis),
    length(Possiveis, Comp),
    random_between(1, Comp, Pos),
    insere_ordenado(Pos, L1, LF).

repete_el(El, N, L):-
    length(L, N),
    maplist(=(El), L).


duplica_elementos(L1,L2):-
    findall([El,El] , member(El,L1), Dups),
    flatten(Dups, L2).

num_occ(Lst, El, N):-
    include(==(El), Lst, El_iguais),
    length(El_iguais, N).

substitui_maiores_N(N, Subst, L1, L2):-
    maplist(subst_aux(N, Subst), L1, L2), !.

subst_aux(N, Novo, El, Novo):- El > N.
subst_aux(N, _, El, El):- El =< N.

