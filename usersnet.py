import networkx as net
import affiliatelib as afil
from networkx.algorithms import bipartite as bi
from Edgesize import getweight
from TopicSize import nodesizing

def plotusenet(a=type(list)):
    g=a[0]
    userz=a[3]
    topiccnet=bi.weighted_projected_graph(g, userz, ratio=False)
    weights=[edata['weight'] for f,t,edata in topiccnet.edges(data=True)]
    net.draw_networkx(topiccnet, width=weights, edge_color=weights)

def getnet(a=type(list)):
    g=a[0]
    userz=a[3]
    topiccnet=bi.weighted_projected_graph(g, userz, ratio=False)
    return topiccnet
