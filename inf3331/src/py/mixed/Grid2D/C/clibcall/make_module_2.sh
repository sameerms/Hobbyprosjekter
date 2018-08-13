#!/bin/sh -x
./clean.sh

python setup.py build_ext
python setup.py install --install-platlib=.
# test the module:
python -c 'import ext_gridloop; print dir(ext_gridloop); print ext_gridloop.__doc__'
           