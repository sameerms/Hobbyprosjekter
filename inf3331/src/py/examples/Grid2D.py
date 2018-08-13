#!/usr/bin/env python

from py4cs.numpytools import *
import time, sys, Gnuplot
from math import sin as mathsin  # efficiency trick

class Grid2D:
    def __init__(self,
                 xmin=0, xmax=1, dx=0.5,
                 ymin=0, ymax=1, dy=0.5):
        # coordinates in each space direction:
        self.xcoor = sequence(xmin, xmax, dx, Float)
        self.ycoor = sequence(ymin, ymax, dy, Float)

        # store for convenience:
        self.dx = dx;  self.dy = dy  
        self.nx = len(self.xcoor);  self.ny = len(self.ycoor)

        # make two-dim. versions of the coordinate arrays:
        # (needed for vectorized function evaluations)
        self.xcoorv = self.xcoor[:,NewAxis]
        self.ycoorv = self.ycoor[NewAxis,:]

    def vectorized_eval(self, f):
        """Evaluate a vectorized function f at each grid point."""
        return f(self.xcoorv, self.ycoorv)
    
    def __call__(self, f):
        """
        Treat f either as an expression containing x and y
        or as a standard Python function f(x,y). Evaluate the 
        formula or function for all grid points and 
        return the corresponding two-dimensional array.
        """
        if isinstance(f, str):  # is f a string?
            # introduce the names x and y such that a simple
            # eval(f) will work for the arrays directly:
            x = self.xcoorv;  y = self.ycoorv
            a = eval(f)
        else:
            a = f(self.xcoorv, self.ycoorv)
        return a

    def __str__(self):
        s = '\nx: ' + str(self.xcoor) + '\ny: ' + str(self.ycoor)
        return s

    def gridloop(self, f):
        """
        Implement strights loops as a simple (and slow)
        alternative to the vectorized code in __call__.
        """
        f_is_str = isinstance(f, str)  # is f a string? save res.
        if f_is_str:
            f_compiled = compile(f, '<string>', 'eval')
        lx = size(self.xcoor); ly = size(self.ycoor)
        _a = zeros((lx,ly), Float)  # use _a so a can be in f expr.
        for i in xrange(lx):
            x = self.xcoor[i]
            for j in xrange(ly):
                y = self.ycoor[j]
                if f_is_str:
                    _a[i,j] = eval(f_compiled)
                else:
                    _a[i,j] = f(x, y)
        return _a

    def gridloop_hardcoded_func(self):
        """As gridloop, but hardcode a function formula."""
        lx = size(self.xcoor); ly = size(self.ycoor)
        a = zeros((lx,ly), Float)
        for i in xrange(lx):
            x = self.xcoor[i]
            for j in xrange(ly):
                y = self.ycoor[j]
                a[i,j] = sin(x*y) + 8*x
        return a

    def gridloop_list(self, f):
        """As gridloop, but use a list instead of a NumPy array."""
        f_is_str = isinstance(f, str)  # is f a string? save res.
        if f_is_str:
            f_compiled = compile(f, '<string>', 'eval')
        lx = size(self.xcoor); ly = size(self.ycoor)
        _a = []
        for i in xrange(lx):
            _a.append([])
            x = self.xcoor[i]
            for j in xrange(ly):
                y = self.ycoor[j]
                if f_is_str:
                    _a_value = eval(f_compiled)
                else:
                    _a_value = f(x, y)
                _a[i].append(_a_value)
        return _a

    def plot(self, func_values):
        self.g = Gnuplot.Gnuplot(persist=1)
        self.g('set parametric')
        self.g('set data style lines')
        self.g('set hidden')
        self.g('set contour base')
        self.g.splot(Gnuplot.GridData(
            func_values, self.xcoor, self.ycoor))
        time.sleep(2)  # give Gnuplot some time to make the plot
        """
        More examples on plotting two-dimensional scalar fields in Gnuplot
        can be found in the demo.py script that comes with the
        Python package containing the Gnuplot module.
        """
        

