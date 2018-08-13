#!/usr/bin/env python
"""
Measure the efficiency of different Python constructions.
"""

from py4cs.misc import timer, timer_system
import sys, math, random, timeit
gmathsin = math.sin  # global name
from py4cs.numpytools import *
print 'Basic NumPy package:', basic_NumPy

def range_tests(n):

    print '\n*** Efficiency of loops, loop length =', n, '***\n'
    t1 = timeit.Timer('for i in range(n): pass',
                      setup='n=%d' % n).timeit(5)
    t2 = timeit.Timer('for i in xrange(n): pass',
                      setup='n=%d' % n).timeit(5)
    t3 = timeit.Timer('for i in iseq(stop=n-1): pass',
                      setup='from py4cs.numpytools import iseq;' +
                      'n=%d' % n).timeit(5)
    print 'range:   %.2f' % (t1/t2)
    print 'xrange:  %.2f' % (t2/t2)
    print 'iseq:    %.2f' % (t3/t2)

    t4 = timeit.Timer('[i for i in xrange(n)]',
                      setup='n=%d' % n).timeit(5)
    t5 = timeit.Timer('map(lambda i: i, xrange(n))',
                      setup='n=%d' % n).timeit(5)
    print 'list comprehension: %.2f' % (t4/t4)
    print 'corresponding map:  %.2f' % (t5/t4)


def allocate_tests(n):

    def list_append1(n):
        r = []
        for i in xrange(n):
            r.append(i+2)
        return r

    def list_chunk1(n):
        r = [0.0]*n
        for i in xrange(n):
            r[i] = i+2
        return r

    def list_append2(n):
        r = []
        for i in xrange(n):
            r.append(random.gauss(0,1))
        return r

    def list_chunk2(n):
        r = [0.0]*n
        for i in xrange(n):
            r[i] = random.gauss(0,1)
        return r

    def list_append3(n):
        g = random.gauss
        r = []
        for i in xrange(n):
            r.append(g(0,1))
        return r

    def list_append4(n):
        return [random.gauss(0,1) for i in xrange(n)]

    def list_chunk3(n):
        g = random.gauss
        r = [0.0]*n
        for i in xrange(n):
            r[i] = g(0,1)
        return r

    def NumPy_zeros(n):
        return zeros(n, Float)
    
    def NumPy_arange(n):
        return sequence(0,1,1.0/(n-1))
    
    def NumPy_random(n):
        import RandomArray
        return RandomArray.normal(0,1,n)
    

    print 'allocate n numbers in an array/list: n =', n
    # few calls, use timer instead of timeit
    rep = 3
    print timer(NumPy_zeros,  (n,), repetitions=rep)
    print timer(NumPy_arange, (n,), repetitions=rep)
    print timer(NumPy_random, (n,), repetitions=rep)
    print timer(list_append1, (n,), repetitions=rep)
    print timer(list_chunk1,  (n,), repetitions=rep)
    print timer(list_append2, (n,), repetitions=rep)
    print timer(list_append4, (n,), repetitions=rep)
    print timer(list_chunk2,  (n,), repetitions=rep)
    print timer(list_append3, (n,), repetitions=rep)
    print timer(list_chunk3,  (n,), repetitions=rep)


