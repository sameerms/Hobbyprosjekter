import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from matplotlib.pyplot import imshow
import time
from scipy import weave
import scipy.weave

def heat_equation_cpass(t0,t1,dt,n,m,u,f,nu):
    
    global uList
    global uNew
    global fList
   
    
    shape=(n,m)
    uVal=u
    fVal=f
    dty=float
    
    uList=np.empty(shape,dtype=dty)
    uList.fill(uVal)
   # print uList
   
    uNew=uList
   
    
    fList=np.empty(shape,dtype=dty)
    fList.fill(fVal)
  #  print fList
    temp= uList
    
 
    tstart= time.time()
    for temp in range(t0,int(t1/dt)):
        
        expr = "uNew[1:-1, 1:-1] = uList[1:-1, 1:-1] +dt*(nu* uList[:-2, 1:-1]+ nu*uList[1:-1, :-2]-4*nu*uList[1:-1, 1:-1]+nu*uList[1:-1, 2:]+ nu*uList[2:, 1:-1]+fList[1:-1, 1:-1])"   
        weave.blitz(expr)
    
    
    
    tfinish = time.time()   
   
    print "Value at u[25][50] :", uNew[25][50]
    print "max with numpy array uNew" , np.nanmax(uNew)
    print "Total time using numpy and weave: ", tfinish-tstart, "s"
    return uNew
    
    
heat_equation_cpass(0,1000,0.1,50,100,0,1,1)   


fig=figure(1)
img=subplot(111)
im=img.imshow(uNew,interpolation = 'nearest')
fig.colorbar(im)
show()
plt.close() 
    
