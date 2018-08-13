#!/usr/bin/env python

import Tkinter
import os, sys
import Pmw
from py4cs.FuncDependenceViz import FuncDependenceViz        

if __name__ == '__main__':
    import math
    p_intervals = {'mu': (0,8), 'sigma': (0,1), 'alpha': (0,1)}

    # recall that lambda is a reserved keyword in Python,
    # use lambda_ instead:
    def lognormal(x, lambda_, zeta):
        if x < 1.0E-9:
            f = 0.0
        else:
            f = 1/(zeta*math.sqrt(2*math.pi)*x)*math.exp(
                -0.5*((math.log(x)-lambda_)/zeta)**2)
        return f

    def U(x, p):
        mu = p['mu']; sigma = p['sigma']
        zeta = math.sqrt(math.log(1 + (sigma/mu)**2))
        lambda_ = math.log(mu) - 0.5*0.5*zeta**2
        return lognormal(x, lambda_, zeta)
    
    def F(x, p):
        mu = p['mu']; sigma = p['mu']; alpha = p['alpha']
        zeta = math.sqrt(math.log(1 + (sigma/mu)**2))
        lambda_ = math.log(mu) - 0.5*0.5*zeta**2
        # response modification:
        lambda_ = math.log(alpha) + 2*lambda_
        zeta = 2*zeta
        return lognormal(x, lambda_, zeta)

    f = { 'U': U, 'F': F }   # function names and objects

    root=Tkinter.Tk()
    Pmw.initialise(root)
    try:
        viztool = sys.argv[1]
    except:
        viztool = 'gnuplot'  # alternative: Pmw.Blt.Graph
    try:
        update = sys.argv[2]
    except:
        update = 'after'  # alternative: arbitrary (cont. update)
    gui = FuncDependenceViz(root, p_intervals, f,
                            xmin=0, xmax=8,
                            resolution=40,
                            viztool=viztool,
                            plot_update=update)
    root.mainloop()
# end