def call_tests(rep, x, y, z):

    try:
        from call import loop, fempty, fwconsts, flops
        fempty.__name__ = 'empty_func in F77'
        fwconsts.__name__ = 'func_with_consts in F77'
    except:
        print 'Run f2py -c -m call call.f'
        sys.exit(1)

    def empty_func(x, y, z):
        pass

    def func_with_consts1(x, y, z):
        a = 0.3
        b = 1.2
        c = 1.22E+02
        q = a*x + b*y + c*z
        return q
    
    def func_with_consts2(x, y, z, a=0.3, b=1.2, c=1.22E+02):
        q = a*x + b*y + c*z
        return q

    def func_with_consts3(x, y, z):
        # hardcoded coefficients
        q = 0.3*x + 1.2*y + 1.22E+02*z
        return q

    def _help(x):
        return x+1
    
    def func_loop_with_call(n):
        r = 0.1
        for i in xrange(n):
            r = _help(r)

    def func_loop_with_inline(n):
        r = 0.1
        for i in xrange(n):
            r = r + 1

            
    # test NumPy vs math sin for scalar arguments:
    # see sin_comparison.py
    
    print '\n*** Testing function calls ***\n'

    fclass1 = """
class MyFunc:
    def __call__(self, x):
        return 2.0
f = MyFunc()
fm = f.__call__
"""

    fclass3 = """
from math import sin
class MyFunc:
    def __call__(self, x, y, z):
        return sin(x)*sin(y)*sin(z)
f = MyFunc()
"""

    setup = """
from py4cs.numpytools import wrap2callable
from math import sin
f = wrap2callable"""
    t1 = timeit.Timer('f(0.9)', setup=setup+'(2.0)').timeit(rep)
    t2 = timeit.Timer('f(0.9)', setup=setup+'(lambda x: 2.0)').timeit(rep)
    t3 = timeit.Timer('f(0.9)', setup=setup+'("2.0")').timeit(rep)
    t4 = timeit.Timer('f(0.9)', setup=fclass1).timeit(rep)
    t4b = timeit.Timer('fm(0.9)', setup=fclass1).timeit(rep)
    t5 = timeit.Timer('f(0.9)', setup='def f(x): return 2.0').timeit(rep)
    t6 = timeit.Timer('f(0.9, 0.1, 1)', setup=setup+'(2.0)').timeit(rep)
    t7 = timeit.Timer('f(0.9, 0.1, 1)', setup=setup+'(lambda x,y,z: 2.0)').timeit(rep)
    t8 = timeit.Timer('f(0.9, 0.1, 1)', setup=setup+'("2.0")').timeit(rep)
    t9 = timeit.Timer('f(1,1,1)',
         setup=setup+'(lambda x,y,z: sin(x)*sin(y)*sin(z))').timeit(rep)
    t10 = timeit.Timer('f(1,1,1)',
         setup=setup+'("sin(x)*sin(y)*sin(z)", ' + \
                      'independent_variables=("x","y","z"))').timeit(rep)
    t11 = timeit.Timer('f(1,1,1)', setup=fclass3).timeit(rep)
    best = min(t1, t2, t3, t4, t5, t6, t7, t8, t9 ,t10, t11)
    best3 = min(t9, t10, t11)
    print """
overhead with wrap2callable: constant function 2.0      (best=%f)
f = wrap2callable(2.0);  f(0.9)                         %.2f  const
f = wrap2callable(lambda x: 2.0);  f(0.9)               %.2f  func
f = wrap2callable("2.0");  f(0.9)                       %.2f  StringFunction
function object                                         %.2f 
%s
function object f: fm = f.__call__, fm(0.9)             %.2f 
def f(x): return 2.0                                    %.2f  func

increasing the number of arguments:
f = wrap2callable(2.0);  f(0.9, 0.1, 1)                 %.2f  const
f = wrap2callable(lambda x,y,z: 2.0);  f(0.9, 0.1, 1)   %.2f  func
f = wrap2callable("2.0");  f(0.9, 0.1, 1)               %.2f  StringFunction

f = wrap2callable(lambda x,y,z: sin(x)*sin(y)*sin(z))   %.2f  %.2f
f = wrap2callable("sin(x)*sin(y)*sin(z)");  f(1,1,1)    %.2f  %.2f
function object                                         %.2f  %.2f
%s
""" % (best, t1/best, t2/best, t3/best, t4/best, fclass1, t4b/best,
       t5/best, t6/best, t7/best, t8/best, t9/best, t9/best3, 
       t10/best, t10/best3, t11/best, t11/best3, fclass3)

    # F77 versions:
    print timer(empty_func, (x, y, z), repetitions=rep)
    f77rep = 100
    c = timer(loop, (f77rep*rep, 'fempty'), repetitions=1,
              comment='loop over fempty in  F77:')
    print c/float(f77rep*rep)  # time for a single call
    print timer(fwconsts, (x, y, z), repetitions=rep)
    c = timer(loop, (f77rep*rep, 'fwconsts'), repetitions=1,
              comment='loop over fwconsts in F77:')
    print c/float(f77rep*rep)

    print timer(empty_func, (x, y, z), repetitions=rep, comment='no body:')
    print timer(func_with_consts1, (x, y, z), repetitions=rep,
                comment='constants in statements:')
    print timer(func_with_consts2, (x, y, z), repetitions=rep,
                comment='constants as default kwargs:')
    print timer(func_with_consts3, (x, y, z), repetitions=rep,
                comment='constants hardcoded:')

    print timer(func_loop_with_call, (rep,), repetitions=1,
                comment='loop with function call:')

    print timer(func_loop_with_inline, (rep,), repetitions=1,
                comment='loop with inline expression:')


    m = 10*rep
    t1 = timeit.Timer('myfunc(2)', setup='def myfunc(x): return x').timeit(m)
    t2 = timeit.Timer('isinstance(x,list)', setup='x=(1,2,3)').timeit(m)
    print 'isinstance is %.2f times slower than a trivial func' % (t2/t1)
    
    call_nargs_test(rep)

    """
    Python 2.3 on laptop IBM X30:
    a function call costs about 3 flops
    calling empty_func and func_with_consts gives compatible results
    a sin(x) call is as fast as 3 flops
    """

