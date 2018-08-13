#!/usr/bin/env python
import os, sys

#os.system('f2py -m ext_gridloop -c --fcompiler='Gnu' gridloop.f')

# force use of Numeric (for F2py):
os.environ['NUMTOOLSARRAY'] = 'Numeric'  
from py4cs.numpytools import *


# local data, as in Grid2D:
xcoor = sequence(0, 1, 0.5, Float)
ycoor = sequence(0, 1, 1, Float)
a = zeros((size(xcoor),size(ycoor)), Float)
print 'a is', type(a)
print 'x =', xcoor, '\ny =', ycoor

def dump():
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            print 'value at (%g,%g)  \t = a[%d,%d] = %g' % \
                  (xcoor[i], ycoor[j], i, j, a[i,j])
def myfunc(x, y):
    r = x + 2*y
    print 'in myfunc...return', r
    return r

import ext_gridloop

print ext_gridloop.gridloop1_v1.__doc__
ext_gridloop.gridloop1_v1(a, xcoor, ycoor, myfunc)
print 'a after gridloop_v1:\n', a
dump()
print 'a is still filled with zeros!\n\n'

# try something simple and compare 1-dim and 2-dim arrays:
print ext_gridloop.change.__doc__
ext_gridloop.change(a, xcoor, ycoor)
print 'a after change:\n', a
print 'xcoor after change:\n', xcoor
print 'ycoor after change:\n', ycoor

# repair x and y (a is ok in the calling code):
xcoor = sequence(0, 1, 0.5, Float)
ycoor = sequence(0, 1, 1, Float)


print ext_gridloop.gridloop2.__doc__
a = ext_gridloop.gridloop2(xcoor, ycoor, myfunc)
print 'a after gridloop2:\n', a
dump()
print 'a is correct!\n\n'

# work with an input _and_ output array:
print ext_gridloop.gridloop3.__doc__
a[:,:] = -1.0
print 'Fortran storage of a?', \
      ext_gridloop.has_column_major_storage(a)
b = ext_gridloop.gridloop3(a, xcoor, ycoor, myfunc)
print 'a after gridloop3:\n', a
print 'is a overwritten?', a is b
dump()
print 'a is correct!\n\n'

# work with an overwrite statement:
print ext_gridloop.gridloop4.__doc__
a = zeros((size(xcoor),size(ycoor)), Float)  # C storage
print 'NumPy array; Fortran storage of a?', \
      ext_gridloop.has_column_major_storage(a)
a = ext_gridloop.as_column_major_storage(a)
print 'after as_column_major_storage; Fortran storage of a?', \
      ext_gridloop.has_column_major_storage(a)
a[:,:] = -1.0
b = ext_gridloop.gridloop4(a, xcoor, ycoor, myfunc)
print 'a after gridloop4:\n', a
print 'is a overwritten?', a is b
dump()
print 'a is correct!\n\n'
# let a be a NumPy array with C storage:
a = zeros((size(xcoor),size(ycoor)), Float)
print 'Fortran storage of a?', \
      ext_gridloop.has_column_major_storage(a)
b = ext_gridloop.gridloop4(a, xcoor, ycoor, myfunc)
print 'b after gridloop4:\n', b
print 'is a overwritten?', a is b
print 'b is correct!\n\n'

# work with an inout array (imporant: start with Fortran
# column major storage)
a = ext_gridloop.as_column_major_storage(\
    zeros((size(xcoor),size(ycoor)), Float))
print ext_gridloop.gridloop1_v2.__doc__
print 'Fortran storage of a?', \
      ext_gridloop.has_column_major_storage(a)
ext_gridloop.gridloop1_v2(a, xcoor, ycoor, myfunc)
print 'a after gridloop1_v2:\n', a
dump()
print 'a is correct!\n\n'

# try again, this time with a fresh NumPy (C) array as input:
a = zeros((size(xcoor),size(ycoor)), Float)
try:
    print 'Fortran storage of a?', \
      ext_gridloop.has_column_major_storage(a)
    ext_gridloop.gridloop1_v2(a, xcoor, ycoor, myfunc)
except:
    pass

a = ext_gridloop.as_column_major_storage(\
    zeros((size(xcoor),size(ycoor)), Float)) # column major storage
print 'Fortran storage of a?', \
      ext_gridloop.has_column_major_storage(a)
ext_gridloop.gridloop1_v2(a, xcoor, ycoor, myfunc)
print 'a after gridloop1_v2 with a c2fdim2 transformation:\n', a
dump()
print 'a is correct!\n\n'
# this is the way to realize the gridloop1 function!!


# try gridloop_v3, which declares a as intent(inout,c):
a = zeros((size(xcoor),size(ycoor)), Float)
print ext_gridloop.gridloop1_v3.__doc__
print 'Fortran storage of a?', \
      ext_gridloop.has_column_major_storage(a)
ext_gridloop.gridloop1_v3(a, xcoor, ycoor, myfunc)
print 'a after gridloop1_v3:\n', a
print 'Fortran storage of a?', \
      ext_gridloop.has_column_major_storage(a)
dump()
print 'a is NOT correct!\n\n'

# try gridloop_v4, which declares a as intent(inout,c),
# but we operate on the transpose of a:
a = zeros((size(xcoor),size(ycoor)), Float)
print ext_gridloop.gridloop1_v4.__doc__
print 'Fortran storage of a?', \
      ext_gridloop.has_column_major_storage(a)
ext_gridloop.gridloop1_v4(a, xcoor, ycoor, myfunc)
print 'a after gridloop1_v4:\n', a
print 'Fortran storage of a?', \
      ext_gridloop.has_column_major_storage(a)
dump()
print 'a is correct!\n\n'