def timing(n=2000):
    # timing:
    dx = 1.0/n
    g = Grid2D(xmin=0, xmax=1, dx=dx,
               ymin=0, ymax=1, dy=dx)

    expression = 'sin(x*y) + 8*x'
    print 'evaluating', expression
    def myfunc(x, y):
        return sin(x*y) + 8*x

    from py4cs.misc import timer
    t0 = time.clock()

    # vectorized expressions are so fast that we run the code
    # repeatedly
    rep=20
    print 'vectorized code with eval... (%d calls)' % rep
    t1 = timer(g.__call__, (expression,), repetitions=rep, comment='eval(str)')
    print 'vectorized code with function call... (%d calls)' % rep
    t2 = timer(g.__call__, (myfunc,), repetitions=rep, comment='myfunc')

    print 'explicit loops with formula hardcoded...(1 call)'
    f = g.gridloop_hardcoded_func()
    t3 = timer(g.gridloop_hardcoded_func, (), repetitions=1, comment='')

    print 'explicit loops with eval...(1 call)'
    t4 = timer(g.gridloop, (expression,), repetitions=1, comment='eval(str)')
    print 'explicit loops with myfunc...(1 call)'
    t5 = timer(g.gridloop, (myfunc,), repetitions=1, comment='myfunc')

    print 'explicit loops with list and eval...(1 call)'
    t6 = timer(g.gridloop_list, (expression,), repetitions=1,
               comment='eval(str)')
    print 'explicit loops with list and myfunc...(1 call)'
    t7 = timer(g.gridloop_list, (myfunc,), repetitions=1, comment='myfunc')

    # The scalar computations above used sin from NumPy, which is
    # known to be slow for scalar arguments. Here we use math.sin
    # (stored in mathsin, could also use the slightly slower math.sin
    # explicitly)
    # taken globally so eval works: from math import sin as mathsin
    def myfunc_scalar(x, y):
        return mathsin(x*y) + 8*x
    expression_scalar = 'mathsin(x*y) + 8*x'
    print 'explicit loops with eval...(1 call) and math sin'
    t8 = timer(g.gridloop, (expression_scalar,), repetitions=1,
               comment='eval(str)')
    print 'explicit loops with myfunc...(1 call) and math sin'
    t9 = timer(g.gridloop, (myfunc_scalar,), repetitions=1, comment='myfunc')

    # report
    f = max(t1,t2)  # fastest implementation
    print """
Basic NumPy module: %s

vectorized with eval(expression):   %.2f  %.1f
vectorized with myfunc call:        %.2f  %.1f

scalar versions with NumPy sin function:
loops with inline formula:          %.2f  %.1f
loops with eval(expression):        %.2f  %.1f
loops with myfunc call:             %.2f  %.1f
loops with list and eval:           %.2f  %.1f
loops with list and myfunc:         %.2f  %.1f

scalar versions with math.sin function:
loops with eval(expression_scalar): %.2f  %.1f
loops with myfunc_scalar:           %.2f  %.1f
""" % (basic_NumPy, t1, t1/f, t2, t2/f, t3, t3/f, t4, t4/f, t5, t5/f,
       t6, t6/f, t7, t7/f, t8, t8/f, t9, t9/f)
    

def verify1():
    g = Grid2D()
    global a  # will be evaluated in global scope in g.__call__
    a = 2  # (global variable when eval(formula) is evaluated)
    f = g('a*x+y')
    print g, f
    f = g.gridloop('a*x+y')
    print g, f
    #g.plot(f)
    
def _run():
    try:
        func = sys.argv[1]
    except:
        func = 'verify1'
    if func == 'timing':
        try:
            n = int(sys.argv[2])
        except:
            n = 2000
        exec 'timing(%d)' % n
    else:
        exec func + '()'
    
if __name__ == '__main__':
    _run()