def generate_func_with_many_args(n):
    code = """
def func_with_many_args(%s):
    return True
""" % ', '.join(['a%d' % i for i in range(1,n+1)])
    return code

def call_nargs_test(rep):
    for n in range(1,101,20):
        code = generate_func_with_many_args(n)
        exec code in globals(), globals()
        print timer(func_with_many_args, tuple(range(n)), repetitions=rep,
                comment='empty func with %d arguments:' % n)

    
def flop_tests(n):
    """
    Test the efficiency of floating point operations: one multiplication
    per pass in a loop 'for i in xrange(n)'.
    """
    try:
        from call import loop, fempty, fwconsts, flops
        fempty.__name__ = 'empty_func in F77'
        fwconsts.__name__ = 'func_with_consts in F77'
    except:
        print 'Run f2py -c -m call call.f'
        sys.exit(1)


    def empty_loop(n):
        for i in xrange(n):
            pass
        
    def flops_py(n):
        b = 1.0000001
        a = 1.1
        for i in xrange(n):
            a = a*b
        return a

    print '\n\n*** Multiplication test ***\n'
    t1 = timeit.Timer('a*b*c', setup='a=1.01; b=0.98; c=0.99').timeit(n)
    print n, 'multiplications in a loop'
    t2 = timer(flops, (n,), repetitions=100, comment='F77:')
    # result in F77 is multiplication _with_ loop
    best = min(t1, t2)
    print 'multiplication: python=%.2f F77=%.2f' % (t1/best, t2/best)


