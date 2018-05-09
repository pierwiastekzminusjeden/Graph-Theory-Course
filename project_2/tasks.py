#!/usr/bin/env python3
###################################################################################
#@authors Krystian Molenda, Marcin Miś, Karolina Mizera
#
#
#
#
###################################################################################


from src.GraphClass import Graph
from src.draw import draw_graph
import numpy as np 
from src.generateGraph import randGraph



#task_1
#task_1 w module src.generateGraph.
G =  randGraph()
print('----------------------')
print('Graf spójny losowy')
G.randomWeightMatrix()
draw_graph(G,'zestaw3/graf_spójny.png')
print(G.matrix)

#task_2 
G.dijkstra(0)
print('----------------------')

#task_3 
print('Macierz odległości')
G.distanceMatrix()
print(G.distMatrix)
print('----------------------')

#task_4
print('Centrum grafu')
print(G.searchGraphCenter())
print('----------------------')
print('Centrum minmax')
print(G.searchMinimaxCenter())

#task_5
print('----------------------')
draw_graph(G.mst_prim(),'zestaw3/graf_prim.png')
print('Minimalne drzewo rozpinające')
print(G.mst_matrix)
