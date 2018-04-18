#@author Karolina Mizera
#@author Marcin Miś


import numpy as np
from list import List
from adjmatrix import AdjMatrix
from incidencematrix import IncidenceMatrix



#@brief Konwerter z listy na macierz sąsiedztwa. 
#
#@param list obiekt klasy list z danymi
def fromListToAdjMatrix(_list: List):
    adjMatrix = AdjMatrix(_list.tops)
    for i in range(0, _list.tops):
        for j in range(0, _list.tops):
            if _list.matrix[i][j] != 0:
                adjMatrix.matrix[i][_list.matrix[i][j]-1] = 1
            #else:
                #adjMatrix.matrix[i][_list.matrix[i][j]-1] = 0 
    return adjMatrix




def fromAdjMatrixtoIncidenceMatrix(adjMatrix: AdjMatrix):
    numberOfCollumns = CountIncidanceInAdjMatrix(adjMatrix)
    print(numberOfCollumns)
    incidenceMatrix = IncidenceMatrix(adjMatrix.tops, numberOfCollumns) 
    pivot = 0   #iteracja w macierzy incydencji po kolumnach
    for i in range(0 , adjMatrix.tops):
       
        for j in range(0 , i):
            
            if adjMatrix.matrix[i][j] == 1:
                
                incidenceMatrix.matrix[j][pivot] = 1
                incidenceMatrix.matrix[i][pivot] = 1
                pivot = pivot + 1
    return incidenceMatrix


def fromIncidenceMatrixtoList(incidenceMatrix: IncidenceMatrix):
    lista = List(incidenceMatrix.tops)
    temp=0
    for j in range( incidenceMatrix.edges):
        temp = 0
        for i in range( incidenceMatrix.tops ):
            if incidenceMatrix.matrix[i][j] == 1:
                if not temp == 0:
                    temp=temp-1
                    for index in range(lista.tops):
                        if not lista.matrix[i][index]:
                            lista.matrix[i][index]=temp+1
                            break

                    for index in range(lista.tops):
                        if not lista.matrix[temp][index]:
                            lista.matrix[temp][index]=i+1
                            break
                else:
                    temp = i+1
                    continue# i, bo iterujemy od zera, więc wierzchołek sądziada ma wartość o jeden większą niż pozycja w macierzy'''
    return lista


def CountIncidanceInAdjMatrix(adjMatrix: AdjMatrix):
#przy zamianie adjmatrix -> incidence
#zlicza i zwraca ile incydencji jest w macierzy
    counter=0
    for i in range(adjMatrix.tops):
        for j in range(i):
            if adjMatrix.matrix[i][j]==1:
                counter = counter + 1
    #print(counter)
    return counter