from distutils.core import setup, Extension
import os

name = 'ext_gridloop'
setup(name=name,
      include_dirs=[os.path.join(os.environ['scripting'],
                                'src', 'C')],
      ext_modules=[Extension(name, ['gridloop1_C.c', 'gridloop1_wrap.c'])])
