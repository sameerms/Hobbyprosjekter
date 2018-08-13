#!/usr/bin/env python
"""Examples of using setattr, getattr, and hasattr."""
from py4cs.numpytools import *
from py4cs.misc import timer

def run(solvers, methods, data, datasets):
    results = {}
    # find largest data sets:
    maxsize = max([size(getattr(data, d)) for d in datasets \
                   if hasattr(data, d)])
    print maxsize
    # combine all solvers, methods, and datasets:
    for s in solvers:
        for m in methods:
            for d in datasets:
                if hasattr(solver, m) and hasattr(data, d):
                    f = getattr(solver, m)
                    x = getattr(data, d)
                    r = timer(f, (x,), repetitions=maxsize/size(x))
                    results[(m,d)] = r
    return results

class Extreme:
    """Find extreme values of NumPy data."""
    def __init__(self):
        pass

    def ravel(self, x):
        """Make x one-dimensional, use list min/max in Python."""
        rx = ravel(x)
        xmin = min(rx)
        xmax = max(rx)
        return xmin, xmax

    def flat(self, x):
        """Use list min/max on x.flat."""
        xmin = min(x.flat)
        xmax = max(x.flat)
        return xmin, xmax

    def MLab_minmax(self, x):
        """Use MLab's min/max functions repeatedly."""
        import MLab
        xmin = x; xmax = x
        for i in iseq(len(x.shape)-1,0,-1):
            xmin = MLab.min(xmin, i)
            xmax = MLab.max(xmax, i)
        return xmin, xmax

class Arrays:
    def __init__(self, n):
        self.d1 = seq(1, n, 1)
        self.d2 = seq(1, n*n, 1)
        self.d2.shape = (n, n)
        self.d3 = seq(1, n*n*n, 1)
        self.d3.shape = (n, n, n)
        self.maxsize = size(self.d3)

data = Arrays(200)
solver = Extreme()
methods = ('ravel', 'flat', 'MLab_minmax')
datasets = ('d1', 'd2', 'd3', 'd4', 'd5')

r = run((solver,), methods, data, datasets)
for m, d in r:
    print '%s and %s : %g' % (m, d, r[(m,d)])
