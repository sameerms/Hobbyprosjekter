#!/usr/bin/env python
"""
Comparison of scalar and vectorized sine functions when
the argument is a scalar.
A test on a**b vs pow(a,b) is also included.
"""

import timeit, sys

try:
    n = int(sys.argv[1])
except:
    n = 1000000  # default

print 'n =', n

t1 = timeit.Timer('sin(1.2)',
                  setup='from Numeric import sin').timeit(n)
t2 = timeit.Timer('sin(1.2)',
                  setup='from math import sin').timeit(n)
t3 = timeit.Timer('sin(1.2)',
                  setup='from numarray import sin').timeit(n)

best = min(t1, t2, t3)
print """
single expression sin(1.2)
Numeric sin    %.2f
math sin       %.2f
numarray sin   %.2f
""" % (t1/best, t2/best, t3/best)

# module.sin vs just sin:
t4 = timeit.Timer('Numeric.sin(1.2)',  setup='import Numeric').timeit(n)
t5 = timeit.Timer('math.sin(1.2)',     setup='import math').timeit(n)
t6 = timeit.Timer('numarray.sin(1.2)', setup='import numarray').timeit(n)

best2 = min(t4, t5, t6)
print """
single expression module.sin(1.2)
Numeric.sin    %.2f    %.2f
math.sin       %.2f    %.2f
numarray.sin   %.2f    %.2f
""" % (t4/best2, t4/best, t5/best2, t5/best, t6/best2, t6/best)

# call to function involving intrinsic functions:
sc = 'myfunc(1.2, 1.4)'
f = """ sin, cos, exp
def myfunc(x, y):
    return x**2 + cos(x*y)*sin(x)
"""
t7 = timeit.Timer(sc, setup='from Numeric import'+f).timeit(n)
t8 = timeit.Timer(sc, setup='from math import'+f).timeit(n)
t9 = timeit.Timer(sc, setup='from numarray import'+f).timeit(n)

best = min(t7, t8, t9)
print """
call to function with sin/cos/pow
Numeric sin    %.2f
math sin       %.2f
numarray sin   %.2f
""" % (t7/best, t8/best, t9/best)

f = """ as N
def myfunc(x, y):
    return x*x + N.cos(x*y)*N.sin(x)
"""
t7b = timeit.Timer(sc, setup='import Numeric'+f).timeit(n)
t8b = timeit.Timer(sc, setup='import math'+f).timeit(n)
t9b = timeit.Timer(sc, setup='import numarray'+f).timeit(n)

bestb = min(t7b, t8b, t9b)
print """
call to function with N.sin/N.cos
Numeric sin    %.2f   %.2f
math sin       %.2f   %.2f
numarray sin   %.2f   %.2f
""" % (t7b/bestb, t7b/best, t8b/bestb, t8b/best, t9b/bestb, t9b/best)

t10 = timeit.Timer('a**b', setup='a=1.1; b=1.2').timeit(n)
t11 = timeit.Timer('pow(a,b)',
                   setup='from math import pow; a=1.1; b=1.2').timeit(n)
t12 = timeit.Timer('pow(a,b)',
                   setup='from operator import pow; a=1.1; b=1.2').timeit(n)
best = min(t10, t11, t12)
print """
a**b            %.2f
pow(a,b)        %.2f  (from math import pow)
pow(a,b)        %.2f  (from operator import pow)
""" % (t10/best, t11/best, t12/best)

