#!/usr/bin/env python
"""
Module for estimating convergence rate of numerical algorithms,
based on data from a set of experiments.
"""

from Scientific.Functions.LeastSquares import leastSquaresFit
from py4cs.numpytools import *
import Gnuplot, time

# The classes in this module have only static methods, i.e.,
# they are merely name spaces for related functions.

class ManyDiscretizationPrm(object):
    """
    General tool for fitting an error model containing an
    arbitrary number of discretization parameters.
    The error is a weighted sum of each discretization parameter
    raised to a real expoenent. The weights and exponents are
    the unknown parameters to be fitted by a nonlinear
    least squares procedure.
    """
    
    def error_model(p, d):
        """
        Evaluate the theoretical error model:
        e = error_model(p, d)
        p    : sequence of parameters (to be estimated)
        d    : sequence of (known) discretization parameters
        e    : error
        len(p) must be 2*len(d) in this model
        """
        if len(p) != 2*len(d):
            raise ValueError, 'len(p)=%d != 2*len(d)=%d' % (len(p),2*len(d))
        sum = 0
        for i in range(len(d)):
            sum += p[2*i] * d[i]**p[2*i+1]
        return sum

    def nonlinear_fit(d, e, initial_guess):
        """
        d   : list of values of the set of discretization
              parameters in each experiment:
              d = ((d_1,d_2,d_3),(d_1,d_2,d_3,),...)
              d[i] provides the values of the discretization
              parameters in experiement no. i
        e   : list of error values; e = (e_1, e_2, ...)
              e[i] is the error associated with the parameters
              d[i]

        initial_guess is the starting value for the unknown
        parameters vector.
        """
        if len(d) != len(e):
            raise ValueError, 'len(d) != len(e)'
        # transform d and e to the data format required by
        # the Scientific package:
        data = []
        for d_i, e_i in zip(d, e):
            if isinstance(d_i, (float, int)):
                data.append(((d_i,), e_i))
            else:  # d_i is tuple, list, array, NumArray, ...
                data.append((d_i, e_i))
        sol = leastSquaresFit(ManyDiscretizationPrm.error_model,
                              initial_guess, data)
        # return list of fitted parameters (p in error_model)
        # (sol[1] is a measure of the quality of the fit)
        return sol[0]  

    error_model = staticmethod(error_model)
    nonlinear_fit = staticmethod(nonlinear_fit)

