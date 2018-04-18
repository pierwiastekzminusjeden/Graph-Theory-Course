#@author Marcin Miś

import numpy as np

#@brief Klasa odpowiadająca za zczytywanie grafu z pliku z macierzą incydencji.
class IncidenceMatrix:
    tops = 0
    edges = 0
    matrix = np.zeros((0, 0), int)

#@brief konstruktor
#
#@param tops liczba wierzcholkow
#@param edges liczba krawedzi
    def __init__(self, tops=0, edges=0):
        self.tops = tops
        self.edges = edges
        self.matrix = np.zeros((tops, edges), int)

#@brief Zczytuje macierz incydencji z pliku do macierzy incydencji
#
#@param self nazwa obiektu
#@param file nazwa pliku
#@see   macierz incydencji
    def createIncMatrixFromFile(self, file: str):
        self.tops = self.countFileLines(self, file)
        self.edges = self.countLineCharacters(self, file)
        self.matrix = np.zeros((self.tops, self.edges), int)
        self.matrix = np.loadtxt(file)
        print(self.matrix)


#@brief Licznik linii w pliku
    def countFileLines(self,file: str):
        with open(file) as f:
            for i, l in enumerate(f):
                pass
            return i + 1

#@brief Licznik znaków w liniii
    def countLineCharacters(self,file: str):
        counter = 0
        with open(file) as f:
            for line in f:
                for ch in line:
                    if ch.isdigit():
                        counter +=1
                return counter