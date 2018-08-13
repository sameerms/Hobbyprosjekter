#!/usr/bin/env python
import sys, math, string
from Numeric import *
"""
As datatrans2.py, but using NumPy arrays and the special
filetable module to simplify the I/O.
"""
    
try:
    infilename = sys.argv[1];  outfilename = sys.argv[2]
except:
    print "Usage:",sys.argv[0], "infile outfile"; sys.exit(1)

# read (x,y) data from file into a NumPy array data:
import py4cs.filetable
f = open(infilename, 'r'); data = py4cs.filetable.read(f); f.close()

# transform y values:

def myfunc(y):
    # y is a NumPy array
    lt0_indices = less(y,0)  # find all indices where y<0
    r = y**5*exp(-y)
    # truncate, i.e., insert 0 for all indices where y<0:
    y = where(lt0_indices, 0.0, r)
    return y

y = data[:,1]
y = myfunc(y)

# create a two-dimensional NumPy array with (x,myfunc(y)):
newdata = transpose(array([data[:,0], y]))

# dump the new data to file:
f = open(outfilename, 'w'); py4cs.filetable.write(f, newdata); f.close()
# end
