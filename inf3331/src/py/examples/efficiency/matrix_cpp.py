# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.
import _matrix_cpp
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


class Matrix(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Matrix, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Matrix, name)
    def __init__(self,*args):
        _swig_setattr(self, Matrix, 'this', apply(_matrix_cpp.new_Matrix,args))
        _swig_setattr(self, Matrix, 'thisown', 1)
    def __del__(self, destroy= _matrix_cpp.delete_Matrix):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __call__(*args): return apply(_matrix_cpp.Matrix___call__,args)
    def set(*args): return apply(_matrix_cpp.Matrix_set,args)
    def get(*args): return apply(_matrix_cpp.Matrix_get,args)
    def fill1(*args): return apply(_matrix_cpp.Matrix_fill1,args)
    def fill2(*args): return apply(_matrix_cpp.Matrix_fill2,args)
    def __repr__(self):
        return "<C Matrix instance at %s>" % (self.this,)

class MatrixPtr(Matrix):
    def __init__(self,this):
        _swig_setattr(self, Matrix, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, Matrix, 'thisown', 0)
        _swig_setattr(self, Matrix,self.__class__,Matrix)
_matrix_cpp.Matrix_swigregister(MatrixPtr)


