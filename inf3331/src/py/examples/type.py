#!/usr/bin/env python
import os, shutil, glob

def remove(files):
    """
    Remove one or more files and/or directories.
    """
    if isinstance(files, str): # is files a string?
        files = [files]  # convert files from a string to a list
    if not isinstance(files, list):  # is files not a list?
        raise TypeError, \
              'remove() argument 1 must be a string '\
              'or a list, not a %s' % type(files)
    for file in files:
        print 'removing',
        if os.path.isdir(file):
            shutil.rmtree(file)
            print 'directory',
        elif os.path.isfile(file):
            print 'file',
            os.remove(file)
        print file

# test the remove function:
for i in range(10):
    os.mkdir('tmp_'+str(i))
    f = open('tmp__'+str(i), 'w'); f.close()
remove('tmp_1')
remove(glob.glob('tmp_[0-9]') + glob.glob('tmp__[0-9]'))

# -----------------------------------------------------------------
class MyClass:
    def __init__(self, s):
        self.s = s
#    def __str__(self):
#        return "MyClass instance '%s'" % self.s
        
from types import *

myinst = MyClass('some input')  # instance of user-defined class
somelist = ['text', 1.28736, ['sub', 'list'],
            {'sub' : 'dictionary', 'heterogeneous' : 1},
            ('some', 'sub', 'tuple'), 888, myinst]

def typecheck_types(i):
    if type(i) == IntType:
        print 'integer'
        # work with i as integer
    elif type(i) == ListType:
        print 'list'
        # work with i as list
    elif type(i) == TupleType:
        print 'tuple'
        # work with i as tuple
    elif type(i) == DictType:
        print 'dictionary'
        # work with i as dictionary
    elif type(i) == StringType:
        print 'string'
        # work with i as string
    elif type(i) == UnicodeType:
        print '(unicode) string'
        # work with i as a unicode string
    elif type(i) == FloatType:
        print 'float'
        # work with i as float
    elif type(i) == InstanceType:
        print 'instance of user-defined class'
        # work with i as an instance
    else:
        print type(i)

def typecheck(i):
    if isinstance(i, (int, long)):
        print 'integer'
        # work with i as integer
    elif isinstance(i, list):
        print 'list'
        # work with i as list
    elif isinstance(i, tuple):
        print 'tuple'
        # work with i as tuple
    elif isinstance(i, dict):
        print 'dictionary'
        # work with i as dictionary
    elif isinstance(i, str):
        print 'string'
        # work with i as string
    elif isinstance(i, basestring):  # better than just str!
        # i is a str or a unicode string
        print 'string'
        # work with i as string
    elif isinstance(i, float):
        print 'float'
        # work with i as float
    elif isinstance(i, MyClass):
        print 'instance of user-defined class (MyClass)',
    else:
        print type(i)

def typecheck_type(i):
    if type(i) == type(1):
        print 'integer'
        # work with i as integer
    elif type(i) == type([]):
        print 'list'
        # work with i as list
    elif type(i) == type(()):
        print 'tuple'
        # work with i as tuple
    elif type(i) == type({}):
        print 'dictionary'
        # work with i as dictionary
    elif type(i) == type(''):
        print 'string'
        # work with i as string
    elif type(i) == type(u''):
        print '(unicode) string'
        # work with i as unicode string
    elif type(i) == type(1.0):
        print 'float'
        # work with i as float
    elif type(i) == type(MyClass('')):
        print '\n  instance of user-defined class'
    else:
        print type(i)
    
for i in somelist:
    print i, 'is',
    typecheck(i)
    typecheck_types(i)
    typecheck_type(i)

print 'The next call should raise an exception:'
try:
    remove(os)
except TypeError, msg:
    print 'Yes, got an exception:\n', msg
    



