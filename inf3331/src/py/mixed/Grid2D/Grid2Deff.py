#!/usr/bin/env python

from py4cs.numpytools import *
from math import sin as mathsin  # for efficiency in scalar callback
import time, sys, Gnuplot, os
# make sys.path so we can find Grid2D.py:
sys.path.insert(0, os.path.join(os.environ['scripting'],
                                'src','py','examples'))
from Grid2D import Grid2D
try:
    import ext_gridloop
except ImportError:
    print 'Build ext_gridloop: ./make_module_1.sh'
    sys.exit(1)


class Grid2Deff(Grid2D):
    # Grid2D's constructor is sufficient
    #def __init__(self,
    #             xmin=0, xmax=1, dx=0.5,
    #             ymin=0, ymax=1, dy=0.5):
    #    Grid2D.__init__(self, xmin, xmax, dx, ymin, ymax, dy)
        
    def ext_gridloop1(self, f):
        """Compute a[i,j] = f(xi,yj) in an external routine."""
        # a is made here, sent to the routine, and then returned
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
        ext_gridloop.gridloop1(a, self.xcoor, self.ycoor, func)
        return a

    def ext_gridloop2(self, f):
        """Compute a[i,j] = f(xi,yj) in an external routine."""
        # a is made in the external routine
        if isinstance(f, str):
            f_compiled = compile(f, '<string>', 'eval')
            def f_str(x, y):
                return eval(f_compiled)
                #return eval(f)  # much slower
            func = f_str
        else:
            func = f
        a = ext_gridloop.gridloop2(self.xcoor, self.ycoor, func)
        return a

    def ext_gridloop_exceptions(self, f):
        """Test error handling in the extension module."""
        try: #1
            ext_gridloop.gridloop1((1,2), self.xcoor, self.ycoor[1:], f)
        except: 
            print sys.exc_type, sys.exc_value
        try: #2
            ext_gridloop.gridloop1(self.xcoor, self.xcoor, self.ycoor[1:], f)
        except:
            print sys.exc_type, sys.exc_value
        try: #3
            ext_gridloop.gridloop2(self.xcoor, self.ycoor, 'abc')
        except:
            print sys.exc_type, sys.exc_value
        try: #4
            ext_gridloop.gridloop2(array(self.xcoor,Complex64),
                                   self.ycoor, 'abc')
        except:
            print sys.exc_type, sys.exc_value
        try: #5
            ext_gridloop.gridloop2(array([[0,0],[1,2]]), self.ycoor, 'abc')
        except:
            print sys.exc_type, sys.exc_value

    # NOTE: the three next functions are only available in the
    # Fortran 77 extension module:
    
    def ext_gridloop_vec1(self, f):
        """As ext_gridloop2, but vectorized callback."""
        a = zeros((size(self.xcoor),size(self.ycoor)), Float)
        a = ext_gridloop.gridloop_vec1(a, self.xcoor, self.ycoor, f)
        return a

    def ext_gridloop_vec2(self, f):
        """As ext_gridloop_vec1, but callback to func. w/grid arg."""
        a = zeros((size(self.xcoor),size(self.ycoor)), Float)
        a = ext_gridloop.gridloop_vec2(a, f, func1_extra_args=(self,))
        return a

    def myfuncf3(self, a):
        a[:,:] = myfunc(self.xcoorv, self.ycoorv)  # in-place mod.

    def ext_gridloop_vec3(self, f):
        """As ext_gridloop_vec2, but callback to class method."""
        a = zeros((size(self.xcoor),size(self.ycoor)), Float)
        a = ext_gridloop.gridloop_vec2(a, f)
        return a


    def ext_gridloop2_str(self, f77_name):
        """
        Call an interface to ext_gridloop.gridloop2, which avoids
        callbacks to Python and calls the f77_name F77 function
        instead.
        """
        a = ext_gridloop.gridloop2_str(self.xcoor, self.ycoor,
                                       f77_name)
        return a

    def ext_gridloop2_fcb(self):
        """As ext_gridloop2, but compiled Fortran callback func."""
        import callback
        a = callback.gridloop2_fcb(self.xcoor, self.ycoor)
        return a

    def ext_gridloop2_fcb_compile(self, fstr):
        if not isinstance(fstr, str):
            raise TypeError, \
            'fstr must be string expression, not', type(fstr)
        
        # generate Fortran source
        import f2py2e
        source = """
      real*8 function fcb(x, y)
      real*8 x, y
      fcb = %s
      return
      end

      subroutine gridloop2_fcb(a, xcoor, ycoor, nx, ny)
      integer nx, ny
      real*8 a(nx,ny), xcoor(nx), ycoor(ny)
Cf2py intent(out) a
Cf2py intent(in) xcoor
Cf2py intent(in) ycoor
Cf2py depend(nx,ny) a
      real*8 fcb
      external fcb

      call gridloop2(a, xcoor, ycoor, nx, ny, fcb)
      return
      end
""" % fstr
        # compile callback code and link with ext_gridloop.so:
        f2py_args = "--fcompiler='Gnu' --build-dir tmp2"\
                    " -DF2PY_REPORT_ON_ARRAY_COPY=1 "\
                    " ./ext_gridloop.so"
        r = f2py2e.compile(source, modulename='callback',
                           extra_args=f2py_args, verbose=True,
                           source_fn='_cb.f')
        if r:
            print 'unsuccessful compilation'; sys.exit(1)
        import callback  # see if we can import successfully

    def ext_gridloop2_compile(self, fstr):
        if not isinstance(fstr, str):
            raise TypeError, \
            'fstr must be string expression, not', type(fstr)
        
        # generate Fortran source for gridloop2:
        import f2py2e
        source = """
      subroutine gridloop2(a, xcoor, ycoor, nx, ny)
      integer nx, ny
      real*8 a(nx,ny), xcoor(nx), ycoor(ny)
Cf2py intent(out) a
Cf2py depend(nx,ny) a

      integer i,j
      real*8 x, y
      do j = 1,ny
         y = ycoor(j)
         do i = 1,nx
            x = xcoor(i)
            a(i,j) = %s
         end do
      end do
      return
      end
""" % fstr        
        f2py_args = "--fcompiler='Gnu' --build-dir tmp1"\
                    " -DF2PY_REPORT_ON_ARRAY_COPY=1"
        r = f2py2e.compile(source, modulename='ext_gridloop2',
                           extra_args=f2py_args, verbose=True,
                           source_fn='_cb.f')
        if r:
            print 'unsuccessful compilation'; sys.exit(1)
        import ext_gridloop2  # see if we can import successfully

    def ext_gridloop2_v2(self):
        """
        As ext_gridloop2, but the Fortran gridloop2 function was
        generated and compiled in Python.
        """
        import ext_gridloop2
        return ext_gridloop2.gridloop2(self.xcoor, self.ycoor)

    def dump(self, a):
        """Nice printout of a 2D array a."""
        for i in xrange(a.shape[0]):
            for j in xrange(a.shape[1]):
                print 'value at (%g,%g)  \t = a[%d,%d] = %g' % \
                      (self.xcoor[i], self.ycoor[j], i, j, a[i,j])

