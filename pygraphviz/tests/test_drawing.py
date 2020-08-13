from tempfile import TemporaryFile
import pytest
import pygraphviz as pgv
stringify = pgv.testing.stringify


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


def test_name_error():
    with pytest.raises(ValueError):
        A = pgv.AGraph(name="test graph")
        A.draw("foo", prog="foo")


def test_name_error_old():
    with pytest.raises(ValueError):
        A = pgv.AGraph(name="test graph")
        A.draw_command_line("foo", prog="foo")


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
#    print(A.has_layout)
#    print(A.to_string())
    with TemporaryFile() as fh:
        A.draw(fh, format="jpg")
        assert fh.tell() > 0
    with TemporaryFile() as fh:
        A.draw(fh, format="png", prog="twopi")
        assert fh.tell() > 0
    with TemporaryFile() as fh:
        A.draw(path=fh, prog="circo", format="png")
        assert fh.tell() > 0

def test_name1():
    A = pgv.AGraph(name="")
    assert stringify(A) == "strict graph { }"
    assert A.__repr__()[0:7] == "<AGraph"

def test_drawing_args():
    A = pgv.AGraph(name='test graph')
    A.add_path([1, 2, 3, 4])
#    A.draw(path="wrap.png", prog="twopi")
#    A.draw(path="wrapblank.png", prog="twopi",args="-Nshape=circle")
    args = "-Ncolor=red -Nshape=box -Efontsize=8 -Grotate=90"
#    A.draw(path="wrapargs.pdf", prog="twopi", args=args)
    with TemporaryFile() as fh:
        A.draw(fh, format="dot", prog="twopi", args=args)
        fh.seek(0)
        dot_string = fh.read().decode(A.encoding)
    with TemporaryFile() as fh:
        A.draw(fh, format="dot", prog="twopi", args=" ")
        fh.seek(0)
        dot_string = fh.read().decode(A.encoding)
    print(dot_string)
    print(A.string())
    #assert "red" in dot_string
    #assert "fontsize" in dot_string
    #assert "rotate" in dot_string

def test_name2():
    A = pgv.AGraph(name="")
    assert stringify(A) == "strict graph { }"
    assert A.__repr__()[0:7] == "<AGraph"


def test_drawing_to_create_dot_string():
    A = pgv.AGraph(name='test graph')
    A.add_path([1, 2, 3, 4])
    A.layout()
    dot_rep = A.to_string()
    assert "test graph" in dot_rep
    assert "strict graph" in dot_rep
    assert "pos" in dot_rep
    assert "height" in dot_rep
    assert "width" in dot_rep
    assert "1 -- 2" in dot_rep
    assert "2 -- 3" in dot_rep
    assert "3 -- 4" in dot_rep

    # unfortunately, the layout and dot outcomes vary
    # with system and graphviz version. One example is
    # shown here, the numbers can be very different.
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
    #print("dot representation:", dot_rep)
    #assert expected == dot_rep
