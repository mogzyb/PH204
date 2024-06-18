# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:02:27 2020

@author: mogzy
"""
#1
import sympy as sp
sp.init_printing(use_unicode=True)

x,y = sp.symbols('x,y')
f = 1/(x**2+1)

integral=sp.integrate(f,(x,-sp.oo,sp.oo))

#2
g=(x-3)**3-x**3+(x+4)**2+x*y

solution=sp.solve(g.diff(x),x)