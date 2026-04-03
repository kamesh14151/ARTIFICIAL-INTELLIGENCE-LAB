hanoi(1, Source, Dest, _) :-
    format('Move disk from ~w to ~w~n', [Source, Dest]).

hanoi(N, Source, Dest, Aux) :-
    N > 1,
    M is N - 1,
    hanoi(M, Source, Aux, Dest),
    hanoi(1, Source, Dest, Aux),
    hanoi(M, Aux, Dest, Source).

run_hanoi :-
    write('Enter number of disks: '), read(N),
    hanoi(N, left, right, middle).