def matrixfill_tests(language, n):

    from math import sin, exp
    if language == 'F77':
        try:
            from matrix_f77 import makematrix, set, tonumpy, adump, \
                 fill1, fill2, lfill1, lfill2
        except:
            print 'Run f2py -c m matrix matrix_f77.f'
            sys.exit(1)
        makematrix(n, n)  # make matrix in F77
    elif language == 'C++':
        try:
            from matrix_cpp import Matrix
            from _matrix_cpp import Matrix_set
            import _matrix_cpp  # for efficiency comparison
        except:
            print 'run make_cpp.sh'
            sys.exit(1)
        m = Matrix(n)

    a = zeros((n, n), Float)

    def setmatrix1_py():
        """Fill NumPy matrix in Python loop."""
        for i in xrange(n):
            for j in xrange(n):
                a[i, j] = i*j-2
        return a

    def setmatrix2_py():
        """Fill NumPy matrix in Python loop; sin/exp formula."""
        for i in xrange(n):
            x = i*0.1
            for j in xrange(n):
                y = j*0.1
                a[i, j] = sin(x)*sin(y)*exp(-x*y)
        return a

    #======== F77 functions =========

    def setmatrix1_f_index():
        """Fill F77 matrix in a Python loop with F77 indexing."""
        for i in xrange(n):
            for j in xrange(n):
                set(i, j, i*j-2)
        r = tonumpy(n, n)
        # could perhaps tune the interface file such that tonumpy
        # doesn't need arguments
        return r

    def setmatrix2_f_index():
        """Fill F77 matrix in a Python loop with F77 indexing; sin/exp."""
        for i in xrange(n):
            x = 0.1*i
            for j in xrange(n):
                y = 0.1*j
                set(i, j, sin(x)*sin(y)*exp(-x*y))
        r = tonumpy(n, n)
        return r

    def setmatrix1_f_loop1():
        """Fill F77 matrix in Fortran loops."""
        fill1()  # all loops in F77
        r = tonumpy(n, n)
        return r

    def setmatrix1_f_loop2():
        """Fill NumPy matrix in Fortran loops."""
        r = lfill1(a)  # all loops in F77, fill NumPy array
        return r

    def setmatrix2_f_loop1():
        """Fill F77 matrix in Fortran loops; sin/exp formula."""
        fill2()  # all loops in F77
        r = tonumpy(n, n)
        return r

    def setmatrix2_f_loop2():
        """Fill NumPy matrix in Fortran loops; sin/exp formula."""
        r = lfill2(a)  # all loops in F77, fill NumPy array
        return r

    #======== C++ functions =========

    def setmatrix1_c_index1():
        """Fill C++ matrix in a Python loop with F77 indexing."""
        for i in xrange(n):
            for j in xrange(n):
                m.set(i, j, i*j-2)
        # could perhaps tune the interface file such that tonumpy
        # doesn't need arguments
        return m

    def setmatrix2_c_index1():
        """Fill F77 matrix in a Python loop with F77 indexing; sin/exp."""
        for i in xrange(n):
            x = 0.1*i
            for j in xrange(n):
                y = 0.1*j
                m.set(i, j, sin(x)*sin(y)*exp(-x*y))
        return m

    def setmatrix1_c_index3():
        """Avoid proxy class, call Matrix_set directly."""
        for i in xrange(n):
            for j in xrange(n):
                Matrix_set(m, i, j, i*j-2)
        # could perhaps tune the interface file such that tonumpy
        # doesn't need arguments
        return m

    def setmatrix2_c_index3():
        """Avoid proxy class, call Matrix_set directly; sin/exp formula."""
        for i in xrange(n):
            x = 0.1*i
            for j in xrange(n):
                y = 0.1*j
                Matrix_set(m, i, j, sin(x)*sin(y)*exp(-x*y))
        return m

    def setmatrix1_c_index4():
        """Avoid proxy class, call _matrix_cpp.Matrix_set directly."""
        for i in xrange(n):
            for j in xrange(n):
                _matrix_cpp.Matrix_set(m, i, j, i*j-2)
        # could perhaps tune the interface file such that tonumpy
        # doesn't need arguments
        return m

    def setmatrix2_c_index4():
        """Avoid proxy class, call _matrix_cpp.Matrix_set directly."""
        for i in xrange(n):
            x = 0.1*i
            for j in xrange(n):
                y = 0.1*j
                _matrix_cpp.Matrix_set(m, i, j, sin(x)*sin(y)*exp(-x*y))
        return m


    def setmatrix1_c_loop1():
        """Fill F77 matrix in Fortran loops."""
        m.fill1()  # all loops in F77
        return m

    def setmatrix2_c_loop1():
        """Fill F77 matrix in Fortran loops; sin/exp formula."""
        m.fill2()  # all loops in F77
        return m


    #======== end of C++ functions =========

    def sort(d):
        """Sort result dictionary: d[problem_description]=time."""
        list = [(key, d[key]) for key in d]
        def s(a, b):
            """sort list of 2-tuples"""
            return cmp(a[1],b[1])  # a,b = (comment,time)
        list.sort(s)
        return list
        
    if language == 'F77':
        res = {}
        # one multiplication in Python for each matrix entry:
        t = timer(setmatrix1_py, (), repetitions=10)
        res['Python loop and NumPy array'] = t
        t = timer(setmatrix1_f_index , (), repetitions=10)
        res['Python loop and F77 indexing in F77 array'] = t
        t = timer(setmatrix1_f_loop1, (), repetitions=100)
        res['F77 loop over F77 array'] = t
        t = timer(setmatrix1_f_loop2, (), repetitions=100)
        res['F77 loop over NumPy array'] = t
        res = sort(res)
        print '\n\n\nTable: a[i,j] = i*j-2\n(one mult+sub per iteration)\n'
        for comment, time in res:
            print '%60s %7.3f' % (comment,time)
        print '\n\n'

        # a sin/exp function expression for each matrix entry:
        res = {}
        t = timer(setmatrix2_py, (), repetitions=10)
        res['Python loop and NumPy array'] = t
        t = timer(setmatrix2_f_index , (), repetitions=10)
        res['Python loop and F77 indexing in F77 array'] = t
        t = timer(setmatrix2_f_loop1, (), repetitions=100)
        res['F77 loop over F77 array'] = t
        t = timer(setmatrix2_f_loop2, (), repetitions=100)
        res['F77 loop over NumPy array'] = t
        res = sort(res)
        print '\n\n\nTable: a[i,j] = sin/exp expression\n'
        for comment, time in res:
            print '%60s %7.3f' % (comment,time)
        print '\n\n'

    elif language == 'C++':
        res = {}
        # one multiplication in Python for each matrix entry:
        t = timer(setmatrix1_py, (), repetitions=10)
        res['Python loop and NumPy array'] = t
        t = timer(setmatrix1_c_index1, (), repetitions=10)
        res['Indexing: m.set'] = t
        t = timer(setmatrix1_c_index3, (), repetitions=10)
        res['Indexing: Matrix_set'] = t
        t = timer(setmatrix1_c_index4, (), repetitions=10)
        res['Indexing: matrix_cpp.Matrix_set'] = t
        t = timer(setmatrix1_c_loop1, (), repetitions=100)
        res['C++ loop over C++ array'] = t
        res = sort(res)
        print '\n\n\nTable: a[i,j] = i*j-2\n(one mult+sub per iteration)\n'
        for comment, time in res:
            print '%60s %7.3f' % (comment,time)
        print '\n\n'

        # a sin/exp function expression for each matrix entry:
        res = {}
        t = timer(setmatrix2_py, (), repetitions=10)
        res['Python loop and NumPy array'] = t
        t = timer(setmatrix2_c_index1, (), repetitions=10)
        res['Indexing: m.set'] = t
        t = timer(setmatrix2_c_index3, (), repetitions=10)
        res['Indexing: Matrix_set'] = t
        t = timer(setmatrix2_c_index4, (), repetitions=10)
        res['Indexing: matrix_cpp.Matrix_set'] = t
        t = timer(setmatrix2_c_loop1, (), repetitions=100)
        res['C++ loop over C++ array'] = t
        res = sort(res)
        print '\n\n\nTable: a[i,j] = sin/exp-expression\n'
        for comment, time in res:
            print '%60s %7.3f' % (comment,time)
        print '\n\n'

    

