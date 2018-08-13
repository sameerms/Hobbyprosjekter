# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from pylab import *
from matplotlib.pyplot import imshow
import time




class HeatEqaution(object):
    """  
    Your implementation should be parametrised with the start time t0, the end
time t1, the time step dt, the rectangle dimensions n, m, the initial temperature
distribution u (an n × m list), a heat source function f (also a n × m list) and
the thermal diffusivity nu (a material specific parameter, a float).
Run the simulation on a 50 × 100 large rectangle, starting with u = 0 at t0 = 0
until t1 = 1000 with a timestep dt = 0.1, ν = 1 (i.e. nu=1) and f set to 1
everywhere. Plot the results using matplotlib (for example with pyplot.imshow
and pyplot.colorbar or scitools on UiO computers)
"""

    global uList;
    global uNew;   
    global maxval   
    
    def heat_equation(self,t0,t1,dt,n,m,u,f,nu):
        global uList
        global uNew
        global maxval
        dt= float(dt)
        nu=float(nu)
        
        uList= [];                                                 # creates 2D list to saves the temperature at a given time
        for row in xrange(n):uList +=[[float(u)]*m]
        fList=[]
        for row in xrange(n):fList +=[[float(f)]*m]
        
        uNew= uList                                               #copy the list before we manipulate the ulist
        
        tstart = time.time()

       
        for temp in range(t0,int(t1/dt)):
            for i in range(1,n-1):
                for j in range(1,m-1):
                    uNew[i][j] = uList[i][j]+ dt*(nu*uList[i-1][j] + nu*uList[i][j-1] - 4*nu*uList[i][j]+ nu*uList[i][j+1] + nu*uList[i+1][j] + fList[i][j])
                     
        
        tstop = time.time()
       # print uList
        print "Max value at u[25][50] :", uNew[25][50]
        maxval, i, j = max((item, i, j)  for i, row in enumerate(uNew)
                                     for j, item in enumerate(row))

        print"heat_equation max value ",(maxval)
        print " Max fount at u [i][j] = u[",i,"][",j,"]"
        
       

        print "Total time with scaler version  : ", tstop-tstart, "s"
        return uNew

"""  
update formula
u_new[i][j] = u[i][j]+ dt*(nu*u[i-1][j] + nu*u[i][j-1] - 4*nu*u[i][j]+ nu*u[i][j+1] + nu*u[i+1][j] + f[i][j])

"""   

       
       
      












s=HeatEqaution()

s.heat_equation(0,1000,0.1,50,100,0,1,1)

fig=figure(1)
img=subplot(111)
im=img.imshow(uNew,interpolation = 'nearest')
fig.colorbar(im)


s.heat_equation(0,0,0.1,50,100,0,1,1)
figure(2)
imshow(uNew,interpolation = 'nearest')
show()
close()


