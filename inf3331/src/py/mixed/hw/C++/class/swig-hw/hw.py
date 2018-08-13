# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.
import _hw
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


class HelloWorld(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, HelloWorld, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, HelloWorld, name)
    def __init__(self,*args):
        _swig_setattr(self, HelloWorld, 'this', apply(_hw.new_HelloWorld,args))
        _swig_setattr(self, HelloWorld, 'thisown', 1)
    def __del__(self, destroy= _hw.delete_HelloWorld):
        try:
            if self.thisown: destroy(self)
        except: pass
    def set(*args): return apply(_hw.HelloWorld_set,args)
    def get(*args): return apply(_hw.HelloWorld_get,args)
    def message(*args): return apply(_hw.HelloWorld_message,args)
    def print_(*args): return apply(_hw.HelloWorld_print_,args)
    def __repr__(self):
        return "<C HelloWorld instance at %s>" % (self.this,)

class HelloWorldPtr(HelloWorld):
    def __init__(self,this):
        _swig_setattr(self, HelloWorld, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, HelloWorld, 'thisown', 0)
        _swig_setattr(self, HelloWorld,self.__class__,HelloWorld)
_hw.HelloWorld_swigregister(HelloWorldPtr)

class HelloWorld2(HelloWorld):
    __swig_setmethods__ = {}
    for _s in [HelloWorld]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, HelloWorld2, name, value)
    __swig_getmethods__ = {}
    for _s in [HelloWorld]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, HelloWorld2, name)
    def gets(*args): return apply(_hw.HelloWorld2_gets,args)
    def __init__(self,*args):
        _swig_setattr(self, HelloWorld2, 'this', apply(_hw.new_HelloWorld2,args))
        _swig_setattr(self, HelloWorld2, 'thisown', 1)
    def __del__(self, destroy= _hw.delete_HelloWorld2):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C HelloWorld2 instance at %s>" % (self.this,)

class HelloWorld2Ptr(HelloWorld2):
    def __init__(self,this):
        _swig_setattr(self, HelloWorld2, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, HelloWorld2, 'thisown', 0)
        _swig_setattr(self, HelloWorld2,self.__class__,HelloWorld2)
_hw.HelloWorld2_swigregister(HelloWorld2Ptr)


