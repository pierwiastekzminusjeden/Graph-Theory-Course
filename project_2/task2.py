
from src.draw import draw_graph
from src.GraphicSeries import changeRandomEdge
from src.GraphicSeries import graphicStringFromList


#zadanie 2
# Randomizuje grafy proste o zadanych stopniach wierzchołków. Operuje na 
# grafie stworzonym w poprzednim zadaniu.
 
print('task 2 ')
print(' Program randomizuje zadana liczbe krawedzi grafu prostego utworzonego po wprowadzeniu ciagu graficznego ')
while True: 
    G1 = graphicStringFromList()
    draw_graph(G1, 'zestaw2/task2_before_rand.png')

    G2 = changeRandomEdge(G1, 1)
    try:
        draw_graph(G2, 'zestaw2/task2_after_rand.png')
    except:    
        print("brak wizualizacji grafu") 

