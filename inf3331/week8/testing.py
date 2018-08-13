
import time
from math import *
#from heat_equation import HeatEqaution

import numpy as np

def source_term_change(t0,t1,dt,n,m,u,nu):
    global uList
    global uNew
    global uAna
    shape=(n,m)
    uVal=u
   
    dty=float
    
    uList=np.empty(shape,dtype=dty)
    uList.fill(uVal)
    
    uNew=uList
    uAna=uList
    analytic_u=np.empty_like(uNew)
    f=np.empty_like(uNew)
    
    for i in range(0,n-1):
        for j in range(0,m-1):
            f[i][j] =  nu*((2*pi/(m-1))**2 + (2*pi/(n-1))**2)*sin(2*pi/(n-1)*i)*sin(2*pi/(m-1)*j)
            analytic_u[i][j] = sin(2*pi/(n-1)*i)*sin(2*pi/(m-1)*j)
            
    tstart= time.time()
     
    for temp in range(t0,int(t1/dt)):
        uNew[1:-1, 1:-1] = uList[1:-1, 1:-1] +dt*(nu* uList[:-2, 1:-1]+ nu*uList[1:-1, :-2]-4*nu*uList[1:-1, 1:-1]+nu*uList[1:-1, 2:]+ nu*uList[2:, 1:-1]+f[1:-1, 1:-1])
       
    tfinish = time.time()
    print "Total time using numpy : ", tfinish-tstart, "s"
    err = (abs(uNew - analytic_u)).max()
    print "error is ", err
    
   


source_term_change(0,1000,0.1,50,100,0,1) 

source_term_change(0,1000,0.1,70,140,0,1)         # error decreases with higher 2D matrix dimension 
                                                    # please do the test separately other wise the error variable will get added with new value and might show different results
                                                

    