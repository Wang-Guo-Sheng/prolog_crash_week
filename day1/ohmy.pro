cat(lion).
cat(tiger).

dorothy(X, Y, Z) :- Y = tiger, lion = X, Z = bear.
twin_cats(X, Y) :- cat(X), cat(Y).