def loop_vs_NumPy_tests(n):
    """
    Compare a loop with sin or i+2 computations in pure Python and NumPy.
    """

    def py_loop1_sin(x):
        from math import sin  # scalar sin
        for i in xrange(len(x)):
            x[i] = sin(x[i])
        return x

    def py_loop2_sin(x):
        from py4cs.numpytools import sin  # vector sin (inefficient!)
        for i in xrange(len(x)):
            x[i] = sin(x[i])
        return x


    def I(x):
        # from math import sin # this is expensive: from 70 to 16!
        return sin(x)
    
    def py_loop3_sin(x):
        for i in xrange(len(x)):
            x[i] = I(x[i])
        return x

    def NumPy_loop_sin(x):
        from py4cs.numpytools import sin
        x = sin(x)
        return x


    def py_loop1_sincos_x2(x):
        from math import sin, cos, pow  # scalar sin
        for i in xrange(len(x)):
            x[i] = sin(x[i])*cos(x[i]) + x[i]**2
        return x

    def py_loop2_sincos_x2(x):
        from py4cs.numpytools import sin, cos
        for i in xrange(len(x)):
            x[i] = sin(x[i])*cos(x[i]) + x[i]**2
        return x

    def py_loop2b_sincos_x2(x):
        from math import sin, cos  # scalar sin
        for i in xrange(len(x)):
            x[i] = sin(x[i])*cos(x[i]) + x[i]**2
        return x

    def I2(x):
        # from math import sin # this is expensive: from 70 to 16!
        return sin(x)*cos(x) + x**2
    
    def py_loop3_sincos_x2(x):
        for i in xrange(len(x)):
            x[i] = I2(x[i])
        return x

    def py_loop4_sincos_x2(x):
        from math import sin, cos
        for i in xrange(len(x)):
            xi = x[i]
            x[i] = sin(xi)*cos(xi) + xi**2
        return x

    def NumPy_loop_sincos_x2(x):
        from py4cs.numpytools import sin, cos
        x = sin(x)*cos(x) + x**2
        return x


    def py_loop1_ip2(x):
        from math import sin  # scalar sin
        for i in xrange(len(x)):
            x[i] = sin(x[i])
        return x

    def NumPy_loop1_ip2(x):
        x = arange(2, n+2, 1, Float)
        return x

    def NumPy_loop2_ip2(x):
        x = fromfunction(lambda i: i+2, (len(x),))
        return x

    def py_loop1_2Dsincos(x, y):
        u = zeros((len(x),len(y)), Float)
        from math import sin as msin, cos as mcos

        def I(x, y):
            return msin(x)*mcos(y)

        # x[i], y[j]: coordinates of grid point (i,j)
        for i in xrange(len(x)):
            for j in xrange(len(y)):
                u[i,j] = I(x[i], y[j])
        return u

    def py_loop2_2Dsincos(x, y):
        # inlined expressions
        u = zeros((len(x),len(y)), Float)
        from math import sin as msin, cos as mcos

        # x[i], y[j]: coordinates of grid point (i,j)
        for i in xrange(len(x)):
            for j in xrange(len(y)):
                u[i,j] = msin(x[i])*mcos(y[j])
        return u

    def py_loop3_2Dsincos(x, y):
        # reverse the order of traversal
        u = zeros((len(x),len(y)), Float)
        from math import sin as msin, cos as mcos

        # x[i], y[j]: coordinates of grid point (i,j)
        for j in xrange(len(y)):
            for i in xrange(len(x)):
                u[i,j] = msin(x[i])*mcos(y[j])
        return u

    def NumPy_loop1_2Dsincos(x, y):
        xv = x[:, NewAxis]
        yv = y[NewAxis, :]

        def I3(x, y):
            return sin(x)*cos(y)

        u = I3(xv, yv)
        return u
        

    def py_loop1_manyarit(x):
        from math import sin, cos
        for i in xrange(len(x)):
            x[i] = sin(x[i])*cos(x[i]) + sin(2*x[i])*cos(2*x[i]) + \
                   sin(3*x[i])*cos(3*x[i]) + \
                   sin(4*x[i])*cos(4*x[i]) + sin(5*x[i])*cos(5*x[i]) 
        return x

    def NumPy_loop1_manyarit(x):
        from py4cs.numpytools import sin, cos, amax
        x = sin(x)*cos(x) + sin(2*x)*cos(2*x) + \
            sin(3*x)*cos(3*x) + \
            sin(4*x)*cos(4*x) + sin(5*x)*cos(5*x) 
        return x

    try:
        from call import sinloop as F77_loop_sin, \
             ip2loop as F77_loop_ip2, \
             sincosloop as F77_loop_sincos_x2, \
             gridloop2d1 as F77_loop1_2Dsincos, \
             gridloop2d2 as F77_loop2_2Dsincos, \
             gridloop2d3 as F77_loop3_2Dsincos, \
             manyarit as F77_loop_manyarit
        
        F77_loop_sin.__name__ = 'F77_loop_sin'
        F77_loop_ip2.__name__ = 'F77_loop_ip2'
        F77_loop_sincos_x2.__name__ = 'F77_loop_sincos_x2'
        F77_loop_manyarit.__name__ = 'F77_loop_manyarit'
        F77_loop1_2Dsincos.__name__ = 'F77_loop1_2Dsincos'
        F77_loop2_2Dsincos.__name__ = 'F77_loop2_2Dsincos'
        F77_loop3_2Dsincos.__name__ = 'F77_loop3_2Dsincos'
    except Exception, msg:
        print 'import error (from call import ...):', msg
        print 'Run f2py -c -m call call.f'
        sys.exit(1)


    # 2D grid:
    print '\n\n'
    m0 = sqrt(n)
    #m0 = 1600
    for j in (4, 2, 1):
        m = m0/j
        print '\n\ninitializing a %dx%d array\n' % (m,m)
        x = seq(0, 1, 1/float(m-1))
        y = x.copy()
        u = zeros((len(x), len(y)), Float)
        t1 = timer(py_loop3_2Dsincos, args=(x,y), repetitions=1*j)
        t1 = timer(py_loop2_2Dsincos, args=(x,y), repetitions=1*j)
        t1 = timer(py_loop1_2Dsincos, args=(x,y), repetitions=1*j)
        print 'pure Python loop:%d u[i,j]=sin(x[i])*cos(y[j]):' % size(u), t1
        from py4cs.numpytools import sin, cos  # ensure vectorized versions
        t2 = timer(NumPy_loop1_2Dsincos, args=(x,y), repetitions=20*j)
        print 'NumPy:%d u=sin(x)*cos(y):' % size(u), t2
        # numarray does not work 100% with f2py:
        if not isinstance(u, NumArray):
            import call
            u = call.as_column_major_storage(u)
            t3a = timer(F77_loop1_2Dsincos, args=(u,x,y), repetitions=20*j,
                        comment='call I1')
            t3b = timer(F77_loop2_2Dsincos, args=(u,x,y), repetitions=20*j,
                        comment='inline')
            t3c = timer(F77_loop3_2Dsincos, args=(u,x,y), repetitions=20*j,
                        comment='3 loops')
            #v1 = NumPy_loop1_2Dsincos(x,y)
            #v2 = F77_loop_2Dsincos(u, x, y)
            #print 'difference v1-v2', size(v1-v2), amax(v1-v2), amin(v1-v2)
            print 'corresponing Fortran loop:', t3a, t3b, t3c
            t3 = min(t3a, t3b, t3c)
            print 'summary:', t1/t3, t2/t3, '1.0'
        print 'NumPy is', t1/t2, 'times faster than pure Python'

    x = seq(0, 1, 1/float(n-1))

    # 5 combinations of sin(x)*cos(x)
    # (NumPy vectorized code is less efficient than Fortran now because
    # there are so many calls to C functions and 
    print '\n\n'
    t1 = timer(py_loop1_manyarit, args=(x,), repetitions=1)
    print 'pure Python loop 1:%d x[i]=5 sin(x[i])*cos(x[i]) terms:' % n, t1
    print 'x max:', amax(x)
    from py4cs.numpytools import sin, cos
    t2 = timer(NumPy_loop1_manyarit, args=(x,), repetitions=4)
    print 'corresponing NumPy expression x=5 terms sin(x)*cos(x):', t2
    t3 = timer(F77_loop_manyarit, args=(x,), repetitions=20)
    print 'corresponing Fortran loop:', t3
    print 'NumPy is %d times faster than plain loops' % (t1/t2)
    print 'summary: %g %g %g' % (t1/t3, t2/t3, 1.0)

    
    # sin(x):
    print '\n\n'
    t1 = timer(py_loop1_sin, args=(x.tolist(),), repetitions=1)
    print 'pure Python loop 1:%d x[i]=sin(x[i]), x is list, scalar math.sin:' % n, t1
    t1 = timer(py_loop1_sin, args=(x,), repetitions=1)
    print 'pure Python loop 1:%d x[i]=sin(x[i]), x is array, scalar math.sin:' % n, t1
    t1b = timer(py_loop2_sin, args=(x,), repetitions=1)
    print 'pure Python loop 1:%d x[i]=sin(x[i]), NumPy vector sin:' % n, t1b
    t2 = timer(NumPy_loop_sin, args=(x,), repetitions=20)
    print 'corresponing NumPy expression x=sin(x):', t2
    from math import sin  # scalar sin
    t1c = timer(py_loop3_sin, args=(x,), repetitions=1)
    print 'pure Python loop 1:%d x[i]=I(x[i]), I is sin(x):' % n, t1c
    t3 = timer(F77_loop_sin, args=(x,), repetitions=20)
    print 'corresponing Fortran loop:', t3
    print 'summary:', t1/t3, t2/t3, '1.0'
    print 'NumPy is', t1/t2, 'times faster than pure Python'
    print 'NumPy sin (instead of math.sin):', t1b/t3
    print 'calling I(x[i]):', t1c/t3

    # sin(x)*cos(x) + x**2
    print '\n\n'
    t1 = timer(py_loop2b_sincos_x2, args=(x.tolist(),), repetitions=1)
    print 'pure Python loop 1:%d x[i]=sin(x[i])*cos(x[i])+x[i]*x[i]:' % n, t1
    t1 = timer(py_loop2_sincos_x2, args=(x.tolist(),), repetitions=1)
    print 'pure Python loop 1:%d x[i]=sin(x[i])*cos(x[i])+x[i]*x[i] with NumPy sin, cos, power:' % n, t1
    t1 = timer(py_loop1_sincos_x2, args=(x.tolist(),), repetitions=1)
    print 'pure Python loop 1:%d x[i]=sin(x[i])*cos(x[i])+x[i]**2, x is list, scalar math.sin:' % n, t1
    t1 = timer(py_loop1_sincos_x2, args=(x,), repetitions=1)
    print 'pure Python loop 1:%d x[i]=sin(x[i])*cos(x[i])+x[i]**2, x is array, scalar math.sin:' % n, t1
    t2 = timer(NumPy_loop_sincos_x2, args=(x,), repetitions=20)
    print 'corresponing NumPy expression x=sin(x)*cos(x)+x**2:', t2
    from math import sin, cos  # scalar sin, cos
    t1c = timer(py_loop3_sincos_x2, args=(x,), repetitions=1)
    print 'pure Python loop 1:%d x[i]=I2(x[i]), I is sin(x)*cos(x[i])+x**2:' % n, t1c
    t1b = timer(py_loop4_sincos_x2, args=(x,), repetitions=1)
    print 'pure Python loop 1:%d xi=x[i]; x[i]=sin(xi)*cos(xi)+xi**2:' % n, t1b
    t3 = timer(F77_loop_sincos_x2, args=(x,), repetitions=20)
    print 'corresponing Fortran loop:', t3
    print 'summary:', t1/t3, t2/t3, '1.0'
    print 'NumPy is', t1/t2, 'times faster than pure Python'
    print 'xi=x[i] trick:', t1b/t3, t1b
    print 'calling I2(x[i]):', t1c/t3

    # i+2:
    print '\n\n'
    t1 = timer(py_loop1_ip2, args=(x.tolist(),), repetitions=1)
    print 'pure Python loop 1:%d x[i]=i+2, x is list:' % n, t1
    t1 = timer(py_loop1_ip2, args=(x,), repetitions=1)
    print 'pure Python loop 1:%d x[i]=i+2, x is array:' % n, t1
    t2 = timer(NumPy_loop1_ip2, args=(x,), repetitions=20)
    print 'corresponing NumPy expression x=arange:', t2
    t2 = timer(NumPy_loop1_ip2, args=(x,), repetitions=20)
    print 'corresponing NumPy expression x=fromfunction(lambda; i i+2):', t2
    t3 = timer(F77_loop_ip2, args=(x,), repetitions=20)
    print 'corresponing Fortran loop:', t3
    print 'summary:', t1/t3, t2/t3, '1.0'
    print 'NumPy is', t1/t2, 'times faster than pure Python'

    
