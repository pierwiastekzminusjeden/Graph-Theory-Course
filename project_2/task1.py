#!/usr/bin/env python3
from src.draw import draw_graph
from src.GraphicSeries import graphicStringFromList


#zadanie 1
# Sprawdza czy sekwencja liczb naturalnych jest ciągiem graficznym. Konstruuje graf
# prosty o stopniach wierzchołków zadanych przez wprowadzony ciag.

print(' task 1 \n')

while True: 
    G1 = graphicStringFromList()
    try:
        draw_graph(G1, 'zestaw2/task1_graph.png')
    except ZeroDivisionError:
        print("Brak wizualizacji grafu") 
    