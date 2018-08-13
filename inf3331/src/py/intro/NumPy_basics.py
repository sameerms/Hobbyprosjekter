#!/usr/bin/env python
"""
Demonstrate basic usage of the Numeric module
"""

from py4cs.numpytools import *
#from Numeric import *
#from numarray import *

n=10

# create an array a of length n, with zeroes and
# double precision float type:
a = zeros(n, Float)
print 'zeros(n, Float):', type(a), a.typecode(), a
a = zeros(n) # becomes array of integers
print 'zeros(n)', type(a), a.typecode(), a
# note: no keyword arguments in the zeros function:
# a = zeros(n, typecode=Float) # error

# create an array x with values from -5 to 5 in 
# steps of 0.5:
#x = arrayrange(-5, 5, 0.5, typecode=Float)
x = arrayrange(-5, 5, 0.5, Float)
# or (Float is implied since when at least one of the
# arguments is a real number):
x = arrayrange(-5, 5, 0.5)
# note: round-off errors may prevent the last element
# in x from being equal to the upper bound 5
x = arrayrange(-5, 5.1, 0.5)  # ensures that 5 is in x
print 'arrayrange(-5, 5, 0.5)', type(x), x.typecode(), x

# it is trivial to make accompanying y values:
y = sin(x/2.0)*3.0
print 'y = sin(x/2.0)*3.0:', type(y), y.typecode(), y

# create a NumPy array of a Python list:
pl = [0, 1.2, 4, -9.1, 5, 8]
a = array(pl, typecode=Float)  # can omit typecode if desired
print 'pl = [0, 1.2, 4, -9.1, 5, 8]; '\
      'array(pl, typecode=Float)', type(a), a
# from nested Python list to NumPy arrays and back again:
x = [0, 0.5, 1]; y = [-6.1, -2, 1.2]  # lists
a = array([x, y])  # form 2x3 array (x and y as rows)
# turn 1st row to Python list and use index to locate an entry:
i = a[0,:].tolist().index(0.5)
y_i = a[1,i]

# initialization from a function:
def myfunc(i, j):
    return (i+1)*(j+4-i)

# make 100x100 array where a[i,j] = myfunc(i,j):
a = fromfunction(myfunc, (100,100))

# make a one-dim. array of length n:
n = 10000000
def myfunc2(i):  return sin(i*0.0001)
print '\ncreating arrays of length %5.0E ... it may take some time...' % (float(n))
import time; t1 = time.clock()
a = fromfunction(myfunc2, (n,))
t2 = time.clock()
cpu_fromfunction = t2 - t1
# alternative initialization via arange and sin:
a = arange(1, n, 1, Float); a = sin(a*0.0001)
cpu_arange_sin = time.clock() - t2
print 'fromfunction took', cpu_fromfunction, \
      's and arange&sin took', cpu_arange_sin, 's for length', n

# make an array computed on a 3D grid:


# indexing:
a = array([0, 1.2, 4, -9.1, 5, 8])
a.shape = (2,3) # turn a into a 2x3 matrix

print a[0,1]     # print entry (0,1)
i=1; j=0
a[i,j] = 10      # assignment to entry (i,j)
print a[:,0]     # print first column
a[:,:] = 0       # set all elements of a equal to 0

a = sequence(0, 29)
a.shape = (5,6)
print a
print a[1:3,:-1:2]    # a[i,j] for i=1,2 and j=0,2,4
print a[::3,2:-1:2]   # a[i,j] for i=0,3 and j=2,4
i = slice(None, None, 3);  j = slice(2, -1, 2)
print a[i,j]


a = array([0, 1.2, 4, -9.1, 5, 8])
a.shape = (2,3) # turn a into a 2x3 matrix

# traverse array a:
for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        a[i,j] = (i+1)*(j+1)*(j+2)
        print 'a[%d,%d]=%g ' % (i,j,a[i,j]),
    print  # newline after each row

print 'a.shape = (2,3); a=', a 
# turn a into a vector of length 6 again
a.shape = (size(a),)   # size(a) returns the total no of elements
print 'a.shape = (size(a),); a=', a 

# mathematical functions:
b = 3*a - 1
b = clip(b, 0.1, 1.0E+20)  # throw away entries < 0.1
c = cos(b)     # take the cosine of all entries in b
print 'b = 3*a - 1; b = clip(b, 0.1, 1.0E+20); c = cos(b)', b, c
# these functions are available:
c = sin(b)   
c = arcsin(c)
c = sinh(b)
# same functions for the cos and tan families
c = b**2.5  # raise all entries to the power of 2.5
c = log(b)
c = exp(b)
c = sqrt(b)

