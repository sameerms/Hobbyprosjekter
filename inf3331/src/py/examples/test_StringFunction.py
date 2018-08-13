#!/usr/bin/env python

from py4cs.StringFunction import StringFunction1
import unittest

class TestStringFunction1(unittest.TestCase):
    """Test the StringFunction1 class."""
    
    def setUp(self):
        # initializations for each test go here...
        return

    def test_plain1(self):
        f = StringFunction1('1+2*x')
        v = f(2)
        self.failUnlessEqual(v, 5, 'wrong value')

    def test_plain2(self):
        f = StringFunction1('sin(3*x) + log(1+x)')
        v = f(2.0)
        self.failUnlessAlmostEqual(v, 0.81919679046918392, 6,
                                   'wrong value')

    def test_independent_variable_t(self):
        f = StringFunction1('1+t', independent_variable='t')
        v = '%.2f' % f(1.2)
        self.failUnlessEqual(v, '2.20', 'wrong value')

    def test_independent_variable_z(self):
        f = StringFunction1('1+z')
        self.failUnlessRaises(NameError, f, 1.2)

    def test_set_parameters(self):
        f = StringFunction1('a+b*x', a=1)
        f.set_parameters(b=4)
        v = f(2)
        self.failUnlessEqual(v, 9, 'wrong value')
        
if __name__ == '__main__':
    unittest.main()
