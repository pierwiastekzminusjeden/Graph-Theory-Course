#!/usr/bin/env python3

from src.GraphClass import Graph
from src.draw import draw_graph


#Representation - Adjacency matrix

#task 1
print('==== task 1 ======')
G = Graph()
G.GNP(5,0.4)
print(G.matrix)
draw_graph(G, "zestaw4/randomGraph.png")

# task 2
print('\n==== task 2 ======')
print("Kosaraju tops list")
print(G.kosaraju())

# task 3
print('\n==== task 3 ======')
G2 = Graph()
print("Strongly cohesive graph")
G2.cohesiveGraph(5,0.1)
print(G2.matrix)
print(G2.randomWeightMatrix())
draw_graph(G2, "zestaw4/randomCohesiveGraph.png")
print("Bellman ford algorithm")
G2.bellman_ford(G2,0, True)

# task 4
print('\n==== task 4 ======\n')
print("Johnson alghoritm")
print(G2.johnson(3))
