% Facts
parent(john, mike).
parent(john, susan).
parent(mary, mike).
parent(mary, susan).

male(john).
male(mike).
female(mary).
female(susan).

% Rules
father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
siblings(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.

% Interactive query
run_family :-
    write('Enter relation (father/mother/grandparent/siblings): '), read(Rel),
    write('Enter first person: '), read(P1),
    write('Enter second person: '), read(P2),
    (call(Rel, P1, P2) -> writeln('True') ; writeln('False')).