class OneDiscretizationPrm(object):
    """
    Tools for fitting an error model with only one discretization
    parameter: e = C*h^2.
    """
    
    def error_model(p, d):
        """e = C*h**a"""
        C, a = p
        h = d[0]
        return C*h**a

    def loglog_error_model(p, d):
        """Requires log-log data."""
        C, a = p
        h = d[0]
        return log(C) + a*log(h)


    def linear_loglog_fit(d, e):
        """
        Linear least squares algorithm.
        Suitable for problems with only one distinct
        discretization parameter.

        d  : sequence of discretization parameter values
        e  : sequence of corresponding error values

        The error model the data is supposed to fit reads
        e[i] = log(C[i]) + a*log(d[i])
        """
        A = transpose(array([d, zeros(len(d), Float)+1]))
        sol = LinearAlgebra.linear_least_squares(A, e)
        a, logC = sol[0]
        C = exp(logC)
        return a, C

    def nonlinear_fit(d, e, initial_guess):
        """
        d   : list of values of the (single) discretization
              parameter in each experiment:
              d[i] provides the values of the discretization
              parameter in experiement no. i
        e   : list of error values; e = (e_1, e_2, ...)
              e[i] is the error associated with the parameters
              d[i]

        initial_guess is the starting value for the unknown
        parameters vector.
        """
        if len(d) != len(e):
            raise ValueError, 'd and e must have the same length'
        if not isinstance(d[0], (float,int)):
            raise TypeError, \
            'd must be an array of numbers, not %s' % str(type(d[0]))
        # transform d and e to the data format required by
        # the Scientific package:
        data = []
        for d_i, e_i in zip(d, e):
            data.append(((d_i,) , e_i))  # recall (a,) conversion to tuple
        sol = leastSquaresFit(OneDiscretizationPrm.error_model,
                              initial_guess, data)
        return sol[0]


    def pairwise_rates(d, e):
        """
        Compare convergence rates, where each rate is based on
        a formula for two successive experiments.
        """
        if len(d) != len(e):
            raise ValueError, 'd and e must have the same length'
        
        rates = []
        for i in range(1, len(d)):
            rates.append( log(e[i-1]/e[i])/log(d[i-1]/d[i]) )
        # estimate C from the last data point:
        C = e[-1]/d[-1]**rates[-1]
        return rates, C

    def analyze(d, e, initial_guess=None,
                plot_title='', filename='tmp.ps'):
        """
        Run linear, nonlinear and successive rates models.
        Plot results.
        """
        # convert to NumPy arrays:
        d = array(d, Float);  e = array(e, Float)

        # linear least squares fit:
        a, C = OneDiscretizationPrm.linear_loglog_fit(log(d), log(e))
        print "linear LS fit: const=%e rate=%.1f" % (C, a)

        # nonlinear least squares fit (no log-log):
        C2, a2 = OneDiscretizationPrm.nonlinear_fit(d, e, initial_guess)
        print "nonlinear LS fit: const=%e rate=%.1f" % (C2, a2)

        # pairwise estimate of the rate:
        rates, C3 = OneDiscretizationPrm.pairwise_rates(d, e)
        a3 = rates[-1]
        print "pairwise fit: const=%e rate=%.1f" % (C3, a3)
        print "all rates:", rates
        # Note that one_discrprm... returns a, C while the other
        # function returns C, a. The linear least squares fit is fixed,
        # and the other has the parameter sequence defined in the
        # error model.

        # C*h^r plot:
        if 0:
            g1 = Gnuplot.Gnuplot(persist=1)
            g1('set key left box')
            g1('set pointsize 2')
            g1('set title "%s"' % plot_title)
            data = Gnuplot.Data(d, e,
                                with='points', title='data')
            fit1 = Gnuplot.Func('%(C)g*x**%(a)g' % vars(),
                                with='lines',
                                title='linear log-log least-squares fit')
            fit2 = Gnuplot.Func('%(C2)g*x**%(a2)g' % vars(),
                                with='lines',
                                title='nonlinear direct least-squares fit')
            fit3 = Gnuplot.Func('%(C3)g*x**%(a3)g' % vars(),
                                with='lines',
                                title='successive rates; two last experiments')
            g1.plot(data, fit1, fit2, fit3)
            time.sleep(2)

        # log-log plot:
        g2 = Gnuplot.Gnuplot(persist=1)
        g2('set key left box')
        g2('set pointsize 2')
        g2('set title "%s"' % plot_title)
        data = Gnuplot.Data(log(d), log(e),
                            with='points', title='data')
        fit1 = Gnuplot.Func('%g + %g*x' % (log(C), a),
                            with='lines',
        title='linear log-log least-squares fit: %.1f*h^%.1f' % (log(C), a))
        fit2 = Gnuplot.Func('%g + %g*x' % (log(C2), a2),
                            with='lines',
        title='nonlinear direct least-squares fit: %.1f*h^%.1f' % (log(C2), a2))
        fit3 = Gnuplot.Func('%g + %g*x' % (log(C3), a3),
                            with='lines',
        title='successive rates; two last experiments: %.1f*h^%.1f' % (log(C3), a3))
        g2.plot(data, fit1, fit2, fit3)
        g2.hardcopy(filename=filename, enhanced=1, mode='eps',
                    color=0, fontname='Times-Roman', fontsize=18)
        time.sleep(2)
        

    error_model = staticmethod(error_model)
    loglog_error_model = staticmethod(loglog_error_model)
    linear_loglog_fit = staticmethod(linear_loglog_fit)
    nonlinear_fit = staticmethod(nonlinear_fit)
    pairwise_rates = staticmethod(pairwise_rates)
    analyze = staticmethod(analyze)

# no need for this one?
def many_discrprm_log_fit(d, e, factors):
    """
    Linear least squares algorithm.
    Suitable for problems with a common
    discretization parameter, i.e., a common
    convergence rate for each parameter.
    Only the exponent can be estimated.
    
    d  : sequence of the main discretization parameter values
    e  : sequence of corresponding error values
    factors : multiply factors[j]*d[i][j] such that
              the rate gets the same

    The error model the data is supposed to fit reads
    e[i] = log(C[i]) + a*log(d[i])
    """
    # not ready, just a copy:
    A = transpose(array([d, zeros(len(d), Float)+1]))
    sol = LinearAlgebra.linear_least_squares(A, e)
    a, logC = sol[0]
    C = exp(logC)
    return a, C


import random
def _test1():
    """Single discretization parameter test."""
    random.seed(1234)
    n = 7
    h = 1
    e = [];  d = []
    for i in range(7):
        h /= 2.0
        error = OneDiscretizationPrm.error_model((4,2), (h,))
        error += random.gauss(0, 0.1*error)  # perturb data
        d.append(h)
        e.append(error)
    OneDiscretizationPrm.analyze(d, e, initial_guess=(3,2))

# missing tasks:
# example with dx, dy and dt
# same example, but with factors to get a common rate
# dx, dt tables and experiments with whole table, one
# column and one row, and the diagonal

if __name__ == '__main__':
    _test1()
    
    
