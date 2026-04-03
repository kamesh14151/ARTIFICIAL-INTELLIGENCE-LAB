% Facts
like(john, pizza).
hate(mary, rain).
own(john, car).
father(john, mike).
female(mary).

% Rules
may_steal(X, Y) :- own(Y, X).

% Interactive query
run_like :-
    write('Enter person: '), read(P),
    write('Enter item: '), read(I),
    (like(P, I) -> writeln('True') ; writeln('False')).
