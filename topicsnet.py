import networkx as net
from networkx.algorithms import bipartite as bi
from Edgesize import getweight
from TopicSize import nodesizing

def plottopicnet(a=type(list)):
    g=a[0]
    topicz=a[2]
    topiccnet=bi.weighted_projected_graph(g, topicz, ratio=False)
    weights=[edata['weight'] for f,t,edata in topiccnet.edges(data=True)]
    net.draw_networkx(topiccnet, width=weights, edge_color=weights)
    
def getnet(a=type(list)):
    g=a[0]
    topicz=a[2]
    topiccnet=bi.weighted_projected_graph(g, topicz, ratio=False)
    return topiccnet
