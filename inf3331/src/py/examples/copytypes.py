#!/usr/bin/env python
import copy

# number objects:
a = -99
b = a    # b becomes a copy of a
a = 999
print b  # b is still -99

# strings:
a = '-99'
b = a    # b becomes a copy of a
a = '999'
print b  # b is still '-99'

# user-defined objects:
class A:
    def __init__(self, value=None):
        self.value = value
    def __str__(self):
        return 'value=%s' % str(self.value)
    def __repr__(self):
        return self.__str__()

a = A(-99)
b_assign  = a
b_shallow = copy.copy(a)
b_deep    = copy.deepcopy(a)
a.value = 999
print '\nassignment:', b_assign, '\nshallow:',\
      b_shallow, '\ndeep:', b_deep

a = A([-99])
b_assign  = a
b_shallow = copy.copy(a)
b_deep    = copy.deepcopy(a)
a.value[0] = 999
print '\nassignment:', b_assign, '\nshallow:',\
      b_shallow, '\ndeep:', b_deep

# lists:
a = [4,3,5,['some string',-99], A(-99)]
b_assign  = a
b_shallow = copy.copy(a)
b_deep    = copy.deepcopy(a)
b_slice   = a[0:5]
a[3] = 999; a[4].value = 999
print '\nassignment:', b_assign, '\nshallow:', b_shallow,\
      '\ndeep:', b_deep, '\nslice:', b_slice

# dictionaries behave similarly:
a = {'key1' : -99, 'key2' : ('something else', 8, A(-99))}
b_assign  = a
b_shallow = copy.copy(a)
b_deep    = copy.deepcopy(a)
a['key1'] = 999;  a['key2'][2].value = 999
print '\nassignment:', b_assign, '\nshallow:', b_shallow,\
      '\ndeep:', b_deep

# (tuple example does not make sense here; you cannot
# change the items in a tuple)
