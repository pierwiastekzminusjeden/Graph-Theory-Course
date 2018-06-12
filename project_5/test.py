from src.GraphClass import Graph
from src.draw import draw_graph

#task 1
print("task 1")
G = Graph(4)
# draw_graph(G, "Zestaw5/task1Graph.png")
print(G.matrixWeight)

#task 2
print("\ntask 2 - generated graph")
print(G.FordFulkerson(0, 5))


