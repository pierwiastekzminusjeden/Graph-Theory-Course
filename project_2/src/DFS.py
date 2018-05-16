#!/usr/bin/env python3

from src.GraphClass import Graph
import numpy as np


#Zadanie 3

##################################################################################

#@brief implementajca algorytmu przeszukiwania w głąb
#@param g Reprezentacja macierzy sasiedztwa grafu
#@param v wierzchołek grafu od którego przeszukujemy
#@param visited lista wierzchołków już odwiedzonych
def DFS(g, v, visited):
    visited.append(v)

    for i in g.neighbors(v):
        if i not in visited:
            DFS(g,i,visited)

#########################################################################################

#@brief Funkcja znajdujaca najwieksza składową grafu za pomocą algorytmu przeszukiwania w głą. Korzysta z funkcji DFS
#@param g Reprezentacja macierzy sasiedztwa grafu
#@ret   Zwraca liste odwiedzonych kolejno wierzchołków w wyniku przeszukiwania w głąb najwiekszej składowej grafu
def searchComp(g):
    g.repairAdj()
    visited = []  #tablica odwiedzin
    
    #Start, przeszukuje wstepnie od zerowego wierzcholka. Jeżeli graf spójny zwraca liste wierzcholkow
    DFS(g,0,visited)
    length = len(visited)
    if(len(visited) == g.dimensions[0]):
        return visited


    #Jeśli graf nie jest spojny szuka najwiekszej skladowej grafu
    else:
        tmpVisited = []
        for i in range(1, g.dimensions[0]):
            DFS(g, i, tmpVisited)
            if len(tmpVisited) > length:
                length = len(tmpVisited)
                visited = tmpVisited[:]
            tmpVisited.clear()
        
        return visited

    
