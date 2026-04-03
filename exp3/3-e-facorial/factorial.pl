factorial(0, 1).
factorial(N, R) :-
    N > 0,
    N1 is N - 1,
    factorial(N1, R1),
    R is N * R1.

run_factorial :-
    write('Enter a number: '), read(N),
    factorial(N, R),
    format('Factorial of ~w = ~w~n', [N, R]).
