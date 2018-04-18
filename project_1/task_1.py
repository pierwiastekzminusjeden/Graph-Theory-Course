#!/usr/bin/env python3

#############################
#@author Karolina Mizera
#@author Krystian Molenda
#@author Marcin Miś
#############################


#import sys
#sys.path.append('$(src)')   #add path to project_11/src or being all files in the same catalog is required
from list import List
from adjmatrix import AdjMatrix
from incidencematrix import IncidenceMatrix
from adjMatrixFile import SaveToFile
import convert
from draw import draw_graph




#Enter first matrix
print('''Import matrix from file.
A - Adjacency Matrix
I - Incidence Matrix
L - Adjacency List
other - exit''')
#@key representation flag

key = input(" ")
fileName = input("Enter file name: ")   #enter name of data file. File must be in the same catalog. Examples in catalog /data


if (key not in 'AIL') or (fileName != ''):
    if key == 'A':
        adjMatrix = AdjMatrix              
        adjMatrix.createAdjMatrixFromFile(adjMatrix,fileName)
    elif key == 'I':
        incMatrix = IncidenceMatrix
        incMatrix.createIncMatrixFromFile(incMatrix,fileName)
    elif key == 'L':
        _list = List
        _list.createListFromFile(_list, fileName)
    print(" ")

#conversions
    while key in 'AIL' :
        if key == 'A':
            draw_graph(adjMatrix, 'zad1Graph.png')

            print('''Convert representation:
        AI - Adjacency Matrix to Incidence Matrix
        AL - Adjency Matrix to Adjency List
        x - exit''')
            
            key = input(" ")
            if key == 'AI':
                incMatrix = convert.fromAdjMatrixtoIncidenceMatrix(adjMatrix)
                print(incMatrix.matrix)
                key = 'I'
            elif key == 'AL':
                incMatrix = convert.fromAdjMatrixtoIncidenceMatrix(adjMatrix)
                _list = incMatrix = convert.fromIncidenceMatrixtoList(incMatrix)
                print(_list.matrix)
                key = 'L'

        elif key == 'I':
            print('''Convert representation:
        IL - Incidence Matrix to Adjency List
        IA - Incidence Matrix to Adjency Matrix
        x - exit ''')

            
            key = input(" ")
            if key == 'IL':
                _list =  convert.fromIncidenceMatrixtoList(incMatrix)
                print(_list.matrix)
                key = 'L'
            elif key == 'IA':
                _list =  convert.fromIncidenceMatrixtoList(incMatrix)
                adjMatrix = convert.fromListToAdjMatrix(_list)
                print(adjMatrix.matrix)
                key = 'A'

        elif  key == 'L':

            print('''Convert representation: 
        LA - Adjacency List to Adjency Matrix
        LI - Adjency List to Incidence Matrix
        x - exit''')
            key = input(" ")
            if key == 'LA':
                adjMatrix = convert.fromListToAdjMatrix(_list)
                print(adjMatrix.matrix)
                key = 'A'
            elif key == 'LI':
                adjMatrix = convert.fromListToAdjMatrix(_list)
                incMatrix = convert.fromAdjMatrixtoIncidenceMatrix(adjMatrix)
                print(incMatrix.matrix)
                key = 'I'