# "in-place" opertions:
print 'in-place operations:'
multiply(a, 3.0, a) # multiply a's entries by 3
print 'multiply(a, 3.0, a); a=', a
subtract(a, 1.0, a) # subtract 1 from a's entries
print 'subtract(a, 1.0, a); a=', a
divide  (a, 3.0, a) # divide a's entries by 3
print 'divide  (a, 3.0, a); a=', a 
add     (a, 1.0, a) # add 1 to a's entries
print 'add     (a, 1.0, a); a=', a
power   (a, 2.0, a) # square all entries
print 'power   (a, 2.0, a); a=', a 
# in-place arithmentic operators:
a *= 3.0
print 'a *= 3.0; a=', a
a -= 1.0   
print 'a -= 1.0; a=', a
a /= 3.0   
print 'a /= 3.0; a=', a
a += 1.0   
print 'a += 1.0; a=', a
a **= 2.0  
print 'a **= 2.0; a=', a

a = array([0, 1.2, 4, -9.1, 5, 8])
a.shape = (2,3) # turn a into a 2x3 matrix

# indexing as for Python lists:
a[2:4] = -1      # set a[2] and a[3] to -1
a[-1] = a[0]     # set last element equal to first one
print 'a[2:4] = -1; a[-1] = a[0]; a=', a 

# multi-dimensional indexing:
a.shape = (3,2)
print 'a.shape = (3,2); a[:,0]',
print a[:,0]     # print first column
print 'a[:,1::2]',
print a[:,1::2]  # print second column with stride 2

b = transpose(a)
print 'transpose(a): ', b

if b.typecode() != 'd':
    c = b.astype(Float)
else:
    print 'b array entries are of type Float so '\
          'no casting is necessary'
# typecode() returns 'd' for Float, 'l' for Int,
# 'D' for Complex

# with numarray we use b.type() instead
try:
    if b.type() != Float:
        c = b.astype(Float)
except:
    # Numeric:
    pass


# try out default typecodes:
def create(expression):
    x = eval(expression)
    print '%s; variable type=%s typecode=%s' % \
          (expression,type(x),x.typecode()),
    try:  # numarray?
        print str(x.type())
    except:
        print
    return x

x = create('arrayrange(-5, 5, 0.5)')
x = create('arrayrange(-5, 5, 1)')
x = create('arrayrange(-5.0, 5, 1)')
x = create('arrayrange(-5, 5, 0.5, Complex)')
print 'real part of x:', x.real
print 'imaginary part of x:', x.imag

# file reading and writing of NumPy arrays:
a = sequence(min=1, max=20, inc=1, type=Int) # 1-20
a.shape = (2,10)

# ASCII format:
file = open('tmp.dat', 'w')
file.write('Here is an array a:\n')
file.write(repr(a))
# array2string has many options for controlling the
# output of an array as a string, but repr() gives a format
# that can be converted back to an array by eval()
file.close()

# load the array from file into b:
file = open('tmp.dat', 'r')
file.readline()  # load first comment line
b = eval(file.read())
file.close()
print 'read from ASCII file: a is',type(a),'and\n   a=',a

# binary format:
file = open('tmp.dat', 'wb')
file.write(a.tostring())  # convert a to binary form and dump
file.close()

file = open('tmp.dat', 'rb')
# load binary data into a:
b = fromstring(file.read(), Float) 
file.close()
print 'read from binary file: a=',a

# pickling NumPy arrays: see src/tools/ArrayDB.py


print '\n\n--------- random numbers -------------\n'
n = 10000  # no of random samples

# native Python support for random numbers:
import random
random.seed() # set seed based on current time
random.seed(2198)  # control the seed
# uniform and random are inherited from whrandom:
print 'random number on (0,1):',         random.random()
print 'unform random number on (-1,1):', random.uniform(-1,1)
print 'N(0,1) uniform random number:',   random.gauss(0,1)

# import RandomArray (or RandomArray2 as RandomArray) is done
# transparently by NumPy!

RandomArray.seed(1928,1277) # set seed
# seed() provides a seed based on current time
print 'mean of %d random uniform random numbers:' % n
u = RandomArray.random(n)  # uniform numbers on (0,1)
print 'on (0,1):', sum(u)/n, '(should be 0.5)'
u = RandomArray.uniform(-1,1,n) # uniform numbers on (-1,1)
print 'on (-1,1):', sum(u)/n, '(should be 0)'

