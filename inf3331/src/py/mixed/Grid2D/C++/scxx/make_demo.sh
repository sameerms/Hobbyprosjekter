#!/bin/sh -x
rm -f *.o *.so
root=`python -c 'import sys; print sys.prefix'`
ver=`python -c 'import sys; print sys.version[:3]'`
inc=$PYTHONSRC/../tools/scxx
lib=$root/lib
g++ -O3 -g -I. -I$root/include/python$ver -I$inc -c scxx_demo.cpp
g++ -o app.tmp -L$root/lib/python$ver/config -L$root/lib -L/usr/X11R6/lib \
    scxx_demo.o $root/lib/frobit.so \
    -lpython$ver -ltix8.1.8.3 -lBLT24 -ltk8.3 -ltcl8.3 -lz \
    -lX11 -lpthread -ldl -lutil 

           
