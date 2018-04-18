#@author Marcin Miś
import numpy as np


#@brief Klasa odpowiadająca za zczytywanie grafu z pliku z macierzą sąsiedztwa.
class AdjMatrix:
    tops = 0
    matrix = np.zeros((0, 0), int)
#@brief konstruktor
#
#@param self nazwa obiektu
#@param tops liczba wierzchołków
    def __init__(self, tops=0):
        self.tops = tops
        self.matrix = np.zeros((tops, tops), int)

#@brief Tworzy macierz sąsiedztwa ze zczytywanej macierzy
#
#@param self nazwa obiektu
#@param file nazwa pliku
#@see   macierz sasiedztwa
    def createAdjMatrixFromFile(self, file: str):
        dimension = numberOfLines = self.countFileLines(self, file)
        self.tops = dimension
        self.matrix = np.zeros((dimension,dimension),int)
        self.matrix = np.loadtxt(file)
        print(self.matrix)


#@brief Licznik linii w pliku
    def countFileLines(self,file: str):
        with open(file) as f:
            for i, l in enumerate(f):
                pass
            return i + 1