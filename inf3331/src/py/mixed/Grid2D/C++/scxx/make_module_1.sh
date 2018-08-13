#!/bin/sh -x
rm -f *.o *.so
root=`python -c 'import sys; print sys.prefix'`
ver=`python -c 'import sys; print sys.version[:3]'`
inc=$PYTHONSRC/../tools/scxx
lib=$root/lib
g++ -O3 -g -I. -I$root/include/python$ver -I$inc -c gridloop_scxx.cpp
g++ -shared -o ext_gridloop.so gridloop_scxx.o $lib/frobit.so

# test the module:
python -c 'import ext_gridloop; print dir(ext_gridloop)'
           
