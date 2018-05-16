#!/usr/bin/env python3
from random import randint
import src.GraphicSeries
import src.GraphClass


def random_K_RegularGraph():
    while True:
        k=randint(2,10) #losuje od 2 do 9
        print(k)
        while True:
            n=0
            n=randint(k+1, 11)
            if k%2 and n%2:
                n+=1
            if k+2==n and not k%2:
                n-=1

            if src.GraphicSeries.Interface([k for i in range(n)]):    #if ciąg jes to ciągiem graficznym
                graph= src.GraphicSeries.createGraph([k for i in range(n)]) #tworze macierz sąsiedztwa 
                if graph==False:
                    continue
                print(graph.matrix, '\n')
                break 
            else:
                continue  
        break
    return graph
    
