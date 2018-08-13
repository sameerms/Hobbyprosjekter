#!/bin/sh
import sys, os
from math import cos, sin, pi

def vectorization():
    def somefunc(x):
        if x < 0:
            return 0
        else:
            return sin(x)
        
    import scipy.special
    somefunc_SciPy = scipy.special.general_function(somefunc)
    from py4cs.numpytools import sequence
    n = 800000;  x = sequence(-2, 2, 1.0/n)
    y = somefunc_SciPy(x)
    print y[0], y[-1]

def integrate():
    def myfunc(x):
        return sin(x)
    from scipy import integrate
    result, error = integrate.quad(myfunc, 0, pi)
    print result, error

    def myfunc(x, a, b):
        return a + b*sin(x)
    a=0; b=1
    result, error = integrate.quad(myfunc, 0, pi, args=(a,b), epsabs=1.0e-9)
    print result, error

    
class Oscillator:
    """Implementation of the oscillator code using SciPy."""
    def __init__(self, **kwargs):
        """Initialize parameters from arguments."""
        self.p = {'m': 1.0, 'b': 0.7, 'c': 5.0, 'func': 'y',
                  'A': 5.0, 'w': 2*pi, 'y0': 0.2,
                  'tstop': 30.0, 'dt': 0.05}
        self.p.update(kwargs)
        
    def scan(self):
        """Read parameters from standard input."""
        read = sys.stdin.readline
        self.p = {'m': float(read()), 'b': float(read()),
                  'c': float(read()), 'func': read().strip(),
                  'A': float(read()), 'w': float(read()),
                  'y0': float(read()), 'tstop': float(read()),
                  'dt': float(read())}

    def solve(self):
        """Solve ODE system."""
        # mapping: name of f(y) to Python function for f(y):
        self._fy = {'y': _fy, 'y3': _fy3, 'siny': _fsiny}
        # set initial conditions:
        self.y0 = [self.p['y0'], 0.0]
        # call SciPy solver:
        from py4cs.numpytools import sequence
        self.t = sequence(0, self.p['tstop'], self.p['dt'])

        from scipy.integrate import odeint
        self.yvec = odeint(self.f, self.y0, self.t)

        self.y = self.yvec[:,0]  # y(t)
        # write t and y(t) to sim.dat file:
        f = open('sim.dat', 'w')
        for y, t in zip(self.y, self.t):
            f.write('%g %g\n' % (t, y))
        f.close()

    def f(self, y, t):
        """Right-hand side of 1st-order ODE system."""
        p = self.p # short form
        return [y[1],
                (p['A']*cos(p['w']*t) - p['b']*y[1] -
                 p['c']*self._fy[p['func']](y[0]))/p['m']]

def _fy   (y): return y
def _fy3  (y): return y + y**3/6.0
def _fsiny(y): return sin(y)

def test_Oscillator(dt=0.05):
    s = Oscillator(m=5, dt=dt)
    t1 = os.times()
    s.solve()
    t2 = os.times()
    print 'CPU time of odeint:', t2[0]-t1[0] + t2[1]-t1[1]

    # compare with the oscillator program:
    cmd = './simviz1.py -noscreenplot -case tmp1'
    for option in s.p:  # construct command-line options
        cmd += ' -'+option + ' ' + str(s.p[option])
    t3 = os.times()
    os.system(cmd)
    t4 = os.times()
    print 'CPU time of oscillator:', t4[2]-t3[2] + t4[3]-t3[3]
    from py4cs.CurveViz import CurveVizGnuplot
    from py4cs.filetable import readfile
    t, y = readfile(os.path.join('tmp1','sim.dat'))
    g = CurveVizGnuplot(title='dt=%g' % dt)
    g.plotcurves([((t,y), 'RK2'), ((s.t,s.y), 'LSODE')], ps=True)

# test part:
if __name__ == '__main__':
    test = sys.argv[1]
    if test == 'vectorization':
        vectorization()
    elif test == 'integrate':
        integrate()
    elif test == 'Oscillator':
        test_Oscillator(dt=float(sys.argv[1]))
    else:
        print test, 'not implemented'
    

