# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 15:20:26 2020

@author: Morgan Bridge
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp # 1
from scipy.constants import proton_mass,e

k=1e4
q=e 
m=40*proton_mass

b=np.array([0,0,1])
def f(t,X):
    x,y,z,vx,vy,vz=X
    vbx,vby,vbz=np.cross([vx,vy,vz],b)
    Xdot=np.array([vx,vy,vz,(k*q*x+q*vbx)/m,(k*q*y+q*vby)/m,(k*q*-2*z+q*vbz)/m])
    return Xdot

r=0.001+0.0001*np.random.randn(1)
v=100
thetax=2*np.pi*np.random.random_sample(1)
phix=np.pi*np.random.random_sample(1)
thetav=2*np.pi*np.random.random_sample(1)
phiv=np.pi*np.random.random_sample(1)

x=r*np.cos(thetax)*np.sin(phix)
y=r*np.sin(thetax)*np.sin(phix)
z=r*np.cos(phix)
vx=v*np.cos(thetav)*np.sin(phiv)
vy=v*np.sin(thetav)*np.sin(phiv)
vz=v*np.cos(phiv)

X0 = np.array([x[0],y[0],z[0],vx[0],vy[0],vz[0]])
ts=np.linspace(0,1e-3,10001)
solution = solve_ivp(f, [0, 1e-3], X0,t_eval=ts) # 2

ts = solution.t                       # 3
ys = solution.y.T                     # 4

plt.plot(ys[:,0],ys[:,1])

# 

# from scipy.optimize import newton
# def f(x): return randno**2-x**2

# solution = newton(f,0.001)

