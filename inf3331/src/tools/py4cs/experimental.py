"""Just some experimental unfinished code."""

class NoneArrayObject(object):
    """Generalization of None for arrays."""
    # could subclass NumArray or UserArray
    def __nonzero__(self):
        return False
    def __getitem__(self, i):
        raise IndexError, \
              'illegal index %s in NoneArray (undefined array)' % str(i)
    def __setitem__(self, i, v):
        raise IndexError, \
              'illegal index %s in NoneArray (undefined array)' % str(i)

NoneArray = NoneArrayObject()
from numarray import *

class ArrayGen(NumArray):
    def __init__(self, data, typecode=None, base=None):
        NumArray.__init__(self, data, typecode)
        self.base = base

    def setbase(self, base):
        self.base = base
        
    def __base0(self, index):
        if self.base is None:
            return index
        if type(index) == type(2):
            if not type(self.base) == type(2):
                raise TypeError, \
                      "base is not compatible with integer index"
            else:
                return index - self.base
        else:  # index is tuple
            ind = list(index)
            if len(ind) != len(self.base):
                raise IndexError, "base has length different from index"
            for i in range(len(index)):
                ind[i] = ind[i] - self.base[i]
            return tuple(ind)
    
    def __setitem__(self, i, value):
        UserArray.__setitem__(self, self.__base0(i), value)

    def __getitem__(self, i):
        UserArray.__getitem__(self, self.__base0(i))

    def __getslice__(self, i, j): 
        UserArray.__getslice__(self, self.__base0(i),
                               self.__base0(j))

    def __setslice__(self, i, j, value):
        UserArray.__setslice__(self, self.__base0(i),
                               self.__base0(j), value)

    def printf(self, format="%g", file=sys.stdout, name=""):
        # name[1,4]=...
        pass

def test_ArrayGen():
    a = ArrayGen([1.0, 2.0, 5.0, 8, 9, 10])
    a.shape = (3,2)
    a.setbase((2,2))
    a.base = (2,3)
    print a
    a[2,3] = -77
    print a
