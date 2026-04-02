% Facts
parent(john, mary).
parent(mary, sam).
parent(john, alice).

male(john).
female(mary).
female(alice).

% Rule
grandparent(X,Z) :- parent(X,Y), parent(Y,Z).
