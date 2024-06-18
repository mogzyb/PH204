# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 17:37:17 2020

@author: Morgan Bridge
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp 

alpha=1.1
beta=0.4
gamma=0.4
delta=0.1

def f(t,X):
    x,y=X
    Xdot=alpha*x-beta*y*x
    Ydot=delta*x*y-gamma*y
    return Xdot, Ydot

X0 = np.array([10,10])
ts=np.linspace(0,100,1001)
solution = solve_ivp(f, [0, 100], X0,t_eval=ts) 

ts = solution.t
xs = solution.y.T[:,0]                         
ys = solution.y.T[:,1]


plt.plot(ts,ys)
plt.plot(ts,xs)
#plt.plot(xs,ys)