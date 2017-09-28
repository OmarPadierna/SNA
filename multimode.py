#!usr/bin/python
# encoding: utf-8

"""
Created by Omar Padierna on 2016-01-02.
Copyright (c) 2015 __Venturez.com__. All rights reserved.
Modified from Maksim Tsvetovat 2011-08-17.
"""

import networkx as net
from collections import defaultdict
import math
def plot_multimode(m,layout=net.circular_layout, type_string='type', sizing=dict(), with_labels=True):

    ## create a default color order and an empty color-map
    colors=['r','g','b','c','m','y','k']
    colormap={}
    d=sizing  #we use degree for sizing nodes
    pos=layout(m)  #compute layout 
    
    #Now we need to find groups of nodes that need to be colored differently
    nodesets=defaultdict(list)
    
    for n in m.nodes():
        try:
            t=m.node[n][type_string]
           
        except KeyError:
            ##this happens if a node doesn't have a type_string -- give it a None value
            t=1
        nodesets[t].append(n)
    
    ## Draw each group of nodes separately, using its own color settings
 
    i=0
    for key in nodesets.keys():
        ns=[d[n]*5 for n in nodesets[key]]
        net.draw_networkx_nodes(m,pos,nodelist=nodesets[key], node_size=ns, node_color=colors[i], alpha=0.6)
        colormap[key]=colors[i]
        i+=1
        if i==len(colors): 
            i=0  ### wrap around the colormap if we run out of colors

    edgelisty=m.edges(data=True) 
    ## Draw edges using a default drawing mechanism
    weights_dict=[]
    weights=[]
    edgery=[]
    n=0
    for n in range (0, len(edgelisty)): 
        paquete=edgelisty[n]
        edge=(paquete[0],paquete[1])
        edgery.append(edge)
        weights_dict.append(paquete[2])
        n=n+1
    
    n=0
    
    
    for n in range (0, len(weights_dict)):
        temp=weights_dict[n]
        weights.append(math.log(temp['weight']))
        n=n+1
 
    net.draw_networkx_edges(m,pos,width=weights,alpha=1, edgelist=edgery)  
    
   
    if with_labels: 
        net.draw_networkx_labels(m,pos,font_size=12)
    
   