import math
import sys
import random
from collections import deque
import numpy as np


class Graph:

    def __init__(self, layers=0):
        #task1
        self.layers = layers
        self.tops_in_layer = self.randomize_layers()
        self.dimensions = (sum(self.tops_in_layer), sum(self.tops_in_layer))
        self.matrix = np.zeros(self.dimensions, )
        self.matrixWeight = np.zeros(self.dimensions, int)  
        #print(self.get_tops_in_layers_matrix())
        self.randomize_layers_connections()
        self.add_2n_random_edges()
        self.add_weights()
        #task2
        self.matrix = self.matrixWeight

    def importFromMatrix(self, matrix):
        self.matrix = matrix
        self.matrixWeight = matrix
        self.dimensions = matrix.shape

    def importFromFile(self, file: str):
        self.matrix = np.loadtxt(file)
        self.dimensions = self.matrix.shape

    def importToFile(self, file: str):
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

    def randomize_layers(self):
        number_of_layers = self.layers
        N = number_of_layers - 2 
        tab = []
        for i in range(number_of_layers):
            tab.append(random.randint(2, N))   
        tab[0] = 1 
        tab[number_of_layers - 1] = 1 
        print(tab)
        return tab

    def get_tops_in_layers_matrix(self):
        indexes_of_tops = np.full((self.layers, self.layers), -1, dtype=int) 
        current_top = 0
        for i in range(self.layers):
            for j in range(self.tops_in_layer[i]): 
                indexes_of_tops[i][j] = current_top
                current_top += 1
        return indexes_of_tops 

    def randomize_layers_connections(self):
        for l in range(self.layers - 1):
            if self.tops_in_layer[l + 1] > self.tops_in_layer[l]: 
                for i in self.get_tops_in_layers_matrix()[l + 1]: 
                    if i == -1: 
                        break
                    top_from_connect = self.get_tops_in_layers_matrix()[l][0] + i % (self.tops_in_layer[l])
                    self.matrix[top_from_connect][i] = 1 
            else:                                        
                for i in self.get_tops_in_layers_matrix()[l]:  
                    if i == -1:
                        break
                    top_to_connect = self.get_tops_in_layers_matrix()[l + 1][0] + i % (self.tops_in_layer[l + 1])
                    self.matrix[i][top_to_connect] = 1 
        print(self.matrix)

    def add_2n_random_edges(self):
        N = self.layers - 2
        n = N * 2
        while n != 0:
            x = random.randint(0, self.dimensions[0] - 1)
            y = random.randint(0, self.dimensions[0] - 1)
            if self.matrix[x][y] != 1 and y != 0 and x != self.dimensions[0] - 1 and x!= y:   
                self.matrix[x][y] = 1                                              
                n = n - 1                                                        

    def add_weights(self):
        for i in range(self.dimensions[0]):
            for j in range(self.dimensions[0]):
                if self.matrix[i][j] == 1:
                    self.matrixWeight[i][j] = random.randint(1, 10)


#task2

    def BFS(self,s, t, path):

        visited =[False for _ in range(self.dimensions[0])]
        visited[s] = True

        Q = deque([])
        Q.append(s)
         
        while Q:
 
            u = Q.popleft()
         
            for v in self.neighbors(u):
                if visited[v] == False:
                    visited[v] = v
                    path[v] = u
                    Q.append(v)

        return True if visited[t] else False
             
     
    def FordFulkerson(self, s = 0, t = 0):
        if s == 0 and t == 0:
            exit()

        path = [-1 for _ in range(self.dimensions[0])]
        maxFlow = 0 
        while self.BFS(s, t, path) :
            pathFlow = math.inf
            tmp = t
            while(tmp !=  s):

                pathFlow = min (pathFlow, self.matrix[path[tmp]][tmp])
                tmp = path[tmp]
            maxFlow +=  pathFlow
            v = t
            while(v !=  s):
                self.matrix[path[v]][v] -= pathFlow
                self.matrix[v][path[v]] += pathFlow
                v = path[v]
 
        return (abs(maxFlow), path)