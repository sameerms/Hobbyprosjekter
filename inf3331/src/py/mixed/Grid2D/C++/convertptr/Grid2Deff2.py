#!/usr/bin/env python
# as Grid2Deff.py but explicit conversion between NumPy objects
# and MyArray objects are performed (via SWIG pointer exchange).

from Numeric import *
import time, sys, Gnuplot, os
# make sys.path so we can find Grid2D.py:
sys.path.insert(0, os.path.join(os.environ['scripting'],
                                'src','py','examples'))
from Grid2D import Grid2D
# put . in sys.path so we can find ext_gridloop
# (this script is run from a subdir):
sys.path.insert(0, os.curdir)
import ext_gridloop

# load ../../Grid2Deff.py:
sys.path.insert(0, os.path.join(os.pardir, os.pardir))
from Grid2Deff import f1
               
class Grid2Deff2(Grid2D):
    def __init__(self,
                 xmin=0, xmax=1, dx=0.5,
                 ymin=0, ymax=1, dy=0.5):
        Grid2D.__init__(self, xmin, xmax, dx, ymin, ymax, dy)
        self.c = ext_gridloop.Convert_MyArray()
        
    def ext_gridloop1(self, f):
        """Compute a[i,j] = f(xi,yj) in an external routine."""
        lx = size(self.xcoor);  ly = size(self.ycoor)
        a = zeros((lx,ly), Float)
        try:  # are we in Fortran?
            a = ext_gridloop.as_column_major_storage(a)
        except:
            pass
        if isinstance(f, str):
            f_compiled = compile(f, '<string>', 'eval')
            def f_str(x, y):
                return eval(f_compiled)
                #return eval(f)  # much slower
            func = f_str
        else:
            func = f
        a_p = self.c.py2my(a)
        x_p = self.c.py2my(self.xcoor)
        y_p = self.c.py2my(self.ycoor)
        f_p = self.c.set_pyfunc(func)
        ext_gridloop.gridloop1(a_p, x_p, y_p, f_p)
        return a

    def ext_gridloop2(self, f):
        """Compute a[i,j] = f(xi,yj) in an external routine."""
        if isinstance(f, str):
            f_compiled = compile(f, '<string>', 'eval')
            def f_str(x, y):
                return eval(f_compiled)
                #return eval(f)
            func = f_str
        else:
            func = f
        x_p = self.c.py2my(self.xcoor)
        y_p = self.c.py2my(self.ycoor)
        f_p = self.c.set_pyfunc(func)
        a_p = ext_gridloop.gridloop2(x_p, y_p, f_p)
        a = self.c.my2py(a_p)
        return a

    def ext_gridloop_exceptions(self, f):
        """Test error handling in the extension module."""
        x_p = self.c.py2my(self.xcoor)
        y_p1 = self.c.py2my(self.ycoor[1:])
        f_p = self.c.set_pyfunc(f)
        try: #1
            ext_gridloop.gridloop1((1,2), x_p, y_p1, f_p)
        except: 
            print sys.exc_type, sys.exc_value
        try: #2
            ext_gridloop.gridloop1(x_p, x_p, y_p1, f_p)
        except:
            print sys.exc_type, sys.exc_value
        try: #3
            ext_gridloop.gridloop2(x_p, y_p, 'abc')
        except:
            print sys.exc_type, sys.exc_value
        try: #4
            # cannot be handled by this interface...
            #ext_gridloop.gridloop2(array(self.xcoor,Complex64),
            #                       self.ycoor, 'abc')
            pass
        except:
            print sys.exc_type, sys.exc_value
        try: #5
            # cannot be handled by this interface...
            #ext_gridloop.gridloop2(array([[0,0],[1,2]]), self.ycoor, 'abc')
            pass
        except:
            print sys.exc_type, sys.exc_value

    def dump(self, a):
        """Nice printout of a 2D array a."""
        for i in xrange(a.shape[0]):
            for j in xrange(a.shape[1]):
                print 'value at (%g,%g)  \t = a[%d,%d] = %g' % \
                      (self.xcoor[i], self.ycoor[j], i, j, a[i,j])


def verify1():
    g = Grid2Deff2(dx=0.5, dy=1)
    f_exact = g(f1)  # NumPy computation
    f = g.ext_gridloop1(f1)
    print 'f computed by external gridloop1 function:\n', f
    if allclose(f, f_exact, atol=1.0E-10, rtol=1.0E-12):
        print 'f is correct'
    f = g.ext_gridloop2(f1)
    print 'f computed by external gridloop2 function:\n', f
    if allclose(f, f_exact, atol=1.0E-10, rtol=1.0E-12):
        print 'f is correct'

    # check printing:
    print 'array seen from Python:'
    g.dump(f)
    if 'dump' in dir(ext_gridloop):
        print 'array seen from Fortran (transposed, but right values):'
        ext_gridloop.dump(f, g.xcoor, g.ycoor)
    
def timing2(n=2000):
    dx = 1.0/n
    g = Grid2Deff2(dx=dx, dy=dx)

    # here we use straight NumPy sin in a scalar context:
    def myfunc(x, y):
        return sin(x*y) + 8*x
    expression = 'sin(x*y) + 8*x'
    # here we use math.sin (=mathsin, global variable):
    def myfunc(x, y):
        return mathsin(x*y) + 8*x
    expression = 'mathsin(x*y) + 8*x'

    import time
    print 'starting up g.ext_gridloop1(myfunc)....'
    t0 = time.clock()
    f = g.ext_gridloop1(myfunc)
    t1 = time.clock()
    print 'g.ext_gridloop1(myfunc):', t1-t0
    f = g.ext_gridloop2(myfunc)
    t2 = time.clock()
    print 'g.ext_gridloop2(myfunc):', t2-t1
    f = g.ext_gridloop2(expression)
    t3 = time.clock()
    print 'g.ext_gridloop2(expression):', t3-t2
    print """
Results using an extension module (%dx%d grid),
with callback to Python for each point:
gridloop1 (w/func):               %s
gridloop2 (w/func):               %s
gridloop1 (w/string expression):  %s
""" % (n, n, t1-t0, t2-t1, t3-t2)

def exceptions1():
    g = Grid2Deff2(dx=0.5, dy=1)
    def myfunc(x, y):
        return sin(x*y) + 8*x
    g.ext_gridloop_exceptions(myfunc)

def _run():
    try:
        func = sys.argv[1]
    except:
        func = 'verify1'
    if func == 'timing2':
        try:
            n = int(sys.argv[2])
        except:
            n = 2000
        exec 'timing2(%d)' % n
    else:
        exec func + '()' 
    
if __name__ == '__main__':
    _run()
