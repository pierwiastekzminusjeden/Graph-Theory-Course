import matplotlib.pyplot as plt
import numpy as np
from src.GraphClass import Graph

# @brief rysuje graf
# @param adjMatrix macierz sąsiedztwa
# @param file nazwa pliku
def draw_graph(adjMatrix: Graph, file: str):

    fig, ax = plt.subplots(figsize=(20, 10))

    #wspolrzedne srodka duzego kola
    centreX = 15
    centreY = 15

    tops = adjMatrix.dimensions[0]
    bigCircleRadius = 10

    #wzor na promien malych kol
    smallCircleRadius = (2*3.14*bigCircleRadius)/(tops*2.5)
    if smallCircleRadius > 1:
        smallCircleRadius = 1

    #rysowanie duzego kola
    bigCircle = plt.Circle((centreX, centreY), bigCircleRadius, color='w')
    bigCircle.set_edgecolor('b')
    ax.add_artist(bigCircle)

    #kolory malego kola w RGB
    smallCircleFill = ('orange')
    smallCircleEdge = ('red')
    coordinates = {}

    for i in range(tops):
        calculateX = bigCircleRadius*(np.cos(i*np.deg2rad(360/tops))) + centreX #wspolrzedna x i-tego malego kola
        calculateY = bigCircleRadius*(np.sin(i*np.deg2rad(360/tops))) + centreY #wspolrzedna y i-tego malego kola
        coordinates[i] = (calculateX,calculateY)
        x = plt.Circle((calculateX,calculateY), smallCircleRadius, facecolor=smallCircleFill, edgecolor = smallCircleEdge, linewidth=3)
        ax.add_artist(x)                                                       #rysowanie i-tego malego kola
        plt.text(calculateX, calculateY, i , fontsize=25)                    #wstawianie cyferki do kola


    #tutaj sprawdzam czy sasiaduja i jak tak to rysuje linie miedzy nimi
    for i in range(len(adjMatrix.matrix)):
        for j in range(len(adjMatrix.matrix[i])):
            if adjMatrix.matrix[i][j] != 0:
                #print(coordinates[i][0], coordinates[i][1], coordinates[j][0], coordinates[j][1])
                plt.plot([coordinates[i][0], coordinates[j][0]], [coordinates[i][1], coordinates[j][1]], marker='o')
                plt.text((coordinates[i][0]+coordinates[j][0])/2, (coordinates[i][1] + coordinates[j][1])/2, adjMatrix.matrix[i][j] , fontsize=20)                    #wstawianie cyferki do kola

    #potrzebne do ustalenia rozmiarow osi wspolrzednych
    plt.ylim([0, 30])
    plt.xlim([0, 30])

    #zapis do pliku
    fig.savefig(file)