def f1(x,y):
    print 'x+2*y =',x+2*y
    return x+2*y

def verify1():
    """Basic test of the extension module."""
    g = Grid2Deff(dx=0.5, dy=1)
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

def myfunc(x, y):
    return sin(x*y) + 8*x

def myfuncf1(a, xcoor, ycoor, nx, ny):
    """Vectorized function to be called from extension module."""
    #print 'myfuncf1; type of args:',type(a),type(xcoor),type(nx)
    x = xcoor[:,NewAxis]
    y = ycoor[NewAxis,:]
    a[:,:] = myfunc(x, y)  # in-place modification of a
    print 'myfuncf1, a=',a

def myfuncf2(a, g):
    """Vectorized function to be called from extension module."""
    #print 'myfuncf2; type of args:',type(a),type(g)
    a[:,:] = myfunc(g.xcoorv, g.ycoorv)  # in-place modification of a


def verify2(n=3):
    """
    Test of some methods in class Grid2Deff that call up
    some F77 routines for improving the efficiency of callbacks
    to Python.
    """
    if not 'gridloop_vec2' in dir(ext_gridloop):
        raise ImportError, 'verify2 works only for F77 module'
    dx = 1.0/n
    g = Grid2Deff(dx=dx, dy=dx)
    a = g.ext_gridloop_vec1(myfuncf1)
    print "g.ext_gridloop_vec1(myfuncf1): a=\n",a
    a = g.ext_gridloop_vec2(myfuncf2)
    print "g.ext_gridloop_vec2(myfuncf2): a=\n",a
    # need f2py version > 2.39 (callback to class method):
    a = g.ext_gridloop_vec3(g.myfuncf3)
    print "g.ext_gridloop_vec3(g.myfuncf3): a=\n",a
    a = g.ext_gridloop2_str('f2')
    print "g.ext_gridloop2_str('f2'): a=\n",a
    a = g.ext_gridloop2_str('myfunc')
    print "g.ext_gridloop_str('myfunc'): a=\n",a
    g.ext_gridloop2_fcb_compile('sin(x*y) + 8*x')
    a = g.ext_gridloop2_fcb()
    print "g.gridloop2_fcb: a=\n",a
    import callback
    print 'contents of callback module:', dir(callback)
    g.ext_gridloop2_compile('sin(x*y) + 8*x')
    a = g.ext_gridloop2_v2()
    print "g.gridloop2_v2: a=\n",a


