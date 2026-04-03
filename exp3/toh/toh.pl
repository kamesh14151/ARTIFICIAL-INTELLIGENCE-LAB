goal([1,2,3,4,5,6,7,8,0]).

move([0,X,Y|Rest], [X,0,Y|Rest]).
move([X,0,Y|Rest], [0,X,Y|Rest]).

solve(State) :-
    goal(State).
