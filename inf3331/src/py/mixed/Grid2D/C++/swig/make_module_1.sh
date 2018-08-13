#!/bin/sh -x
./clean.sh

swig -python -c++ -I. ext_gridloop.i

root=`python -c 'import sys; print sys.prefix'`
ver=`python -c 'import sys; print sys.version[:3]'`
g++ -I. -O3 -g -I$root/include/python$ver \
    -c NumPyArray.cpp gridloop.cpp ext_gridloop_wrap.cxx
g++ -shared -o _ext_gridloop.so NumPyArray.o \
    gridloop.o ext_gridloop_wrap.o

# test the module:
python -c 'import ext_gridloop; print dir(ext_gridloop);'
           