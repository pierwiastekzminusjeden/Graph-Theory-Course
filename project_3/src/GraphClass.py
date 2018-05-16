import numpy as np
from sys import maxsize
from math import inf



#klasa reprezentująca macierz sasiedztwa
class Graph:


#Konstruktor, zapisuje wymiary w postaci krotki, A - sasiedztwo, L- lista
    def __init__(self, dimensions = (0,0) ):
        self.dimensions = dimensions
        self.matrix = np.zeros(dimensions, int)
        
       
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
        for i in range(self.dimensions[0]):
            for j in range(self.dimensions[0]):
                self.matrix[i][j] = self.matrix[j][i]
                
#Zwraca liste sąsiadów danego wierzchołka v
    def neighbors(self, v):
        neigh = []
        for i in range(self.dimensions[0]):
            if self.matrix[v][i] != 0:
                neigh.append(i)
        return neigh

    def deg(self, v):
        deg = 0
        for i in range(self.dimensions[0]):
            for j in range(i):
                if self.matrix[i][j] != 0:
                    deg +=1
        return deg