def exception_test(n):
    setup1 = """
from math import sqrt
def compute(x):
    try:
        return sqrt(x)
    except:
        return 0.0
"""
    setup2 = """
from math import sqrt
def compute(x):
    if x > 0:
        return sqrt(x)
    else:
        return 0.0
 """
    t1 = timeit.Timer('compute(-1.1)', setup=setup1).timeit(n)
    t2 = timeit.Timer('compute(-1.1)', setup=setup2).timeit(n)
    best = min(t1, t2)
    print '%.3f   %.1f %.1f' % (best, t1/best, t2/best)

    bigdict = {}
    for i in range(1000):
        bigdict[str(i)] = i
    bigdict = 'd=' + str(bigdict)

    setup1 = bigdict + """
def compute(x):
    try:
        return x['f']
    except:
        return 0.0
"""
    setup2 = bigdict + """
def compute(x):
    if 'f' in x:
        return x['f']
    else:
        return 0.0
"""
    setup3 = bigdict + """
def compute(x):
    return x.get('f', 0.0)
"""
    t1 = timeit.Timer('compute(d)', setup=setup1).timeit(n)
    t2 = timeit.Timer('compute(d)', setup=setup2).timeit(n)
    t3 = timeit.Timer('compute(d)', setup=setup3).timeit(n)
    best = min(t1, t2, t3)
    print '%.3f   %.1f %.1f %.1f' % (best, t1/best, t2/best, t3/best)
    

