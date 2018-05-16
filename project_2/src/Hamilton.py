#!/usr/bin/env python3

from src.DFS import DFS
from src.GraphClass import Graph
import numpy as np

#Zadanie 6: 

#########################################################################################
#@brief implementajca algorytmu wyszukiwania sciezki Hamiltona
#@param g Reprezentacja macierzy sasiedztwa grafu
#@param v wierzchołek grafu od którego przeszukujemy
#@param visited lista wierzchołków już odwiedzonych
def Hamilton(g, v, visited):
    visited.append(v)
    flag = False       #Flaga wyjścia. Jeśli True znaleziono. Pozwala na wyjście z rekurencji
    
    if len(visited) == g.dimensions[0]:
        if g.matrix[v][visited[0]] == 1:     #Sprawdza czy istnieje cykl
            visited.append(visited[0]) 
        return True
    
    for i in g.neighbors(v):
        if i not in visited:
            flag = Hamilton(g,i,visited)
    if flag == True:
        return True
    visited.pop(len(visited)-1)
    
###############################################################################################

#@brief Funkcja znajdujaca najwieksza sciezke lub cykl (jesli istnieje) Hamiltona
#@param g Reprezentacja macierzy sasiedztwa grafu
#@return   Zwraca liste odwiedzonych kolejno wierzchołków w wyniku przeszukiwania w głąb najwiekszej składowej grafu
def searchHamiltonPath(g, start):
    g.repairAdj()
    visited = []  #tablica odwiedzin
    
    #Start, Sprawdza czy graf jest spójny. 
    DFS(g,start,visited)
    if(len(visited) != g.dimensions[0]):
        return 'Graf nie jest Hamiltonowski'
    visited.clear()
    
    flag = Hamilton(g,start,visited)
    if flag == True:
        print('Graf Hamiltonowski')
        print('Cykl Hammiltona')
        return visited
    else:
        print('Graf półhamiltonowski')
        print('Sciezka Hammiltona')
        return visited
