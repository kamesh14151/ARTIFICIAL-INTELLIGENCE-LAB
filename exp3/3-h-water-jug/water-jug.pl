% State represented as state(Jug1, Jug2)

move(state(X, Y), fill1, state(4, Y)) :- X < 4.
move(state(X, Y), fill2, state(X, 3)) :- Y < 3.
move(state(X, Y), empty1, state(0, Y)) :- X > 0.
move(state(X, Y), empty2, state(X, 0)) :- Y > 0.
move(state(X, Y), pour12, state(X1, Y1)) :-
    X > 0, Y < 3,
    Transfer is min(X, 3 - Y),
    X1 is X - Transfer,
    Y1 is Y + Transfer.
move(state(X, Y), pour21, state(X1, Y1)) :-
    Y > 0, X < 4,
    Transfer is min(Y, 4 - X),
    X1 is X + Transfer,
    Y1 is Y - Transfer.

solve(State, Goal, Path) :- bfs([[State]], Goal, Path).

bfs([[Goal|Rest]|_], Goal, [Goal|Rest]).
bfs([Path|Queue], Goal, Solution) :-
    extend(Path, NewPaths),
    append(Queue, NewPaths, Queue1),
    bfs(Queue1, Goal, Solution).

extend([State|Rest], NewPaths) :-
    findall([NewState,State|Rest],
            move(State, _, NewState),
            NewPaths).

run_jug :-
    writeln('Initial state is (0,0). Goal is (2,0).'),
    solve(state(0,0), state(2,0), Path),
    writeln('Solution Path:'),
    writeln(Path).
