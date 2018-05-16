
from src.RegularGraph import random_K_RegularGraph
from src.draw import draw_graph
from src.GraphClass import Graph


#zadanie 5
# Generuje graf losowy k-regularny

print('task 5')
randG = random_K_RegularGraph()
draw_graph(randG, 'zestaw2/task5_rand_k_reg.png')
