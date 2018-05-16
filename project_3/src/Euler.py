import sys
from copy import deepcopy
from numpy import *
from random import randint
from src.GraphClass import Graph
from src.DFS import DFS
from src.GraphicSeries import changeRandomEdge
from src.GraphicSeries import graphicStringFromList




def Euler(numOfTops):
    if numOfTops <5:
        print("nie można zbudować grafu o tej liczbie wierzcholkow")
        sys.exit(0)
    L = []
    visited = []
    iterate = 0
    G = Graph()
    while G.dimensions[0] == 0 or not any(G.matrix)or len(visited) != G.dimensions[0]:
        L.clear()
        visited.clear()
        while iterate != numOfTops:
            i = randint(1, 4)
            if not i%2:
                L.append(i)
                iterate +=1
        G = graphicStringFromList(L)
        DFS(G,0, visited)
        iterate = 0

    # visited.clear()
    # toFind = ecycle(G)
    # toFind.searchEulerPath()
    return G


# class ecycle:
#     S = []
#     D = []
#     n = m = cv  = 0

#     def __init__(self, G):
#         self.G = deepcopy(G)

#     def DFSb(self, v, vf):
#         ecycle.D[v] = ecycle.cv
#         low = ecycle.cv
#         ecycle.cv +=1
#         for i in range(self.G.dimensions[0]):
#             if self.G.matrix[v][i] and i != vf:
#                 if i not in ecycle.D:
#                     tmp = self.DFSb(i,v)
#                     if tmp < low:
#                         low = tmp
#                 elif ecycle.D[i] < low:
#                     low = tmp
#         if vf > -1 and ecycle.D[v] == low:
#             self.G.matrix[vf][v] = self.G.matrix[v][vf] = 2
#         return low

#     def find(self, v):
#         u = w = 0
#         while True:
#             ecycle.S.append(v)       
#             for u in range(ecycle.n) and self.G.matrix[v][u]:
#                 pass
#             if u == ecycle.n :
#                 break
#             for i in range(ecycle.n):
#                 ecycle.D[i] = 0
#             ecycle.cv = 1
#             self.DFSb(v,-1)
            
#             w = u+1
#             while self.G.matrix[v][u] == 2 and w < ecycle.n:
#                 if self.G.matrix[v][w]:
#                     u = w
#                 w +=1
#             self.G.matrix[v][u] = self.G.self.matrix[u][v] = 0
#             v = u

#     def searchEulerPath(self):
#         VD = [0 for _ in range(self.G.dimensions[0])]
#         v1 = v2 = 0
            
#         for v1 in range(ecycle.n):
#             if VD[v1]:
#                 break
#         i = v1
#         while i < ecycle.n:
#             if VD[i] % 2:
#                 v1 = i
#                 break

#         self.find(v1)
#         print(ecycle.S)







