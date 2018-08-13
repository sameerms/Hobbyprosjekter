# -*- coding: utf-8 -*-
import sys
import argparse
import logging
import matplotlib.pyplot as plt

#from heat_equation_numpy import heat_equation_numpy
#from heat_equation_weave import heat_equation_cpass

'''
Implement a common user interface for your Python solvers as well as for the
C-solution using the argparse module. This user-interface should offer at least
the following command line options:
• Option to specify the model parameters such as rectangle dimensions,
start-time, end-time, timestep, thermal diffusivity coefficient and constant
heat source;
• Name of an output file in which the program stores the solution at the final
time, or an input file which is loaded and used as the initial temperature1
;
• Option to save a plot of final temperature as an image;
• Option to switch between the three implementations (pure Python, Numpy,
C);
• Option to activate verbose mode, which prints what the program does.
• A switch for turning on the timeit module, which then reports important
timings at the end of the program.a
Give the options useful name and description/help messages.
'''

def define_command_line_options():
    import argparse
    parser = argparse.ArgumentParser()
    #parser.add_argument('--I', '--initial_condition', type=float,
                      #  default=1.0, help='initial condition, u(0)',
                       # metavar='I')
    
    parser.add_argument('--t0', '--start_time', type=float,
                        default=1.0, help='start time of simulation',
                        metavar='t0')
    parser.add_argument('--t1', '--end_time', type=float,
                        default=1.0, help='end time of simulation',
                        metavar='t1')
    parser.add_argument('--dt', '--timestep', type=float,
                        default=1.0, help='timestep for simulation',
                        metavar='dt')
    parser.add_argument('--n', '--dimenstions',type=int,
                        default=1.0, help='number of rows  in 2D grid',
                        metavar='n')
    parser.add_argument('--m', '--columns', type=int,
                        default=1.0, help='number of columns in 2D grid',
                        metavar='m')
    parser.add_argument('--u', type=float,
                        default=0.0, help='Intial state u ',
                        metavar='u')
    parser.add_argument('--f', type=float,
                        default=1.0, help='heat source function',
                        metavar='f')
    parser.add_argument('--nu', type=float,
                        default=1.0, help='thermal diffusivity coefficient ',
                        metavar='nu')
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),
                        default=sys.stdout)
    parser.add_argument('--makesaveplot',
                        help='makes and saves plot using numpy implementation')
    parser.add_argument('-v', '--verbose',help="Be verbose",
                        action="store_const", dest="loglevel", const=logging.INFO)
    parser.add_argument('-d', '--debug',help="Print lots of debugging statements",
                        action="store_const", dest="loglevel", const=logging.DEBUG,default=logging.WARNING)
    parser.add_argument("-implementation", "--implementation", type=str, choices=['pure', 'numpy', 'C'],
                    help="Select the implementation types between: pure , numpy  , C")
    #parser.add_argument('--dt', '--time_step_values', type=float,
                        #default=[1.0], help='time step values',
                        #metavar='dt', nargs='+', dest='dt_values')
    return parser

def read_command_line():
    parser = define_command_line_options()
    args = parser.parse_args()
    
    print 'implementation=', args.implementation
    
    #logging.basicConfig(level=args.loglevel)
    #print 't0={}, t1={}, dt={},n={},m={},nu={}, outfile={},makeplot={}'.format(
        # args.t0, args.t1, args.dt, args.n, args.m,args.nu, args.outfile,args.makeplot)
    #return args.t0, args.t1, args.dt, args.n, args.m,args.nu, args.outfile,args.makeplot


    #implementation=read_command_line()
    if args.implementation == 'pure':
        from heat_equation import HeatEqaution
        s=HeatEqaution()
        s.heat_equation(args.t0, args.t1, args.dt, args.n, args.m, args.u, args.f, args.nu)
    if args.implementation == 'numpy':
        from heat_equation_numpy import heat_equation_numpy
        heat_equation_numpy(args.t0, args.t1, args.dt, args.n, args.m, args.u, args.f, args.nu)
    if args.implementation == 'C':
        from heat_equation_weave import heat_equation_cpass
        heat_equation_cpass(args.t0, args.t1, args.dt, args.n, args.m, args.u, args.f, args.nu)
        
    if args.makesaveplot :
       print "here u go"
       from heat_equation_numpy import heat_equation_numpy
       heat_equation_numpy(args.t0, args.t1, args.dt, args.n, args.m, args.u, args.f, args.nu) 
       fig = plt.figure(1)
       img= plt.subplot(111)
       im=img.imshow(heat_equation_numpy.uNew,interpolation = 'nearest')
       fig.colorbar(im)
       plt.savefig(fig)
       
    
        
        
    
    
    
read_command_line()
    #print 'I={}, a={}, T={}, makeplot={}, dt_values={}'.format(
       # args.I, args.a, args.T, args.makeplot, args.dt_values)
    #return args.I, args.a, args.T, args.makeplot, args.dt_values
    
