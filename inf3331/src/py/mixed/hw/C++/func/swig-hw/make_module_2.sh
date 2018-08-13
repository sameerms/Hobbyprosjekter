#!/bin/sh -x
./clean.sh
# compile C code and make a shared library module for use with Python
# method: run setup.py

python setup.py build_ext
python setup.py install --install-platlib=.

# test:
python -c 'import hw'

