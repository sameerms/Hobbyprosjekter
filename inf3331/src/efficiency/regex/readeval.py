#!/usr/bin/env python
import re, sys, math
from py4cs.numpytools import *
f = open(sys.argv[1], 'r')
a = eval(f.read())
print "a[1,1,3]=",a[1,1,3]
