fibonacci(0, 0).
fibonacci(1, 1).
fibonacci(N, R) :-
    N > 1,
    N1 is N - 1,
    N2 is N - 2,
    fibonacci(N1, R1),
    fibonacci(N2, R2),
    R is R1 + R2.

run_fibonacci :-
    write('Enter a number: '), read(N),
    fibonacci(N, R),
    format('Fibonacci(~w) = ~w~n', [N, R]).
