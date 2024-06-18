# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 14:00:40 2020

@author: Morgan Bridge
"""

import numpy as np

def rk4(f, x0, dt):
    """Solve differential equation x'(t) = f(t,x(t))
    using 4th order Runge--Kutta with timestep dt.

    Returns a generator which yields each tn,xn.
    """
    tn = 0
    xn = x0
    
    while True:        
        # gives x0 first, then calculates xn for n>0
        yield tn, xn
        
        k1 = dt*f(tn,xn)
        k2 = dt*f(tn+dt/2,xn+k1/2)
        k3 = dt*f(tn+dt/2,xn+k2/2)
        k4 = dt*f(tn+dt,xn+k3)
    
        # use xn = xn + ... (not x += ...) so a numpy array is copied, not changed in-place
        xn = xn + (k1+2*k2+2*k3+k4)/6
        tn = tn + dt
        
        
def f(t,X):
    x,v=X
    Xdot=np.array([v,-np.sin(x)])
    return Xdot

X0=np.array([3.1,0])
dt=0.01
solver=rk4(f,X0,dt)

ts=list()
xs=list()
for ti,xi in solver:
    ts.append(ti)
    xs.append(xi)
    if ti>100.0:
        break
xs=np.array(xs)

import matplotlib.pyplot as plt
plt.plot(ts,xs[:,0])
plt.show()