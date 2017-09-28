#!usr/bin/python
# encoding: utf-8
'''
Created by Omar Padierna 01-12-16
Copyright (c) 2016 __Venturez.com__. All rights reserved.
'''
##Import all required libraries
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import Tkinter as Tk
from Tkinter import *
from tkMessageBox import showinfo
import networkx as nx
import matplotlib.pyplot as plt
import multimode as mm
##Libraries below were made specifically for this project
##Source files must be in the same working directory
import affiliatelib as afil
import usersnet as uzenet
import topicsnet as topicsnet
import triadic


###########################################################################
'''
This section of the code declares the main screen to be used 
and the different containers that will have all the interactive
elements in the GUI.

'''

root = Tk()

root.wm_title("Animated Graph embedded in TK")
root.wm_protocol('WM_DELETE_WINDOW', root.quit())
w = Canvas(master=root, width=200, height=100)
Y= Canvas(master=w, width=100, height=50)
f = plt.figure(figsize=(5,4))
a = f.add_subplot(111)

###########################################################################
'''
This section of the code begins exctracting the network data. 
To make the code more readable, all the network data code has been 
retrieved as a library. Triad analysis, Affiliation Netwokrs and Density
are in the following libraries: 

import affiliatelib as afil
import usersnet as uzenet
import topicsnet as topicsnet
'''
## Obtain Affiliation network: this function returns a tuple 
##containing a graph object and a dictionary that has all the questions
## per user and topic respectively

dble =afil.affiliation()


# Clear the canvas for plotting
a.cla()
#Unpack the tuple, g is the graph object and dictz is the dictionary
g=dble[0]
dictz=dble[1]
# Define the layout for the graph see networkx.draw documentation for more
pos=nx.spring_layout(g)
#Call plot function from library to plot Affiliate network
nx.write_graphml(g, "test.graphml")
mm.plot_multimode(g, type_string='questions', sizing=dictz)
census, node_census = triadic.triadic_census(g)

# Define drawing area for plot in GUI
canvas = FigureCanvasTkAgg(f,master=w)
canvas.show()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
###########################################################################

'''
This section of the code defines the actions that will be
performed by the buttons of the GUI. These actions have 
the functionality in the code but in this section they are not 
binded (related to) the buttons in the GUI
'''

def multimode_graph():
    '''
    This function calls the plot_multimode function to display a multimode graph
    for more information on multimode graphs see the comments in the source code 
    of that library. 
    '''    
    ## Clear plot area. This is needed every time a new plot comes
    ## Otherwise plots will be drawn on top of another
    a.cla()
    ## Unpack tuple from existing network    
    g=dble[0]
    dictz=dble[1]
    ## Define layout
    pos=nx.spring_layout(g)
    ## Plot graph
    mm.plot_multimode(g, type_string='questions', sizing=dictz)
    dense=nx.density(g)
    text.delete(1.0,END)
    text.insert(INSERT, "Density is: ")  
    text.insert(INSERT,dense) 
    ## Send plot to canvas   
    canvas.draw()
        
def users_projected_graph():
    '''
    This function plots the projected graph of the multimode network
    This projected graph onnects the users among each other if both asked a question
    about the same topic
    '''
    ## Clear plot area. This is needed every time a new plot comes
    ## Otherwise plots will be drawn on top of another
    a.cla()
    ## Unpack tuple from existing network    
    g=dble[0]
    dictz=dble[1]
    ##Define layout
    pos=nx.spectral_layout(g)
    ## Plot graph     
    uzenet.plotusenet(dble)
    users=uzenet.getnet(dble)
    dense=nx.density(users)
    text.delete(1.0,END)
    text.insert(INSERT, "Density is: ")  
    text.insert(INSERT,dense) 
    canvas.draw()
        
def topics_projected_graph():
    '''
    Same as above but in this case it shows the network of topics and connects any two topics if 
    a user has asked a question about both
    '''
    a.cla()
    dble =afil.affiliation()
    g=dble[0]
    dictz=dble[1]
    pos=nx.spectral_layout(g)
    topicsnet.plottopicnet(dble)
    topics=topicsnet.getnet(dble)
    dense=nx.density(topics)
    text.delete(1.0,END)
    text.insert(INSERT, "Density is: ")  
    text.insert(INSERT,dense) 
    canvas.draw()
##Kill window        
def finish():
    root.quit() 
###########################################################################
'''
This section contains all the buttons and widgets necessary for interaction. 
Widgets are declared, binded (associated to a specific function) and packed here. 
'''           
#Declare and bind widgets     
text = Text(Y, height=3, width=25)      
b = Button(Y, text="MultiMode",command=multimode_graph)
c = Button(Y, text="Users network",command=users_projected_graph)
d = Button(Y, text="Topics Network",command=topics_projected_graph)
e = Button(Y, text="Close",command=finish)
#Pack widgets to the containers declared at the beginning
b.pack(side=LEFT)
c.pack(side=LEFT)
d.pack(side=LEFT)
e.pack(side=LEFT)
text.pack(side=RIGHT)
w.pack()
Y.pack()
root.mainloop()