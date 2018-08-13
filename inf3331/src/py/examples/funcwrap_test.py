#!/usr/bin/env python
from py4cs.numpytools import *

f1 = wrap2callable(2.0)
print "constant:", f1(0.5)

f2 = wrap2callable('1+2*x')
print "string formula of x:", f2(0.5)

f3 = wrap2callable('1+2*t', independent_variables='t')
print "string formula of t:", f3(0.5)

f4 = wrap2callable('a+b*t', independent_variables='t', a=1, b=2)
print "string formula with parameters:", f4(0.5)

x = seq(0,1,0.5); y=1+2*x
f5 = wrap2callable((x,y))
print "interpolate discrete data (at a grid point):", f5(0.5)
print "interpolate again (not at a grid point):", f5(0.51), 1+2*0.51

def myfunc(x):
    return 1+2*x
f6 = wrap2callable(myfunc)
print "user-defined function", f6(0.5)

f7 = wrap2callable(lambda x: 1+2*x)
print "user-defined anynomous lambda function:", f7(0.5)

class MyClass:
    """Representation of a function f(x; a, b) =a + b*x"""
    def __init__(self, a=1, b=1):
        self.a = a;  self.b = b
    def __call__(self, x):
        return self.a + self.b*x
myclass = MyClass(a=1, b=2)
f8 = wrap2callable(myclass)
print "user-defined class with __call__ method:", f8(0.5)

# three-dimensional functions:
f9 = wrap2callable('1+2*x+3*y+4*z', independent_variables=('x','y','z'))
print "3D string formula:", f9(0.5,1/3.,0.25)

y = seq(0,1,0.5)
z = seq(-1,0.5,0.1)
# for a three-dimensional grid use
xv = x[:,NewAxis,NewAxis]
yv = y[NewAxis,:,NewAxis]
zv = z[NewAxis,NewAxis,:]
def myfunc3(x, y, z):  return 1+2*x+3*y+4*z
values = myfunc3(xv, yv, zv)
f10 = wrap2callable((x, y, z, values))
print "interpolate 3D discrete data:", f10(0.5, 1/3., 0.25)
