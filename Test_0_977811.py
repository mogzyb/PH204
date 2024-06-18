# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 14:02:24 2020

@author: Morgan Bridge
"""

'1'
pi=3.141592653589793

cube_root_pi=pi**(1/3)


'2'
epsilon=8.854e-12
hbar = 1.054e-34
m=9.109e-31
e=1.602e-19

bohr_radius=4*pi*epsilon*hbar**2/(m*e**2)


'3'
number_of_emus=6
if number_of_emus==1:
    print("individual")
elif number_of_emus==2:
    print("pair")
else: 
    print("mob")
    

'4' 
n=35
if n%5==0 and n%7==0:
    logic=True
else:
    logic=False
