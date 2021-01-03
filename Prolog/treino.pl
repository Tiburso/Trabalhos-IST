menor([P|R], M):-
    menor([P|R],M, P).

menor([],M,M).
menor([P|R],M,Temp):-
    P < Temp,
    !,
    menor(R, M, P).

menor([_|R], M, Temp):-
    menor(R, M, Temp).


menor_l(N, L, M):-
    menor(L, Min),
    N >= Min,
    !,
    M = Min.

menor_l(N, _, M):- M = N.

nth(1, [Elem|_], Elem) :- !.
nth(Pos, [_|Tail], Elem) :-
    Pos_1 is Pos - 1,
    nth(Pos_1, Tail, Elem).

xpto(Pos, Num, Lista) :-
    nth(Pos, Lista, Elem),
    Elem < Num.

heroi(capitaoAmerica).
heroi(deadpool) :- !.
heroi(homemDeFerro).
voa(homemDeFerro).
heroi_pes_na_terra_1(X) :- heroi(X), not(voa(X)).
heroi_pes_na_terra_2(X) :- not(voa(X)), heroi(X).


remRep([],[]).
remRep([ H | T], L) :- not(member(H, T)), remRep(T, L), !.
remRep([ H | T], [ H | L]) :- remRep(T, L).

alcunha([], _, _, []).
alcunha([H|R],Nome, Alcunha, [Alcunha|LF]):-
    H == Nome, !,
    alcunha(R, Nome, Alcunha, LF).

alcunha([H|R],Nome, Alcunha, [H|LF]):-
    H \== Nome,
    alcunha(R, Nome, Alcunha, LF).

par(N):- 0 is N mod 2.
filtra_pares([],[]).
filtra_pares([H|R1],[H|R]):-
    par(H), !,
    filtra_pares(R1,R).
filtra_pares([H|R1],R):-
    \+ par(H), !,
    filtra_pares(R1,R).

substitui(_,_,[],[]).
substitui(X,Y,[X|R1],[Y|R]):- substitui(X,Y,R1,R), !.
substitui(X,Y,[H|R1], [H|R]):- substitui(X,Y,R1,R).

xpto(X,Y,L1,L3) :-
    substitui(X, Y, L1, L2),
    substitui(Y, X, L2, L3).

agrupa2(L1, L2,L3):-
    agrupa2(L1,L2,L3,[]).
agrupa2(_,[],LF,LF):- !.
agrupa2(L1,L2,L3,LF):-
    length(L1, N1),
    length(L2, N2),
    random_between(1,N1,I1),
    random_between(1,N2,I2),
    nth1(I1,L1,P1),
    subtract(L1,[P1],LF1),
    nth1(I2,L2,P2),
    subtract(L2,[P2],LF2),
    append(LF,[[P1,P2]],N_LF),
    agrupa2(LF1, LF2, L3, N_LF).
