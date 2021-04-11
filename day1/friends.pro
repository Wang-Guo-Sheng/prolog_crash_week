likes(wallace, cheese).
likes(grommit, cheese).
likes(grommit, cake).
likes(wendolene, sheep).

friend(X, Y) :- \+(X = Y), likes(X, Z), likes(Y, Z).
