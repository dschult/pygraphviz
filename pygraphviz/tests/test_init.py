import pygraphviz as pgv
stringify = pgv.testing.stringify

def test_simple1():
    A = pgv.AGraph(name="")
    assert stringify(A) == "strict graph { }"

def test_drawing_simple():
    A = pgv.AGraph(name="")
    A.draw("twopi", args="-Grotate=90 -Nshape=box")
    assert stringify(A) == "strict graph { }"
    A = pgv.AGraph(name="")
    assert stringify(A) == "strict graph { [Graph rotate=90]; [Node shape=box] }"

def test_simple2():
    A = pgv.AGraph(name="")
    assert stringify(A) == "strict graph { }"
