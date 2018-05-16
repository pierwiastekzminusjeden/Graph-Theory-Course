#!/usr/bin/env python3

from src.DFS import searchComp
from src.GraphClass import Graph
from src.draw import draw_graph
from src.Hamilton import searchHamiltonPath
from src.GraphicSeries import graphicStringFromList
from src.GraphicSeries import changeRandomEdge
from src.RegularGraph import random_K_RegularGraph
from src.Euler import GenerateEuler

#zadanie 1
# Sprawdza czy sekwencja liczb naturalnych jest ciągiem graficznym. Konstruuje graf
# prosty o stopniach wierzchołków zadanych przez wprowadzony ciag.
# #4332211 

print('\n\n\n Zadanie 1')
G1 = graphicStringFromList()
try:
    draw_graph(G1, 'zestaw2/przed_zamiana.png')
except ZeroDivisionError:
    print("Brak wizualizacji grafu") 

#zadanie 2
# Randomizuje grafy proste o zadanych stopniach wierzchołków. Operuje na 
# grafie stworzonym w poprzednim zadaniu.
 
print('\n\n\n Zadanie 2')
G2 = changeRandomEdge(G1, 1)
try:
    draw_graph(G2, 'zestaw2/po_zamianie.png')
except:    
    print("brak wizualizacji grafu") 


#zadanie 3
# Znajduje największą wspólną składową w grafie
# Wypisanie listy kolejno odwiedzonych wierzcholkow
print('\n\n\n Zadanie 3')
G3 = Graph()
G3.importFromFile("zestaw2/adj.txt")
print(searchComp(G3))
draw_graph(G3, 'zestaw2/najwieksza_składowa.png')

#zad 4
# Generuje graf Eulerowski i znajduje sciezke eulera
# Argumentami jest zakres, z jakiego ma byc wylosowana liczba wierzcholkow


G4 = GenerateEuler(5, 6)
try:
    draw_graph(G4, 'zestaw2/graf_Eulerowski.png')
except:    
    print("brak wizualizacji grafu") 


#zadanie 5
# Generuje graf losowy k-regularny

print('\n\n\n Zadanie 5')
randG = random_K_RegularGraph()
draw_graph(randG, 'zestaw2/rand_k_reg.png')

#zadanie 6
# Sprawdza czy graf hamiltonowski. Wypisuje informacje czy hamiltonowski oraz ścieżkę lub cykl. 
# Szuka od zadanego wierzcholka, wyisuje kolejno odwiedzone

print('\n\n\n Zadanie 6')
print(searchHamiltonPath(G3, 0))





