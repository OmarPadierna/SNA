#!usr/bin/python
# encoding: utf-8

"""
Created by Omar Padierna on 2015-12-17.
Copyright (c) 2015 __Venturez.com__. All rights reserved.
Modified from Maksim Tsvetovat on 2011-08-17.
"""

import sys
import os
import csv 
import math

## Import bi-partite (bi-modal) functions

from objc._objc import NULL


def nodesizing (topicz=[],userz=[] ):
  
    dictz={}
    countz=[]
    i=1
    count=0
    #Loop for calculating node size of Topics
    #Node size equals the amount of questions per topic
    #Iterate through CSV file to count questions
    
    for i in range(0,len(topicz)):
        r=csv.reader(open('campaign_short.csv','rU'))  
        for row in r:
            if row[3] == topicz[i]:
                count=count+1           
        dictz[topicz[i]]=count               
        count= 0
        i=i+1
        
    #Loop to calculate the size of Users
    ##Iterate through CSV file
    i=1
    count=0
    
    for i in range(0,len(userz)):
        r=csv.reader(open('campaign_short.csv','rU'))  
        for row in r:
            if row[0] == userz[i] and row[3] is not '':
                count=count+1           
        dictz[userz[i]]=count               
        count= 0
        i=i+1    
    ## Return dictionary of values using topics and users as keys    
    return dictz


    