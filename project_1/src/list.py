#@author Marcin Miś

import numpy as np

#@brief Klasa odpowiadająca za zczytywanie grafu z pliku z listą sąsiedztwa.
#       Zapis następuje w macierzy będącej reprezentacją listy
class List:
    tops = 0
    matrix = np.zeros((0,0), int)
#@brief konstruktor
#
#@param self nazwa obiektu
#@param tops liczba wierzchołków
    def __init__(self, tops = 0):
        self.tops = tops
        self.matrix = np.zeros((tops,tops),int)

#@brief Tworzy macierz będącą reprezentacją listy ze zczytywanej listy z pliku
#
#@param self nazwa obiektu
#@param file nazwa pliku
#@see   lista w postaci macierzy
    def createListFromFile(self, file: str):
        dimension = self.tops = numberOfLines = self.countFileLines(self,file)
        self.matrix = np.zeros((dimension,dimension),int)
        with open(file) as f:
            for line in f:
                flag = 0
                index = 0
                j = 0
                for ch in line:
                    if flag == 0:
                        flag = 1
                        index = int(ch) - 1
                        continue
                    if ch == ':' or ch == '\n' or ch == ' ':
                         continue
                    self.matrix[index][j] = int(ch)
                    j = j + 1
        print(self.matrix)

#@brief Licznik linii w pliku
    def countFileLines(self,file: str):
        with open(file) as f:
            for i, l in enumerate(f):
                pass
            return i + 1