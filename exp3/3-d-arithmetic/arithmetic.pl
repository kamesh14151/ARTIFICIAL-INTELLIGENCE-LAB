add(X, Y, R) :- R is X + Y.
sub(X, Y, R) :- R is X - Y.
multiply(X, Y, R) :- R is X * Y.
divide(X, Y, R) :- Y \= 0, R is X / Y.

run_arithmetic :-
    write('Enter operation (add/sub/multiply/divide): '), read(Op),
    write('Enter first number: '), read(X),
    write('Enter second number: '), read(Y),
    Goal =.. [Op, X, Y, R],
    (call(Goal) -> format('Result = ~w~n', [R]) ; writeln('Invalid operation')).
