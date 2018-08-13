#!/usr/bin/env python

import os, re
from py4cs.numpytools import *
import py4cs.misc
from py4cs.PrmDictBase import PrmDictBase

class SomeSolver(PrmDictBase):
    def __init__(self, **kwargs):
        # register parameters:
        PrmDictBase.__init__(self)
        self.physical_prm = {'density': 1.0, 'Cp': 1.0,
                                   'k': 1.0, 'L': 1.0}
        self.numerical_prm =  {'n': 10, 'dt': 0.1, 'tstop': 3}
        self._prm_list = [self.physical_prm, self.numerical_prm]
        self._type_check.update({'n': True, 'dt': (float,)})
        self.user_prm = None # no extra user parameters
        self.set(**kwargs)

    def _update(self):
        n = self.numerical_prm['n']
        L = self.physical_prm['L']
        k = self.physical_prm['k']

        self.u = zeros(n+1, Float)
        h = L/float(n)
        dt_limit = h**2/(2*k)
        if self.numerical_prm['dt'] > dt_limit:
            self.numerical_prm['dt'] = dt_limit

    def test_short_forms(self):
        """
        # this doesn't work with locals():
        self.dicts2namespace(locals(), self._prm_list)
        print 'local variables:', locals()
        try:
            print 'n =', n
        except NameError, msg:
            print msg
        self.namespace2dicts(locals(), self._prm_list) # clean up

        # exec with locals() from this function: (doesn't work)
        self.dicts2namespace2(locals(), self._prm_list)
        try:
            print 'after exec: n =', n
        except NameError, msg:
            print msg
        # no clean up

        # this works fine:
        exec '%s=%s' % ('n', repr(self.numerical_prm['n']))
        try:
            print 'after local exec: n =', n
        except NameError, msg:
            print msg

        # manipulate locals() here:
        locals()['Cp'] = 1.1
        try:
            print 'locals()[..] modification, Cp =', Cp
        except NameError, msg:
            print msg
        """
        # globals() work:
        self.dicts2namespace(globals(), self._prm_list)
        #kk = globals().keys(); kk.sort(lambda a,b: cmp(a.lower(),b.lower()))
        #print kk
        print 'dt =', dt
        self.namespace2dicts(globals(), self._prm_list) # clean up

        # can make attributes too:
        self.dicts2namespace(self.__dict__, self._prm_list)
        print 'self.n =', self.n
        print 'self.dt =', self.dt
        self.namespace2dicts(self.__dict__, self._prm_list) # clean up

        # exec in a special dictionary:
        mydict = {}
        self.dicts2namespace(mydict, self._prm_list)
        code = """\
print 'Cp=', Cp, 'n=', 'L=', L"""
        exec code in globals(), mydict
        # safe
        

def _test1():
    s = SomeSolver(k=2)
    s.set(Cp=0.1, n=100)
    s.set()  # usage message
    print 'is s extensible?', s.user_prm is dict
    try:
        s.set(q=0.1, m=100)
    except NameError, msg:
        print msg
    s.user_prm = {}
    print 'is s extensible?', s.user_prm is dict
    s.set(q=0.1, m=100)
    s.properties(globals())
    print 's.m:', s.m
    print 's.Cp:', s.Cp
    print 's.L:', s.L
    try:
        s.Cp = 0.1
    except AttributeError, msg:
        print msg
    s.dicts2namespace(locals(), s._prm_list)
    print 'local variables:', locals()
    # cannot access L, Cp, ... :-(
    s.test_short_forms()
    
if __name__ == '__main__':
    _test1()
                            
