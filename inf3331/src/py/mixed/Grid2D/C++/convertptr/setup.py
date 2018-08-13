import os
from distutils.core import setup, Extension
name = 'ext_gridloop'

swig_cmd = 'swig -python -c++ -I. %s.i' % name
os.system(swig_cmd)

sources = ['gridloop.cpp', 'convert.cpp', 'ext_gridloop_wrap.cxx']
setup(name=name,
      ext_modules=[Extension('_' + name,  # SWIG requires _
                             sources=sources,
                             include_dirs=[os.curdir])])
