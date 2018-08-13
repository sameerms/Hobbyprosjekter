#!/usr/bin/env python
"""demonstrate fitting a stright line to data with NumPy"""
# generate random data and fit a straight line
import sys
try:
    n = int(sys.argv[1])
except:
    n = 20  # no of data points

# compute data points in x and y arrays,
# x in (0,1) and y=-2*x+3+eps, where eps is normally
# distributed with mean zero and st.dev. 0.25.

from py4cs.numpytools import *
RandomArray.seed(20,21)

x = sequence(0.0, 1.0, 1.0/(n-1))
# adjust n in case of rounding errors in the above statement:
n = len(x)  
eps = RandomArray.normal(0, 0.25, n)  # noise
a_exact = -2.0; b_exact = 3.0
y = a_exact*x + b_exact + eps

# create least squares system:
A = transpose(array([x, zeros(n, Float)+1]))
B = y
sol = LinearAlgebra.linear_least_squares(A, B)
# sol is a 4-tuple, the solution (a,b) is the 1st entry:
a, b = sol[0]

# plot:
import Gnuplot
g = Gnuplot.Gnuplot(persist=1)
# persist=1: the plot remains on the screen after g is deleted
g('set pointsize 2')
data  = Gnuplot.Data(x, y,
                     with='points', title='data')
exact = Gnuplot.Func('%(a_exact)g*x + %(b_exact)g' % vars(),
                     with='lines', title='exact')
fit   = Gnuplot.Func('%(a)g*x + %(b)g' % vars(),
                     with='lines', title='least-squares fit')
g.plot(data, exact, fit)
g.hardcopy(filename='tmp.ps', enhanced=1, mode='eps',
           color=0, fontname='Times-Roman', fontsize=28)
# make a PNG plot too:
g('set term png small color')
g("set output 'tmp.png'")
g.plot(data, exact, fit)
import time; time.sleep(2)  # wait to let Gnuplot read data