def grep_tests(filesize):
    """
    Test the efficiency of a grep operation on a file with
    size filesize megabytes.
    Compare Python, Perl, and Unix grep (in C).
    """
    from generate_text import generate
    generate(filesize, filename='tmp.dat')

    # run os.system commands
    py = os.path.join(os.environ['scripting'],'exercises','grep.py')
    pl_nice = os.path.join(os.environ['scripting'],'src','perl','grep1.pl')
    pl_dollar_underscore = \
        os.path.join(os.environ['scripting'],'src','perl','grep2.pl')
    pl_grep = os.path.join(os.environ['scripting'],'src','perl','grep4.pl')
    unix = 'grep -H -n'
    pattern = '000000761'
    pattern = repr(r'\s+0+000[0AZBfq][7_/]61\s+')  # add quotes for system cmd
    timer_system(py + ' ' + pattern + ' tmp.dat', comment='plain Python:')
    timer_system(pl_nice + ' ' + pattern + ' tmp.dat', comment='plain Perl:')
    timer_system(pl_dollar_underscore + ' ' + pattern + ' tmp.dat', comment='Perl w/$_:')
    timer_system(pl_grep + ' ' + pattern + ' tmp.dat', comment='Perl grep:')
    timer_system(unix + ' ' + pattern + ' tmp.dat', comment='Unix grep:')
    os.remove('tmp.dat')
    
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Usage: %s test-type\ntypes: allocate range call flops matrixfill vectorization exception grep" \
              % sys.argv[0]
        sys.exit(1)
    for test_tp in sys.argv[1:]:
        print '\n\n'
        if test_tp == 'allocate':
            allocate_tests(1000000)
        elif test_tp == 'range':
            memory = 512000000
            vector_length = int(memory/8.0/2*0.9)/10
            range_tests(vector_length)
        elif test_tp == 'call':
            call_tests(5000000, 0.1, -0.1, 1.0)
        elif test_tp == 'flops':
            flop_tests(20000000)
        elif test_tp == 'matrixfill_f77':
            matrixfill_tests('F77', 1000)
        elif test_tp == 'matrixfill_Cpp':
            matrixfill_tests('C++', 1000)
        elif test_tp == 'grep':
            grep_tests(120)
        elif test_tp == 'vectorization':
            #loop_vs_NumPy_tests(5000000)
            loop_vs_NumPy_tests(1000000)
        elif test_tp == 'exception':
            exception_test(100000)
        else:
            print test_tp, 'not implemented'
