#!/usr/bin/env python
"""
Read tabular data from file into NumPy arrays and vice versa.

This module provides functions for

  * reading row-column table data from file into NumPy arrays
  * writing two-dimensional NumPy arrays to file in a table fashion.

read:
    Load a table with numbers into a two-dim. NumPy array.
    file             file object
    commentchar      files starting with commentchar are skipped
                     (blank lines are also skipped)
    output:          two-dimensional (row-column) NumPy array.

write:
    Write a two-dim. NumPy array a in tabular form.
    file             file object
    a                two-dim. NumPy array

readfile:
    As read, but input is filename rather than a file object.
    The columns are returned as separate arrays instead of
    a two-dimensional array.
  
"""

import string, sys, os, re
from Numeric import *

def read(file, commentchar='#'):
    """Load a table with numbers into a two-dim. NumPy array."""
    # read until next blank line:
    r = []  # total set of numbers (r[i]: numbers in i-th row)
    while 1:  # might call read several times for a file
        line = file.readline()
        if not line: break  # end of file
        if line.isspace(): break  # blank line
        if line[0] == commentchar: continue # treat next line
        r.append([float(s) for s in line.split()])
    return array(r, Float)

def readfile(filename, commentchar='#'):
    """As read. Return columns as separate arrays."""
    f = open(filename, 'r')
    a = read(f, commentchar)
    r = [a[:,i] for i in range(a.shape[1])]
    return r

def write(file, a):
    """Write a two-dim. NumPy array a in tabular form."""
    if len(a.shape) != 2:
        raise TypeError, \
              "a 2D array is required, shape now is "+str(a.shape)
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            file.write(str(a[i,j]) + "\t")
        file.write("\n")

def _generate(m,n,filename, title=None):
    f = open(filename, 'w')
    if title: f.write('# ' + title + "\n#\n")
    for i in range(m):
        for j in range(n):
            r = float(i+j*j)/float(m*n);
            f.write(str(r) + "\t")
        f.write("\n")

def _test(n):
    _generate(n, 20, "tmp.1", "here are some data")
    import time
    t0 = time.clock()
    f = open("tmp.1", "r")
    q = read(f)
    t1 = time.clock()
    print "read:", t1-t0,"seconds\n",q[0:5,0:5]
    f.close()
    t0 = time.clock()
    f = open("tmp.2", "w")
    write(f,q)
    t1 = time.clock()
    print "write:", t1-t0,"seconds"
    
    # compare with TableIO:
    try:
        import TableIO
    except:
        sys.exit(0) # exit silently
    t0 = time.clock()
    p = TableIO.readTableAsArray("tmp.1", "#")
    t1 = time.clock()
    print "TableIO.readTableAsArray:", t1-t0,"seconds\n",p[0:5,0:5]
    t0 = time.clock()
    TableIO.writeArray("tmp.3", p)
    t1 = time.clock()
    print "TableIO.writeArray:", t1-t0,"seconds"

if __name__ == '__main__':
    _test(1000)
    


