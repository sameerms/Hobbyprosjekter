#!/usr/bin/env python

class MySeq:
    def __init__(self, *data):
        self.data = data

    def __iter__(self):
        return MySeqIterator(self.data)

class MySeqIterator:
    def __init__(self, data):
        self.index = 0
        self.data = data

    def next(self):
        if self.index < len(self.data):
            item = self.data[self.index]
            self.index += 1  # ready for next call
            return item
        else:  # out of bounds
            raise StopIteration

class MySeq2:
    def __init__(self, *data):
        self.data = data

    def __iter__(self):
        self.index = 0
        return self

    def next(self):
        if self.index < len(self.data):
            item = self.data[self.index]
            self.index += 1  # ready for next call
            return item
        else:  # out of bounds
            raise StopIteration

print 'manually coded iteration:'
obj = MySeq(1, 9, 3, 4)
iterator = iter(obj)   # iter(obj) means obj.__iter__()
while True:
    try:
        item = iterator.next()
    except StopIteration:
        break
    # process item:
    print item

print 'the equivalent for loop:'
for item in obj:
    print item,
print


print 'with MySeq2:'
obj = MySeq2(1, 9, 3, 4)
for item in obj:
    print item


# generator version:
class MySeq3:
    def __init__(self, *data):
        self.data = data

def items(obj):
    for item in obj.data:
        yield item

print 'using a generator function items:'
for item in items(obj):
    print item

class MySeq4:
    def __init__(self, *data):
        self.data = data

    def __iter__(self):
        for item in obj.data:
            yield item

print 'generator version of __iter__:'
obj = MySeq4(1,2,3,4,6,1)
for item in obj:
    print item

# generate power functions:
def power_functions(limit=10000):
    i = 0
    while i < limit:
        code = """
def f(x):
    return x**%d
""" % i
        exec code
        i += 1
        yield f

print 'x^i functions:'
x = 1.2
limit = 6
for f in power_functions(limit):
    print f(x)
print 'should have', [x**i for i in range(limit)]


# rewrite generators in terms of ordinary functions with lists:
from math import sin, cos, pi
def circle1(np):
    """Return np points (x,y) equally spaced on the unit circle."""
    da = 2*pi/np
    for i in range(np+1):
        yield (cos(i*da), sin(i*da))

def circle2(np):
    da = 2*pi/np
    points = []
    for i in range(np+1):
        points.append((cos(i*da), sin(i*da)))
    return points

def circle3(np):
    da = 2*pi/np
    return [(cos(i*da), sin(i*da)) for i in range(np+1)]

print '\npoints on a circle:'
for x,y in circle1(4):
    print x,y

for x,y in circle2(4):
    print x,y

for x,y in circle3(4):
    print x,y

