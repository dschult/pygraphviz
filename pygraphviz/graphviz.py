# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _graphviz

def _swig_setattr(self,class_type,name,value):
    if (name == "this"):
        if isinstance(value, class_type):
            self.__dict__[name] = value.this
            if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
            del value.thisown
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    self.__dict__[name] = value

def _swig_getattr(self,class_type,name):
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types



agopen = _graphviz.agopen

agclose = _graphviz.agclose

agread = _graphviz.agread

agconcat = _graphviz.agconcat

agwrite = _graphviz.agwrite

agnnodes = _graphviz.agnnodes

agnedges = _graphviz.agnedges

agisundirected = _graphviz.agisundirected

agisdirected = _graphviz.agisdirected

agsubg = _graphviz.agsubg

agfstsubg = _graphviz.agfstsubg

agnxtsubg = _graphviz.agnxtsubg

agparent = _graphviz.agparent

agroot = _graphviz.agroot

agdelsubg = _graphviz.agdelsubg

agnode = _graphviz.agnode

agidnode = _graphviz.agidnode

agsubnode = _graphviz.agsubnode

agfstnode = _graphviz.agfstnode

agnxtnode = _graphviz.agnxtnode

agdelnode = _graphviz.agdelnode

agdegree = _graphviz.agdegree

agedge = _graphviz.agedge

agsubedge = _graphviz.agsubedge

agdeledge = _graphviz.agdeledge

aghead = _graphviz.aghead

agtail = _graphviz.agtail

agfstedge = _graphviz.agfstedge

agnxtedge = _graphviz.agnxtedge

agfstin = _graphviz.agfstin

agnxtin = _graphviz.agnxtin

agfstout = _graphviz.agfstout

agnxtout = _graphviz.agnxtout

agattrsym = _graphviz.agattrsym

agattr = _graphviz.agattr

agnxtattr = _graphviz.agnxtattr

agget = _graphviz.agget

agxget = _graphviz.agxget

agset = _graphviz.agset

agxset = _graphviz.agxset

agattrname = _graphviz.agattrname

agattrdefval = _graphviz.agattrdefval

agraphof = _graphviz.agraphof

agnameof = _graphviz.agnameof

agisarootobj = _graphviz.agisarootobj

AGDATA = _graphviz.AGDATA

AGID = _graphviz.AGID

AGTYPE = _graphviz.AGTYPE
AGRAPH = _graphviz.AGRAPH
AGNODE = _graphviz.AGNODE
AGOUTEDGE = _graphviz.AGOUTEDGE
AGINEDGE = _graphviz.AGINEDGE
AGEDGE = _graphviz.AGEDGE
cvar = _graphviz.cvar
