#!/usr/bin/env python
import sys, math, string
from py4cs.numpytools import *
"""
As datatrans3a.py, but splitting the whole file at once,
store the numbers in a one-dimensional NumPy and then
reshaping the array appropriately.
"""
    
try:
    infilename = sys.argv[1];  outfilename = sys.argv[2]
except:
    print "Usage:",sys.argv[0], "infile outfile"; sys.exit(1)

# read (x,y) data from file into a NumPy array data:
f = open(infilename, 'r')
data = array([float(x) for x in f.read().split()], Float)
# (map is normally faster than [float(x) for x in f.read().split()])
data.shape = (len(data)/2,2)

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
import py4cs.filetable as filetable
f = open(outfilename, 'w'); filetable.write(f, newdata); f.close()
# end