from py4cs.misc import timer
def timing2(n=2000):
    """Time different implementations of the extension module."""
    dx = 1.0/n
    g = Grid2Deff(dx=dx, dy=dx)
    # here we use straight NumPy sin in a scalar context:
    def myfunc(x, y):
        return sin(x*y) + 8*x
    expression = 'sin(x*y) + 8*x'
    # here we use math.sin (=mathsin, global variable):
    def myfunc(x, y):
        return mathsin(x*y) + 8*x
    expression = 'mathsin(x*y) + 8*x'

    print 'basic NumPy module:', basic_NumPy
    t1 = timer(g.ext_gridloop1, (myfunc,), repetitions=1)
    t2 = timer(g.ext_gridloop2, (myfunc,), repetitions=1)
    t3 = timer(g.ext_gridloop2, (expression,), repetitions=1)
    print """
Results using an extension module (%dx%d grid),
with callback to Python for each point:
gridloop1 (w/func):               %s
gridloop2 (w/func):               %s
gridloop1 (w/string expression):  %s
""" % (n, n, t1, t2, t3)

    # try the improved functions (works only for the F77 module):
    nrep = 20
    if 'gridloop_vec2' in dir(ext_gridloop):
        t4 = timer(g.ext_gridloop_vec2, (myfuncf2,), repetitions=nrep)
        print """\
gridloop_vec2 (w/func & NumPy):    %s""" % t4
    if 'gridloop2_str' in dir(ext_gridloop):        
        t5 = timer(g.ext_gridloop2_str, ('myfunc',), repetitions=nrep)
        print """\
gridloop2_str (no Py callback):   %s""" % t5

        # try 'inline' F77 compiled callback too:
        # (give F77 source for core of callback function as argument)
        g.ext_gridloop2_fcb_compile('sin(x*y) + 8*x')
        t6 = timer(g.ext_gridloop2_fcb, (), repetitions=nrep)
        g.ext_gridloop2_compile('sin(x*y) + 8*x')
        t7 = timer(g.ext_gridloop2_v2, (), repetitions=nrep)


def exceptions1():
    """Test exceptions raised by the extension module."""
    g = Grid2Deff(dx=0.5, dy=1)
    def myfunc(x, y):
        return sin(x*y) + 8*x
    g.ext_gridloop_exceptions(myfunc)

def _run():
    # provide function to call (verify1, timing2, exceptions1, etc.)
    # as command-line argument
    try:
        func = sys.argv[1]
    except:
        # basic test if no command-line argument
        func = 'verify1'
    if func == 'timing2':
        # in case of timing, specify grid size as 2nd argument:
        try:
            n = int(sys.argv[2])
        except:
            n = 1100
        exec 'timing2(%d)' % n
    else:
        exec func + '()'
    
if __name__ == '__main__':
    _run()


