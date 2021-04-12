different(red, green).
different(red, blue).
different(green, red).
different(green, blue).
different(blue, red).
different(blue, green).

coloring(Alabama, Mississippi, Georgia, Tennesse, Florida) :-
    different(Mississippi, Tennesse),
    different(Mississippi, Alabama),
    different(Alabama, Tennesse),
    different(Alabama, Mississippi),
    different(Alabama, Georgia),
    different(Alabama, Florida),
    different(Georgia, Florida),
    different(Georgia, Tennesse).
