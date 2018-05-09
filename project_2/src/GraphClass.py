import numpy as np
from sys import maxsize
from math import inf
#klasa reprezentująca macierz sasiedztwa/incydencji. 
class Graph:


#Konstruktor, zapisuje wymiary w postaci krotki, Flagi I - incydencja, A - sasiedztwo, L- lista
    def __init__(self, flag = 'A', dimensions = (0,0) ):
        self.flag = flag
        self.dimensions = dimensions
        self.matrix = np.zeros(dimensions, int)
        self.distMatrix = np.zeros((0,0), int)
        self.mst_matrix = np.zeros((0,0), int)
        self.graphCenter = None
        self.minmaxGraphCenter = None

#importuje z macierzy biblioteki numpy
    def importFromMatrix(self, matrix):
        self.matrix = matrix
        self.dimensions = matrix.shape


#Import z pliku. do self.matrix. Wymiary macierzy do self.dimensions w postaci krotki
    def importFromFile(self, file: str):
        self.matrix = np.loadtxt(file)
        self.dimensions = self.matrix.shape


#Metoda statyczna do zapisu do pliku. 
#Przykładowe wywołanie matrix.importToFile(matrix.matrix, "nazwa")
    @staticmethod
    def importToFile(matrix, file: str):    
        np.savetxt(file, matrix, fmt = '%1d')

#Przywraca macierz ADJ, Tworzy macierz symetryczna. Należy nieco poprawić idee, ale pomaga. Jeśli macierz bedzie poprawnie wprowadzona
#nic nie zrobi. 
# TYLKO DLA NIESKIEROWANEGO, używać ostrożnie 
    def repairAdj(self):
        if self.flag != 'A':
            return
        for i in range(self.dimensions[0]):
            for j in range(self.dimensions[0]):
                self.matrix[i][j] = self.matrix[j][i]
                
#Zwraca liste sąsiadów danego wierzchołka v
    def neighbors(self, v):
        if self.flag != 'A':
            return None
        neigh = []
        for i in range(self.dimensions[0]):
            if self.matrix[v][i] != 0:
                neigh.append(i)
        return neigh


##################################################################################################################
#Modyfikacje do Zestawu 3:
##################################################################################################################

#Zadanie 1

#Ustawia macierz wag krawedzi dla grafu nieskierowanego. W przypadku skierowanego należy usunać ifa
#NADPISUJE MACIERZ SASIEDZTWA WAGAMI
#TYLKO DLA NIESKIEROWANEGO
    def randomWeightMatrix(self):
        for i in range(self.dimensions[0]):
            for j in range(i):
                if self.matrix[i][j] == 1:
                    self.matrix[i][j] =  np.random.randint(1,11)
        self.repairAdj()


##################################################################################################################

#Zadanie 2

#implementacja algorytmu dijkstry jako r metody klasy Graph. 
#Zwraca tablice odległości do wszystkich wierzchołków od wierzchołka zadanego. 
    def dijkstra(self, w):

        Q = [i for i in range(self.dimensions[0])]
        if w not in Q:
            return

        d = [maxsize if i != w else 0 for i in range(self.dimensions[0])] #koszt dojscia
        p = [-1 for i in range(self.dimensions[0])] #lista poprzednikow, w celu łatwiejszego rozwiniecia zadania
        
        while Q:
            u = Q[0]
            for i in Q:
                if d[i] < d[u]:
                    u = i
            Q.remove(u)
            for v in self.neighbors(u):
                if d[v] > d[u] + self.matrix[u][v]:
                    d[v] = d[u] + self.matrix[u][v]
                    p[v] = u

        return d

##################################################################################################################

#Zadanie 3

#Tworzy macierz odległości za pomocą wielokrotnego wywołania algorytmu Dijkstry
#tworzy macierz odległości distMatrix
    def distanceMatrix(self):
        self.distMatrix = np.zeros(self.dimensions, int)
        for i in range(self.dimensions[0]):
            self.distMatrix[i]  = self.dijkstra(i)


##################################################################################################################

#Zadanie 4

#znajduje centrum grafu. Zwraca numer wierzcholka bedacego centrum        
    def searchGraphCenter(self):
        tmp = sum(self.distMatrix[0])
        self.graphCenter = 0
        for v in range(self.dimensions[0]):
            if sum(self.distMatrix[v]) < tmp:
                tmp = sum(self.distMatrix[v])
                self.graphCenter = v

        return self.graphCenter


#znajduje centrum minimax grafu. Zwraca numer wierzcholka bedacego centrum minimax
    def searchMinimaxCenter(self):
        tmp = max(self.distMatrix[0])
        self.minmaxGraphCenter = 0
        for v in range(self.dimensions[0]):
            if max(self.distMatrix[v]) < tmp:
                tmp = max(self.distMatrix[v])
                self.minmaxGraphCenter = v
        return self.minmaxGraphCenter


##################################################################################################################

#Zadanie 5

#zwraca minimalne rozpinajace drzewo jako nowy graf. Tworzy nową macierz będącą reprezentacją
#minimalnego drzewa rozpinającego @mst_matrix
    def mst_prim(self):
        self.mst_matrix = np.zeros(self.dimensions, int)
        parent_list = [None] * self.dimensions[0]
        queue = {node: inf for node in range(self.dimensions[0])}
        queue[0] = 0

        while queue:
            u = min(queue, key=queue.get)
            del queue[u]
            for v in self.neighbors(u):
                if v in queue and self.distMatrix[u][v] < queue[v]:
                    parent_list[v] = u
                    queue[v] = self.distMatrix[u][v]

        for i in range(1, self.dimensions[0]):
            self.mst_matrix[i][parent_list[i]] = 1
            self.mst_matrix[parent_list[i]][i] = 1

        mst = Graph()
        mst.importFromMatrix(self.mst_matrix)
        return mst

##################################################################################

# inne algorytmy

##################################################################################

#@brief implementajca algorytmu przeszukiwania w głąb
#@param g Reprezentacja macierzy sasiedztwa grafu
#@param v wierzchołek grafu od którego przeszukujemy
#@param visited lista wierzchołków już odwiedzonych
    @staticmethod
    def DFS(g, v, visited):
        visited.append(v)

        for i in g.neighbors(v):
            if i not in visited:
                g.DFS(g,i,visited)
