#!/bin/sh
./clean.sh
if [ $# -lt 1 ]; then
    echo "make_module_1.sh gridloopX"
    echo "(X is a number)"
    exit
fi
modulefile=$1
options=$2

root=`python -c 'import sys; print sys.prefix'`
ver=`python -c 'import sys; print sys.version[:3]'`

echo gcc -O3 -g -I$root/include/python$ver \
    -I$scripting/src/C $options \
    -c $modulefile.c -o gridloop.o

gcc -O3 -g -I$root/include/python$ver \
    -I$scripting/src/C $options \
    -c $modulefile.c -o gridloop.o

echo gcc -shared -o ext_gridloop.so gridloop.o 
gcc -shared -o ext_gridloop.so gridloop.o 

echo
echo test the module:
echo python -c 'import ext_gridloop; print dir(ext_gridloop); \
           print ext_gridloop.__doc__'
python -c 'import ext_gridloop; print dir(ext_gridloop); \
           print ext_gridloop.__doc__'

# run the calling script in a debugger:
gdb `which python` <<EOF
run ../../../Grid2Deff.py verify1
where
^D
EOF
