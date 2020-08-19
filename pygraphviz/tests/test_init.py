import pygraphviz as pgv
stringify = pgv.testing.stringify

def test_simple1():
    A = pgv.AGraph(name="")
    assert stringify(A) == "strict graph { }"

def test_drawing_simple():
    A = pgv.AGraph(name="")
    A.draw_with_args("twopi", args="-Grotate=90 -Nshape=box")
    del A.graph_attr["bb"]
    del A.graph_attr["label"]
    assert stringify(A) == "strict graph { graph [rotate=90]; node [shape=box]; }"
    A = pgv.AGraph(name="")
    assert stringify(A) == "strict graph { }"

def test_simple2():
    A = pgv.AGraph(name="")
    assert stringify(A) == "strict graph { }"
