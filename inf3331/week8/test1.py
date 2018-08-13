
import time
from math import *
#from heat_equation import HeatEqaution
from collections import Counter
import numpy

def source_term_change(t0,t1,dt,n,m,u,nu):
    
    
    global uList
    global uNew
    global maxvaluNew
    dt= float(dt)
    nu=float(nu)
    
    uList= [];                                                 # creates 2D list to saves the temperature at a given time
    for row in xrange(n):uList +=[[float(u)]*m]


    uNew= uList                                               #copy the list before we manipulate the ulist
        
    tstart = time.time()

   
    for temp in range(t0,int(t1/dt)):
        for i in range(0,n-1):
            for j in range(0,m-1):
                uNew[i][j] = uList[i][j]+ dt*(nu*uList[i-1][j] + nu*uList[i][j-1] - 4*nu*uList[i][j]+ nu*uList[i][j+1] + nu*uList[i+1][j] + (nu*((2*pi/n)**2 + (2*pi/m)**2)*sin(2*pi/m*i)*sin(2*pi/n*j)))
                 
    
    tstop = time.time()
   # print uList
   # print "Max value :", uNew[25][50]
    
    maxvaluNew, i, j = max((item, i, j)  for i, row in enumerate(uNew)
                                     for j, item in enumerate(row))

    print"u max value ",(maxvaluNew)
    print " Max fount at u [i][j] = u[",i,"][",j,"]"
# 88.0

    
# (2, 7)
   # Unew_max=max(uNew)
   # print "unew list max",Unew_max
   

    print "Total time with func term change version  : ", tstop-tstart, "s"
    
def analytical_solution(t0,t1,dt,n,m,u,nu):
    global uList
    global analytic_u
    global maxvalanalytic_u
    dt= float(dt)
    nu=float(nu)
    
    uList= [];                                                 # creates 2D list to saves the temperature at a given time
    for row in xrange(n):uList +=[[float(u)]*m]


    analytic_u= uList                                               #copy the list before we manipulate the ulist
        
    tstart = time.time()

   
    for temp in range(t0,int(t1/dt)):
        for i in range(0,n-1):
            for j in range(0,m-1):
                #uNew[i][j] = uList[i][j]+ dt*(nu*uList[i-1][j] + nu*uList[i][j-1] - 4*nu*uList[i][j]+ nu*uList[i][j+1] + nu*uList[i+1][j] + (nu*((2*pi/n)**2 + (2*pi/m)**2)*sin(2*pi/m*i)*sin(2*pi/n*j)))
                analytic_u[i][j] = sin(2*pi/(n-1)*i)*sin(2*pi/(m-1)*j)

    
    tstop = time.time()
   # print uList
   # print "Max value analytic :", analytic_u[25][50]
    
  
   

   
    
    
    
    
    maxvalanalytic_u, i, j = max((item, i, j)  for i, row in enumerate(analytic_u)
                                     for j, item in enumerate(row))

    print"u analytic max ",(maxvalanalytic_u)
# 88.0

    print " Max fount at u [i][j] = u[",i,"][",j,"]"
    
    print "Total time with analytil_u version  : ", tstop-tstart, "s"
    #Uana_max=max(analytic_u)
   
    #print "uana max list",Uana_max,
    
   # err = (abs(uNew - analytic_u)).max()
   # print "Error anaylytic ",err 
    
    
'''
f[i][j] = nu*((2*pi/n)**2 + (2*pi/m)**2)*sin(2*pi/m*i)*sin(2*pi/n*j)
analytic_u[i][j] = sin(2*pi/(n-1)*i)*sin(2*pi/(m-1)*j)


source_term_change(0,1000,0.1,50,100,0,1)   
analytical_solution(0,1000,0.1,50,100,0,1)     
err = abs(maxvaluNew - maxvalanalytic_u)
print "error",err
a=numpy.empty_like(uNew)
b=numpy.empty_like(analytic_u)
print a[25][50]
print b[25][50]
error = (abs(a-b)).max()
print "errorright",error
'''

#s=HeatEqaution()
#errold = abs(s.maxval - maxvalanalytic_u)
#print "errorold",errold
while(t0<=t1){
        t0=t0+t1;
code = """
    int i, j;
    for( t0=0;t0<t1;t0=t0+dt){
        for (i=1; i<n-1; i++) {
           for (j=1; j<m-1; j++) {
               uNew[i][j] = uList[i][j]+ dt*(nu*uList[i-1][j] + nu*uList[i][j-1] - 4*nu*uList[i][j]+ nu*uList[i][j+1] + nu*uList[i+1][j] + fList[i][j]);
             }        
       }
    }
    """
    weave.inline(code, ['t0', 't1', 'dt', 'n','m', 'uVal','fVal', 'nu'])
    
    