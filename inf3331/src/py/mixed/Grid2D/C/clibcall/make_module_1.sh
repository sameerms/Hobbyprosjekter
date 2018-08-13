#!/bin/sh -x
./clean.sh
root=`python -c 'import sys; print sys.prefix'`
ver=`python -c 'import sys; print sys.version[:3]'`
gcc -O3 -g -I$root/include/python$ver -I. \
    -I$scripting/src/C \
    -c gridloop1_C.c gridloop1_wrap.c
gcc -shared -o ext_gridloop.so gridloop1_C.o gridloop1_wrap.o

# test the module:
python -c 'import ext_gridloop; print dir(ext_gridloop); \
           print ext_gridloop.__doc__'
           