# normally distributed numbers:
mean = 0.0; stdev = 1.0
u = RandomArray.normal(mean, stdev, n)
m = sum(u)/n  # empirical mean
s = sqrt(sum((u - m)**2)/(n-1))  # empirical st.dev.
print 'generated %d N(0,1) samples with\nmean %g '\
      'and st.dev. %g using RandomArray.normal' % (n, m, s)

less_than = u < 1.5
p = sum(less_than)
prob = p/float(n)
print 'probability N(0,1) < 1.5: %.2f' % prob

print '\n\n--------- linear algebra -------------\n'

# import LinearAlgebra (or LinearAlgebra2 as LinearAlgebra) is done
# transparently by NumPy!

n = 4
A = zeros(n*n, Float); A.shape = (n,n)
x = zeros(n, Float)
b = zeros(n, Float)

for i in range(n):
    x[i] = i/2.0       # some prescribed solution
    for j in range(n):
        A[i,j] = 2.0 + float(i+1)/float(j+i+1)
b = matrixmultiply(A,x)  # adjust rhs to fit x

# does not work for floats, only ints:
#def formula(i,j): return 2.0 + float(i+1)/float(j+1+1)
#A = fromfunction(formula, (n,n))
#A = fromfunction(lambda i,j: 2.0 + float(i+1)/float(j+i+1),(n,n))
#A = fromfunction(lambda i,j: 2 + (i+1)/(j+i+1),(n,n)) # ok

# solve linear system A*y=b:
y = LinearAlgebra.solve_linear_equations(A, b)

# compare exact x with the y we computed:
if abs(sum(x - y)) < 1.0E-10:  print 'correct solution'
else:                          print 'wrong solution',x,y
# alternative:
if allclose(x, y, atol=1.0E-10, rtol=1.0E-12):
    print 'correct solution'
else:
    print 'wrong solution', x, y

# some other operations:
c = innerproduct(x,y)
Ai = LinearAlgebra.inverse(A)
d = LinearAlgebra.determinant(A)
print 'LinearAlgebra.determinant(A) =', d

# test: A times A inverse is the identity matrix:
Inv = LinearAlgebra.inverse # abbreviation
print 'A*A^-1 = ',matrixmultiply(A, Inv(A))
print 'Id = ',identity(len(A))
print 'A*A^-1 - Id = ', matrixmultiply(A, Inv(A))-identity(len(A))
s = sum(matrixmultiply(A, Inv(A)) - identity(len(A)))
print 's=', s

# eigenvalues and eigenvectors:
Ae_val = LinearAlgebra.eigenvalues(A)  # eigenvalues only
Ae_val, Ae_vec = LinearAlgebra.eigenvectors(A)  # eigenvalues and -vectors
print 'A=', A
print 'eigenvalues=\n', Ae_val
print 'eigenvectors=\n', Ae_vec


# Some Matlab-like functions:
import MLab
# Note: MLab.py is a good example on using Numeric!!!

# vectorization:
def somefunc(x):
    """Scalar function."""
    if x < 0:
        return 0
    else:
        return sin(x)

def somefunc_NumPy(x):
    n = size(x)
    r = zeros(n, Float)
    for i in xrange(n):
        if x.flat[i] < 0:   # x.flat views x as one-dimensional
            r[i] = 0.0
        else:
            r[i] = sin(x[i])
    r.shape = x.shape
    return r

def somefunc_NumPy2(x):
    """Vectorized version of somefunc."""
    lt0_indices = less(x,0)  # find all indices where x<0
    r = sin(x)
    # truncate, i.e., insert 0 for all indices where x<0:
    r = where(lt0_indices, 0.0, r)
    return r

somefunc_list = [somefunc_NumPy, somefunc_NumPy2]
try:
    import scipy.special
    somefunc_SciPy = scipy.special.general_function(somefunc)
    somefunc_SciPy.__name__ = somefunc.__name__ + '_SciPy_vectorized'
    somefunc_list.append(somefunc_SciPy)
except:
    print 'unsuccessful scipy import, cannot use scipy'
n = 1000000
x = sequence(0, 2, 1.0/n, Float)
from py4cs.misc import timer
for f in somefunc_list:
    timer(f, (x,), repetitions=1)
timer(somefunc_NumPy2, (x,), repetitions=10)
print 'end of', sys.argv[0]
