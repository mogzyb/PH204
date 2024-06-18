# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 15:09:41 2020

@author: Morgan Bridge
"""

def rover(locations):

    distance={}
    locs=[]
    order_to_visit=[]
    home=[0,0]
    
    i=len(locations)
    
    for x in range(i):
        distance={}
        locs=[]
        for x in locations:
            locs=[x]
            def path_length(locs):
                def pair_distance(a,b): return sum([(ai-bi)**2 for ai,bi in zip(a,b)])**0.5
                return sum([pair_distance(a,b) for a,b in zip([home]+ locs,locs)])
        
            distance[x]=path_length(locs)
            
        sorted_distance=sorted(distance.items(), key=lambda x: x[1], reverse=False)
        home=sorted_distance[0][0]
        order_to_visit.append(sorted_distance[0][0])
        locations.remove(sorted_distance[0][0])

    import matplotlib.pyplot as plt
    plt.figure()
    for loc in locations:
        plt.plot(loc[0],loc[1],'r*')
        
    
    xs = [loc[0] for loc in order_to_visit]
    ys = [loc[1] for loc in order_to_visit]
    plt.plot(xs,ys,'k')
    plt.show()

    return order_to_visit
