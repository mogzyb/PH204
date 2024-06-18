# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 14:06:23 2020

@author: Morgan Bridge
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp # 1

b=np.array([0,0,1])

def f(t,X):
    x,y,z,vx,vy,vz=X
    ax,ay,az=np.cross([vx,vy,vz],b)
    Xdot=np.array([vx,vy,vz,ax,ay,az])
    return Xdot

X0 = np.array([0,0,0,1,0,0])
ts=np.linspace(0,10,10001)
solution = solve_ivp(f, [0, 10], X0,t_eval=ts) # 2

ts = solution.t                       # 3
ys = solution.y.T                     # 4

plt.plot(ys[:,0],ys[:,1])