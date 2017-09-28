#!usr/bin/python
# encoding: utf-8

"""


Created by Omar Padierna on 2015-12-17.
Copyright (c) 2015 __Venturez.com__. All rights reserved.

This library defines a function that calculates the edge size for the multimode network
in this case, edge size refers to the thickness that the line connecting users and topics
will have. This thickness is defined by the number of questions that the user made about any given topic
as such, if the user has 5 questions about housing but only 1 about jobs then the line 
connecting to housing will be thicker than the one connecting to jobs

Note: This code is in beta and it is highly inefficient it only works for small database
        in other words, this code is not scalable
"""

import csv 




def getweight(usery='Omar', topicly='Jobs'):
    ## Read the data from a CSV file
    ## We use the Universal new-line mode since many CSV files are created with Excel
    r=csv.reader(open('campaign_short.csv','rU'))
        
        
        ## we need to keep track separately of nodes of all types 
    topicz=[]
    userz=[]
        
        ## Iterate through the CSV and relate user with topic.
        ## Topic's column is column 3 (the fourth) and user's column is the 
        
    for row in r: 
            
        if row[0] not in userz:
            userz.append(row[0])
        if row[3] not in topicz:
            if row[3] is not '':
                topicz.append(row[3])
    tuplez={}
    weightz=[]
    i=0
    j=0
    count=0
   
   ## Iterate through both lists to calculate weights for specific 
   ## topic and user
        
    for i in range(0,len(topicz)):
        for j in range(0,len(userz)):
                
            r=csv.reader(open('campaign_short.csv','rU'))  
            for row in r:
                if row[3] == topicz[i] and row[0]==userz[j]:
                    count=count+1           
            weightz.append((userz[j],count))
            j=j+1
        tuplez[topicz[i]]=weightz
        weightz=[]                   
        count= 0
        i=i+1
    ##Create a list that unpacks the weights
    mpacker=[]   
    ##Iterate through dictionary and obtain value
    if topicly in tuplez.keys():
        mpacker=tuplez[topicly]
    ##Obtain individual value for specific user     
        val = dict(mpacker)[usery]
        return val
        
           
        