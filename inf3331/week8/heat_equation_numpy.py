import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from matplotlib.pyplot import imshow
import time


def heat_equation_numpy(t0,t1,dt,n,m,u,f,nu):
    
    global uList
    global uNew
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
    
  
    tstart= time.time()
     
    for temp in range(t0,int(t1/dt)):
        
        uNew[1:-1, 1:-1] = uList[1:-1, 1:-1] +dt*(nu* uList[:-2, 1:-1]+ nu*uList[1:-1, :-2]-4*nu*uList[1:-1, 1:-1]+nu*uList[1:-1, 2:]+ nu*uList[2:, 1:-1]+fList[1:-1, 1:-1])
    
    tfinish = time.time()
    print "Max value at uNew[25][50]:",  uNew[25][50]
    print "max with numpy" , np.nanmax(uNew)
        
  

    print "Total time using numpy : ", tfinish-tstart, "s"
    return uNew
    

"""  
update formula
u_new[i][j] = u[i][j]+ dt*(nu*u[i-1][j] + nu*u[i][j-1] - 4*nu*u[i][j]+ nu*u[i][j+1] + nu*u[i+1][j] + f[i][j])

""" 

heat_equation_numpy(0,1000,0.1,50,100,0,1,1)

fig=figure(1)
img=subplot(111)
im=img.imshow(uNew,interpolation = 'nearest')
fig.colorbar(im)

heat_equation_numpy(0,0,0.1,50,100,0,1,1)
figure(2)
imshow(uNew,interpolation = 'nearest')

show()
time.sleep(60)
close('all')
sys.exit()
