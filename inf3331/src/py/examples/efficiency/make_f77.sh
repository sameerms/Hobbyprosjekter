#!/bin/sh
f2py -m matrix_f77 -DF2PY_REPORT_ON_ARRAY_COPY=1 -DF2PY_REPORT_ATEXIT \
         -c matrix_f77.f \
         only: makematrix set get fill1 lfill1 fill2 lfill2 tonumpy adump 
f2py -m call -DF2PY_REPORT_ON_ARRAY_COPY=1 -DF2PY_REPORT_ATEXIT -c call.f
