# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 17:08:21 2020

@author: Morgan Bridge
"""
game=[]
for n in range(1,1001):
        
        if n%3==0 and n%5==0:
            game.append("zig zag")
        elif n%3==0:
            game.append("zig")
        elif n%5==0:
            game.append("zag")
        else:
           game.append(n)