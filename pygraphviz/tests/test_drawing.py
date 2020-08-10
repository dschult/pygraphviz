import pygraphviz as pgv
import pytest


def stringify(agraph):
    result = agraph.string().split()
    if '""' in result:
        result.remove('""')
    return " ".join(result)

def test_drawing_error_no_layout():
    with pytest.raises(AttributeError):
        A = pgv.AGraph(name="test graph")
        A.add_path([1, 2, 3, 4])
        d = A.draw(prog="nop")

def test_drawing_error_old():
    with pytest.raises(AttributeError):
        A = pgv.AGraph(name="test graph")
        A.add_path([1, 2, 3, 4])
        d = A.draw_command_line()


# this is not a very good way to test...
# def test_drawing():
#    A = pgv.AGraph(name='test graph')
#    A.add_path([1,2,3,4])
#    d = A.draw(prog='neato')
#    assert len(d.splitlines()) == 19
# FIXME
# smoke test
# >>> (fd,fname)=tempfile.mkstemp()
# >>> A.draw(fname,format='ps',prog='neato')
# >>> A.draw(fname,prog='neato')
#def test_smoketests():
#    (fd, fname) = tempfile.mkstemp()
#    A.draw(fname, format="ps", prog="neato")
#    A.draw(fname, prog="neato")
def test_drawing_makes_file():
    A = pgv.AGraph(name='test graph')
    A.add_path([1, 2, 3, 4])
#    print(A.to_string())
#    A.layout()
#    print("hi", A.has_layout)
#    print("use dot", A.to_string())
    A.draw("test_gvRender1.png", prog="twopi")
    A.draw("test_gvRender.png")
#    print("all args")
    A.draw(path="test_gvRender_all.png", prog=b"circo", format="png")


def test_drawing_to_create_dot_string():
    A = pgv.AGraph(name='test graph')
    A.add_path([1, 2, 3, 4])
    A.layout()
    dot_rep = A.to_string()
    expected = """strict graph "test graph" {
	graph [bb="0,0,70.071,250.3"];
	node [label="\\N"];
	1	[height=0.5,
		pos="27,18",
		width=0.75];
	2	[height=0.5,
		pos="43.071,88.469",
		width=0.75];
	1 -- 2	[pos="31.139,36.148 33.557,46.75 36.596,60.077 39.002,70.627"];
	3	[height=0.5,
		pos="41.467,160.69",
		width=0.75];
	2 -- 3	[pos="42.666,106.69 42.423,117.64 42.115,131.52 41.872,142.47"];
	4	[height=0.5,
		pos="32.966,232.3",
		width=0.75];
	3 -- 4	[pos="39.322,178.76 38.043,189.53 36.424,203.17 35.14,213.98"];
}
"""
    print("dot representation:", dot_rep)
    assert expected == dot_rep

def test_name_error():
    with pytest.raises(ValueError):
        A = pgv.AGraph(name="test graph")
        A.draw("foo", prog="foo")

def test_name_error_old():
    with pytest.raises(ValueError):
        A = pgv.AGraph(name="test graph")
        A.draw_command_line("foo", prog="foo")
