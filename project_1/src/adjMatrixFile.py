#@author Krystian Molenda

import numpy as np


def SaveToFile(matrix, file: str):    
    np.savetxt(file, matrix, fmt = '%1d')

def ImportFromFile(file: str):
    matrix = np.loadtxt(file)
    return matrix