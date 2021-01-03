suc(N,M):-
    M is N + 1.

ant(N,M):-
    M is N - 1.

perimetro(R,P):-
    P is 2*R*pi.

divisor(D,N):-
    0 is D mod N.

aplica_op(+,Val1,Val2,Res) :- Res is Val1 + Val2.
aplica_op(-,Val1,Val2,Res) :- Res is Val1 - Val2.
aplica_op(*,Val1,Val2,Res) :- Res is Val1 * Val2.
aplica_op(/,Val1,Val2,Res) :- Res is Val1 / Val2.

soma_digitos_r(_,0).
soma_digitos_r(N,Sum):-
    R is N mod 10,
    Sum_N is +(Sum, R),
    soma_digitos(N/10, Sum_N).
