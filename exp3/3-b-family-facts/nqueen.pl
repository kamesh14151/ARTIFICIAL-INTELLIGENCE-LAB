queen(0,[]).

queen(N,[X|Y]) :-
    N1 is N-1,
    queen(N1,Y),
    member(X,[1,2,3,4,5,6,7,8]),
    safe(X,Y,1).

safe(_,[],_).

safe(X,[Y|T],D) :-
    X =\= Y,
    abs(X-Y) =\= D,
    D1 is D+1,
    safe(X,T,D1).
