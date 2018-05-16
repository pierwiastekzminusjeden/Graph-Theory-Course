#!/usr/bin/env python3
from src.Euler import Euler
from src.draw import draw_graph
from src.GraphClass import Graph


#zad 4
# Generuje graf Eulerowski i znajduje sciezke eulera
# Argumentami jest zakres, z jakiego ma byc wylosowana liczba wierzcholkow

print('task 4')
G4 = Euler(5)
try:
    draw_graph(G4, 'zestaw2/task4_graf_Eulerowski.png')
except:    
    print("brak wizualizacji grafu")
