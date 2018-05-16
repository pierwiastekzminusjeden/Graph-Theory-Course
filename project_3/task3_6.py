#!/usr/bin/env python3
from src.DFS import searchComp
from src.Hamilton import searchHamiltonPath
from src.draw import draw_graph
from src.GraphClass import Graph

#zadanie 3
# Znajduje największą wspólną składową w grafie
# Wypisanie listy kolejno odwiedzonych wierzcholkow


print('task 3')
G3 = Graph()
G3.importFromFile("zestaw2/adj.txt")
print(searchComp(G3))
draw_graph(G3, 'zestaw2/task3_and_6.png')


#zadanie 6
# Sprawdza czy graf hamiltonowski. Wypisuje informacje czy hamiltonowski oraz ścieżkę lub cykl. 
# Szuka od zadanego wierzcholka, wyisuje kolejno odwiedzone

print('task 6')
print(searchHamiltonPath(G3, 0))