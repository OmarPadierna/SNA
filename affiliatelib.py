#!usr/bin/python
# encoding: utf-8

"""
Created by Omar Padierna on 2015-12-17.
Copyright (c) 2015 __Venturez.com__. All rights reserved.
Modified from Maksim Tsvetovat on 2011-08-17.
"""
##Import all required libraries
import math
import csv 
import networkx as net
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import Tkinter as Tk
from Tkinter import *
from tkMessageBox import showinfo
import multimode as mm
import triadic
## Import bi-partite (bi-modal) functions
from networkx.algorithms import bipartite as bi
##Libraries below were made specifically for this project
##Source files must be in the same working directory
from Edgesize import getweight
from TopicSize import nodesizing



###########################################################################
'''
This library defines a function called affiliation. Its only purpose
is to read a source file and generate an affiliation network 
between two columns in the file. For this project specifically, is 
users and topics. Data file must be in the same working directory

The function returns a graph, a list of users, a list of topics
and a dictionary with the number of questions as value and the topic or user as keys

'''
###########################################################################
def affiliation():
## Read the data from a CSV file
## We use the Universal new-line mode since many CSV files are created with Excel
    r=csv.reader(open('campaign_short.csv','rU'))
    
    
    ## 2-mode graphs are usually directed. Here, their direction implies number of questions
    g=net.Graph()
    
    ## we need to keep track separately of nodes of all types 
    topicz=[]
    userz=[]
    
    ## Iterate through the CSV and relate user with topic.  
    for row in r: 
        ## Topic's column is column 3 (the fourth) and user's column is 0  
        if row[0] not in userz:
            userz.append(row[0])
        if row[3] not in topicz:
            ## Make sure the field is not empty
            if row[3] is not '':
                topicz.append(row[3])
        if row[3] is not '':
            ## Call getweight function to calculate the number of questions a user made for each topic
            weightly=getweight(usery=row[0], topicly=row[3])
            ## Connect user with topic        
            g.add_edge(row[3], row[0], weight=weightly)
    

    ## Go through the network and assign the attribute 'questions' to each node
               
    for n in g.nodes_iter(): g.node[n]['questions']='None' 
    ## call function nodesizing to get the number of questions per node
    ## for topic nodes that would be the number of questions per topic 
    ## for user nodes that would be the number of questions per user
    dictz=nodesizing(topicz, userz)
    ## Iterate through graph to assign the size of each node as an attribute
    ## It is necessary to assign a "questions" attribute because it will be used 
    ## to calculate node size by the function plot_multimode().  
    for key in dictz.keys():
        g.node[key]['questions']=dictz[key]
    ## Return graph, dictionary of sizes, list of users and list of topics    
    return g, dictz, topicz, userz                 
