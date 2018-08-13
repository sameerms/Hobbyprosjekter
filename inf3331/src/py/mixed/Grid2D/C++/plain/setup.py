import os
from distutils.core import setup, Extension
name = 'ext_gridloop'
setup(name=name,
      ext_modules=[Extension(name,
                             sources=['gridloop.cpp'],
                             include_dirs=[os.curdir])])
