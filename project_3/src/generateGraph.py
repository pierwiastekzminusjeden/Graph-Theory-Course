# !/usr/bin/env python3
# . Napisać program do generowania grafów losowych G(n, l) oraz G(n, p).


#w celu wydajnej obsługi macierzy oraz wygodniejszego wypisywania import numpy
from numpy import *
import random
from src.GraphClass import Graph

# @brief Generuje graf losowy
# @param numberOfTops    liczba wierzchołków
# @param numberOfLines   liczba krawędzi
# @return                macierz sąsiedztwa wygenerowanego grafu

def GNL(numberOfTops, numberOfLines):
    matrix = zeros((numberOfTops,numberOfTops),int)
    i = 0
    
    if numberOfLines > numberOfTops*(numberOfTops-1)/2:
        print("Too many edges")
        return zeros((numberOfTops,numberOfTops), int_)

    while i < numberOfLines:
        x = random.randint(0, numberOfTops-1)
        y = random.randint(0, numberOfTops-1)

        if x != y and matrix[x][y] != 1:
            matrix[x][y] = 1
            matrix[y][x] = 1
            i += 1
    return matrix

# @brief Generuje graf losowy. Sprawdza czy dla zadanego prawdopodobienstwa może być połączenie między
#   wierzchołkami
# @param numberOfTops    liczba wierzchołków
# @param probability     prawdopodobienstwo
# @return                macierz sąsiedztwa wygenerowanego grafu

def GNP(numberOfTops, probability):
    matrix = zeros((numberOfTops, numberOfTops), int_)
    for i in range(numberOfTops):
        for j in range(i):
            if random.random() < probability:
                matrix[i][j] = 1
                matrix[j][i] = 1
    return matrix


##################################################################################################################
#Modyfikacje do Zestawu 3:
##################################################################################################################

#Zadanie 1

#@brief Wylosowanie grafu spójnego. Losowany jest graf z metody GNL z 1 zestawu. Następnie poprzezd DFS
#       sprawdzana jest spójność.
#@comment Metoda zaakceptowana jako poprawna przez Wach
def randGraph():
    G = Graph()
    visited = [1]
    while len(visited) != G.dimensions[0]:
        visited.clear()
        numberOfTops = random.randint(3,7)    
        numberOfLines = random.randint(1,numberOfTops*(numberOfTops-1)/2)
        G.importFromMatrix(GNL(numberOfTops,numberOfLines))
        G.DFS(G,0,visited)
    return G