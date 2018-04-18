#!/usr/bin/env python3

#############################
#@author Karolina Mizera
#@author Krystian Molenda
#@author Marcin Miś
#############################

#import sys
#sys.path.append('$(src)')   #add path to project_11/src or being all files in the same catalog is required
import generateRandomGraph
from adjmatrix import AdjMatrix
from adjMatrixFile import SaveToFile
from draw import draw_graph




print('''Graph generation: 
GNL - Generate with number of lines
GNP - Generate with probability
other - exit''')
key = input(" ")
while (key == 'GNL') or (key == 'GNP'):
    if key == 'GNL':
        numberOfTops = int(input("enter number of tops "))
        numberOfLines = int(input("enter number of lines "))
        gnlAdjMatrix = generateRandomGraph.GNL(numberOfTops, numberOfLines); 
        print(gnlAdjMatrix)            
        SaveToFile(gnlAdjMatrix, "GNL.txt")
        gnl = AdjMatrix
        gnl.createAdjMatrixFromFile(gnl, "GNL.txt")
        draw_graph(gnl,"GNL.png")
        print(" ")

    if key == 'GNP':
        numberOfTops = int(input("enter number of tops "))
        probability = float(input("enter probability "))
        gnpAdjMatrix = generateRandomGraph.GNP(numberOfTops, probability); 
        print(gnpAdjMatrix)              
        SaveToFile(gnpAdjMatrix, "GNP.txt")
        gnp = AdjMatrix
        gnp.createAdjMatrixFromFile(gnp, "GNP.txt")
        draw_graph(gnp,"GNP.png")
        print(" ")