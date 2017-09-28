# SNA


The code in this repo was written in 2014. 

The code for this analysis is based on the book "Social Network Analysis for Startups" by Maksim Tsvetovat. 

To generate the network data, a special library was developed. The source code can be found at "affiliatelib.py". The library opens a CSV file with the app data and maps two columns (user and topic) taking into account the number of questions the user has made for each topic. 

At the moment that this library was created, there was no database or data schema to use. As such, the number of questions per topic is a number that had to be calculated in Python. For that, a library called Edgesize was developed to calculate the weight of each edge and a library called TopicSize was developed to calculate node size. The source code can be found at "Edgesize.py" and "TopicSize.py" respectively. 

A particular characterstic of Affiliate networks is that they can be transformed into projected networks. In this case, the affiliate network has two types of nodes: users and topics. The projected networks therefore would be a network of users connected by the topics they have in common and a network of topics connected by the users they have in common. 

A specific library was developed for each type of node using the "networkx.weighted_projected_graph()" method from the networkx library. The source code for each library can be found at "topicsnet.py" and "usersnet.py"

Since the goal is to generate and visualize network data automatically (i.e. from the app to the computer without using 3rd party software) an graphic user interface was also developed in order to make the analysis slightly more interactive. 

The source code for the GUI can be found at "GUI.py". The GUI shows the affiliate network and its projected networks. 
