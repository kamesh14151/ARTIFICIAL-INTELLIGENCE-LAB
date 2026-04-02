move(state(X,Y), fill1, state(4,Y)) :- X < 4.
move(state(X,Y), fill2, state(X,3)) :- Y < 3.

move(state(X,Y), empty1, state(0,Y)) :- X > 0.
move(state(X,Y), empty2, state(X,0)) :- Y > 0.

move(state(X,Y), pour12, state(X1,Y1)) :-
    X > 0,
    Y < 3,
    T is min(X,3-Y),
    X1 is X-T,
    Y1 is Y+T.

goal(state(2,_)).
