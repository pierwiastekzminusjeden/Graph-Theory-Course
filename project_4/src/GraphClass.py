import math
import sys

import numpy as np



class Graph:
    '''Directed graph represented by adjacency matrix'''

    def __init__(self, dimensions=(0, 0)):
        self.dimensions = dimensions
        self.matrix = np.zeros(dimensions, int)
        self.matrixWeight = np.zeros(dimensions, int)  # macierz wag [-5,10] gdzie zero tez waga
        # self.distMatrix = np.zeros((0,0), int)

    
    def importFromMatrix(self, matrix):
        '''Import reference from numpy matrix to object'''
        self.matrix = matrix
        self.dimensions = matrix.shape

    
    def importFromFile(self, file: str):
        '''Import from file to object'''
        self.matrix = np.loadtxt(file)
        self.dimensions = self.matrix.shape

    
    def importToFile(self, file: str):
        '''Import matrix to file'''
        np.savetxt(file, self.matrix, fmt='%1d')

    
    def neighbors(self, v):
        '''Returns neighbors of v top'''
        if v > self.dimensions[0]:
            return
        neigh = []
        for i in range(self.dimensions[0]):
            if self.matrix[v][i] != 0:
                neigh.append(i)
        return neigh

    # Project 4
    # task 1
    def GNP(self, numberOfTops, probability):
        ''' Modificated directed GNP generator'''
        self.matrix = np.zeros((numberOfTops, numberOfTops), int)
        self.dimensions = self.matrix.shape
        for i in range(numberOfTops):
            for j in range(numberOfTops):
                if np.random.random() < probability and i != j:
                    self.matrix[i][j] = 1

    # task 2
    def DFS(self, v, visited, stack, newOne, flag=False):
        '''Modificated DFS algorithm to Kosaraju implementation. Includes DFS_visit and Components_R'''
        visited.append(v)
        if not flag:
            newOne.append(v)
        for i in self.neighbors(v):
            if i not in visited and flag:
                self.DFS(i, visited, stack, newOne, True)
            elif i not in visited:
                self.DFS(i, visited, stack, newOne)
        if flag:
            stack.append(v)


    def transpose(self):
        '''Graph transposition '''
        for i in range(self.dimensions[0]):
            for j in range(i):
                tmp = self.matrix[i][j]
                self.matrix[i][j] = self.matrix[j][i]
                self.matrix[j][i] = tmp

    #task 2
    def kosaraju(self):
        '''Implementation of Kosaraju algorithm. Finds and returns the biggest strongly 
cohesive subgraph tops list. Uses DFS and transposition methods'''
        visited = []
        stack = []

        for v in range(self.dimensions[0]):
            if v not in visited:
                self.DFS(v, visited, stack, None, True)

        self.transpose()

        visited.clear()
        iterate = 0  
        biggestOne = [] 

        while stack:
            newOne = []
            v = stack.pop()
            if v in visited:
                break
            iterate += 1
            self.DFS(v, visited, stack, newOne)
            if len(newOne) > len(biggestOne):
                biggestOne = newOne[:]
        # print(biggestOne)
        return biggestOne

    # task 3
    def randomWeightMatrix(self):
        '''method sets random weights from the range [-5,10] in graph object'''
        self.matrixWeight = np.zeros(self.dimensions, float)
        for i in range(self.dimensions[0]):
            for j in range(self.dimensions[0]):
                if self.matrix[i][j] == 0:
                    self.matrixWeight[i][j] = math.inf
                #  if i == j:
                #     self.matrixWeight[i][j] = -100
                elif self.matrix[i][j] == 1:
                    self.matrixWeight[i][j] = np.random.randint(-5, 11)
        return self.matrixWeight

    def cohesiveGraph(self, size, probability):
        '''Makes strongly cohesive graph with given size and probability. 
Uses GNP and Kosaraju methods'''
        self.matrix = np.zeros((size, size), int)
        self.dimensions = self.matrix.shape

        self.GNP(size, probability)
        cohesiveGraph = self.kosaraju()

        while len(cohesiveGraph) != self.dimensions[0]:
            self.GNP(size, probability)
            cohesiveGraph = self.kosaraju()
        return cohesiveGraph



    # task 3
    def init_graph(self, selected, path_list, parent_list):
        for i in range(len(path_list)):
            path_list[i] = math.inf
            parent_list[i] = -1
        path_list[selected] = 0

    def bellman_ford(self, graph, selected, flag = False):
        '''Bellman Ford algorithm. Finds shorted paths. Returns path list. 
Prints path and parent lists.'''
        if 0 > selected > graph.dimensions[0]:
            return "wrong top"

        n = graph.dimensions[0]
        path_list = [None for _ in range(n)]
        parent_list = [-1 for _ in range(n)]
        self.init_graph(selected, path_list, parent_list)

        for k in range(n - 1):
            for i in range(n):
                for j in range(n):
                    if graph.matrix[i][j] != 0 and path_list[j] > path_list[i] + graph.matrixWeight[i][j]:
                        path_list[j] = path_list[i] + graph.matrixWeight[i][j]
                        parent_list[j] = i

        for i in range(n):
            for j in range(n):
                if graph.matrix[i][j] != 0 and path_list[j] > path_list[i] + graph.matrixWeight[i][j]:
                    print("UJEMNY CYKL")
                    return False
        if flag:
            print("PARENT__\n", parent_list)
            print("PATH___\n", path_list)
        return path_list

    def add_s(self):
        n = (self.dimensions[0] + 1, self.dimensions[0] + 1)
        g_prim = Graph(n)
        g_prim.matrixWeight = np.zeros(n, float)
        for i in range(n[0] - 1):
            for j in range(n[0] - 1):
                g_prim.matrix[i][j] = self.matrix[i][j]
                g_prim.matrixWeight[i][j] = self.matrixWeight[i][j]
        for i in range(n[0]):
            g_prim.matrix[n[0] - 1][i] = 1
            g_prim.matrixWeight[n[0] - 1][i] = 0
            g_prim.matrixWeight[i][n[0] - 1] = math.inf
        g_prim.matrix[n[0] - 1][n[0] - 1] = 0
        return g_prim


    def dijkstra(self, G, w, matrixWeight):
        '''Dijkstra algorithm.'''
        Q = [i for i in range(G.dimensions[0])]
        if w not in Q:
            return

        d = [sys.maxsize if i != w else 0 for i in range(G.dimensions[0])]  # koszt dojscia
        p = [-1 for i in range(G.dimensions[0])]  

        while Q:
            u = Q[0]
            for i in Q:
                if d[i] < d[u]:
                    u = i
            Q.remove(u)
            for v in self.neighbors(u):
                if d[v] > d[u] + G.matrixWeight[u][v]:
                    d[v] = d[u] + G.matrixWeight[u][v]
                    p[v] = u
        return d

    def johnson(self, selected):
        '''Johnson algorithm. Returns shortest paths matrix. Uses bellman_ford and add_s method'''
        g_prim = self.add_s()

        h = [None for _ in range(g_prim.dimensions[0])]
        w_prim = g_prim.matrixWeight
        bell_ford = self.bellman_ford(g_prim, g_prim.dimensions[0] - 1)
        if not bell_ford:
            print("ERROR")
            return 1
        else:
            for v in range(g_prim.matrix.shape[0]):
                h[v] = bell_ford[v]
            for u in range(g_prim.matrix.shape[0]):
                for v in range(g_prim.matrix.shape[0]):
                    if g_prim.matrixWeight[u][v] == math.inf or h[u] == math.inf or h[v] == math.inf:
                        w_prim[u][v] = math.inf
                    else:
                        w_prim[u][v] = g_prim.matrixWeight[u][v] + h[u] - h[v]
            D = np.zeros(self.dimensions)
            for u in range(self.matrix.shape[0]):
                duv = self.dijkstra(self, u, w_prim)
                for v in range(self.matrix.shape[0]):
                    D[u][v] = duv[v]
            # print(D)
            # np.transpose(D)
            return D



if __name__ == '__main__':
    pass