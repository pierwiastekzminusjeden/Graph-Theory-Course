import matplotlib.pyplot as plt
import numpy as np
from src.GraphClass import Graph


def draw_graph(adjMatrix: Graph, file: str):
    '''@brief draws graph
@param adjMatrix Graph object to draw
@param file file name'''
    fig, ax = plt.subplots(figsize=(20, 10))

    #centre of big cirlce
    centreX = 15
    centreY = 15

    tops = adjMatrix.dimensions[0]
    bigCircleRadius = 10

    #small circle
    smallCircleRadius = (2*3.14*bigCircleRadius)/(tops*2.5)
    if smallCircleRadius > 1:
        smallCircleRadius = 1

    #big circle
    bigCircle = plt.Circle((centreX, centreY), bigCircleRadius, color='w')
    bigCircle.set_edgecolor('b')
    ax.add_artist(bigCircle)

    #colors
    smallCircleFill = (1, 153/255, 51/255)
    smallCircleEdge = (1, 51/255, 0)
    coordinates = {}

    for i in range(tops):
        calculateX = bigCircleRadius*(np.cos(i*np.deg2rad(360/tops))) + centreX 
        calculateY = bigCircleRadius*(np.sin(i*np.deg2rad(360/tops))) + centreY 
        coordinates[i] = (calculateX,calculateY)
        x = plt.Circle((calculateX,calculateY), smallCircleRadius, facecolor=smallCircleFill, edgecolor = smallCircleEdge, linewidth=3)
        ax.add_artist(x)                                                       
        plt.text(calculateX, calculateY, i , fontsize=20)                    


    for i in range(len(adjMatrix.matrix)):
        for j in range(i):
            if adjMatrix.matrix[i][j] != 0:
                # print(coordinates[i][0], coordinates[i][1], coordinates[j][0], coordinates[j][1])
                plt.plot([coordinates[i][0], coordinates[j][0]], [coordinates[i][1], coordinates[j][1]], marker='o')
                if adjMatrix.matrixWeight.shape != (0,0):
                    plt.text((coordinates[i][0]+coordinates[j][0])/2, (coordinates[i][1] + coordinates[j][1])/2, adjMatrix.matrixWeight[i][j] , fontsize=20, color = 'lime')                    #wstawianie cyferki do kola

   
    for j in range(len(adjMatrix.matrix)):
            for i in range(j):
                if adjMatrix.matrix[i][j] != 0:
                    # print(coordinates[i][0], coordinates[i][1], coordinates[j][0], coordinates[j][1])
                    plt.plot([coordinates[i][0], coordinates[j][0]], [coordinates[i][1], coordinates[j][1]],'-x', dashes=[15,11], lw = 2.8)
                    if adjMatrix.matrixWeight.shape != (0,0):
                        plt.text((coordinates[i][0]+coordinates[j][0] + 1 )/2 , (coordinates[i][1] + coordinates[j][1])/2, adjMatrix.matrixWeight[i][j] , fontsize=20, color = 'red')                    #wstawianie cyferki do kola


    #axis
    plt.ylim([0, 30])
    plt.xlim([0, 30])
    #legend
    # plt.rcParams['legend.fontsize'] = 18
    # plt.plot( 'o' ,label = '0 -> 1' )
    # plt.plot('-x', lw = 5, label = '1 -> 0')
    # plt.legend(loc='lower right')

    #save to file
    fig.savefig(file)



if __name__ == '__main__':
    pass