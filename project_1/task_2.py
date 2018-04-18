#!/usr/bin/env python3

#############################
#@author Karolina Mizera
#@author Krystian Molenda
#@author Marcin Miś
#############################

#import sys
#sys.path.append('$(src)')   #add path to project_11/src or being all files in the same catalog is required
from adjmatrix import AdjMatrix
from draw import draw_graph


print('''Print matrix on the picture''')

fileName = input("Enter adjmatrix file name: ") #enter name of data file. File must be in the same catalog. Examples in catalog /data

matrix = AdjMatrix
matrix.createAdjMatrixFromFile(matrix,fileName)


draw_graph(matrix, 'graph.png')
