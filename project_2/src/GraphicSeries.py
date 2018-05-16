#!/usr/bin/env python3
from sys import argv
from sys import exit
import random
from src.GraphClass import Graph




def graphicStringFromList(ciag = None):
#sprawdzanie ciągu graficznego i ewentuale tworzenie reprezentacji macierzowej tego grafu
    gList = []
    if ciag:
        gList = ciag[:]

    elif len(argv) == 1:
        print("Proszę podać ciąg:")
        gList = input(" ")
    else:
        gList = argv[1]
    try:
        bcgString=[int(i) for i in gList]
        gString =[int(i) for i in gList]
    except ValueError:
        print("Koniec programu")
        exit(0)

    if Interface(gString):
        
        graph=createGraph(bcgString)
        print("Otrzymano graf postaci:\n", graph.matrix)
        return graph
    else :
        return Graph((len(gList),len(gList)))
        
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////   
def Interface(gString):
# funkcja opisująca przebieg sprawdzania ciągu graficznego 

    #print("Podano", gString, '\n')

    if len([i for i in gString if i%2])%2: 
        print("""Ciąg nie jest ciągiem graficznym
Nieparzysta liczba wierzchołków o nieparzystych stopniach.""")
        return False

    if gString[0] > len(gString):
        print("Ciąg nie jest ciągiem graficznym, maksymalna liczba stopni jest większa od liczby wierzchołków.")
        return False

    if ifGraphicString(gString):

        return True
    else:
        print("Ciąg nie jest ciągiem graficznym.")
             
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def ifGraphicString(gList):
#implementacja algorytmu sprawdzającego ciąg 
    gList.sort()
    gList.reverse()
    if gList[0]<len(gList):
        for i in range(1,gList[0]+1):
            gList[i]=gList[i]-1    
    else:
        for i in range(1,len(gList)):
            gList[i]=gList[i]-1  
    gList.sort()
    gList.pop()
    gList.reverse() 

    if len(gList)==1 and not gList[0]:
        return True
    elif  len(gList)>1:
        return ifGraphicString(gList)
    else:
        return False

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def createGraph(gList):
    '''tworzenie macierzy sąsiedztwa na podstawie ciągu graficznego'''
    print( "Ciąg",gList ,"jest ciągiem graficznym.")
    graph = Graph((len(gList),len(gList)))
    stone = len(gList)
    copy=gList[:]
    gList.sort()
    gList.reverse()
    index=0
    loop=[0,0]
    while len(gList) > 0:
        control=0
        drawIndex=1 #zmienna sprawdzająca
        j=1 # checkingIndex -> index do faktycznego wypełniania macierzy
        key = gList[0]
        currentSize = len(gList)

        while drawIndex<=key and j<currentSize:
            #print(graph.matrix)
            if not gList[j]: # jeżeli pozycja w ciągu jest równa zero
                j+=1
                continue

            if key != drawIndex and currentSize -1 == j:
                gList[j]=gList[j]-1
                graph.matrix[index][j+index]+=1 
                graph.matrix[j+index][index]+=1#wypełnianie w przypadku pętli
                graph = changeIfPetla(1, graph, index, index+j)
                #print(graph.matrix[j+index][index])
                count = 0
                while graph.matrix[j+index][index]==1:
                    if count == 1000:
                        return False
                    count+=1
                    graph = changeIfPetla(2, graph, index, index+j)#randomizacja
    
                drawIndex+=1
            else:
                gList[j]=gList[j]-1
                graph.matrix[index][j+index]+=1 #zwykłe wpisywanie sąsiadów macierzy
                graph.matrix[j+index][index]+=1
                j+=1
                drawIndex+=1

        if len(gList) == 1:
            if graph.matrix[index][index-1]:
                break
            graph.matrix[index][index]=gList[0]#samotny wierzchołek

        gList.pop(0)
        index+=1    
    control=0
    index = len( graph.matrix[0])
    #while graph.matrix[index-1][index-2]>1:
     #   control+=1
      #  print(graph.matrix)
       # graph=changeIfPetla(1, graph, index-1, index-2) #część do randomizacji krawędzi wielokrotnych
        #print(graph.matrix)
        #if control>10: break   
    while graph.matrix[index-1][index-1]>1:
        #print(graph.matrix)
        graph = changeIfPetla(1, graph,index-1, index-1 )
        
    return graph   


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def changeIfPetla(flag, graph:Graph,  a,b):
    numberOfEdges=len(graph.matrix[0])
    controlv2=0

    
    while True: 
        if controlv2>50: 
            return graph

        #print(randC)
        if flag ==1: 
            randC=random.randrange(0, numberOfEdges-2) 
            if  randC == a or randC == b or  graph.matrix[a][randC] == 1 or  graph.matrix[b][randC] ==1 :
                controlv2+=1
                continue
        elif flag ==2:
            randC=random.randrange(0, a) 
            if  randC == a or randC == b: #or graph.matrix[a][randC] == 1 or  graph.matrix[b][randC] ==1 :
                controlv2+=1
                continue
        else:
            randC=random.randrange(0, numberOfEdges-2) 
            if  randC == a or randC == b: #or graph.matrix[a][randC] == 1 or  graph.matrix[b][randC] ==1 :
                controlv2+=1
                continue
            
        tabD=[i for i in range(1, numberOfEdges-2) if graph.matrix[randC][i]]
        if not len(tabD):
            controlv2+=1
            continue

        randD=tabD[random.randint(0,len(tabD)-1)]  
        if randD == a or randD ==b:
            controlv2+=1
            continue

        if randD  in [i for i in range(1, numberOfEdges) if graph.matrix[b][i]]:
            controlv2+=1
            continue
            
        if randD  in  [i for i in range(1, numberOfEdges) if graph.matrix[a][i]]:
            controlv2+=1
            continue
        break
    if flag == 3:
        graph.matrix[b][a]-=1
        graph.matrix[randC][randD]-=1
        graph.matrix[randD][randC]-=1
        graph.matrix[a][randD]+=1
        graph.matrix[randD][a]+=1
        graph.matrix[randC][b]+=1
        graph.matrix[b][randC]+=1
    else:
        swapEdges( graph, a,b,randC,randD)
    return  graph

def changeRandomEdge(G, n = 1):
    '''randomizacja krawędzi'''
    macierzSasiedztwa=G
    numberOfEdges=macierzSasiedztwa.dimensions[0]
    if numberOfEdges == 0:
        return None

    if numberOfEdges<4:
        return None
    for i in range(n):
        while True: 
            randA=random.randrange(0, numberOfEdges)
            tabB = [i for i in range(1, numberOfEdges) if macierzSasiedztwa.matrix[randA][i]==1]

            if not len(tabB):   
                continue

            randB=tabB[random.randint(0,len(tabB)-1)]

            randC=random.randrange(0, numberOfEdges)
            while  randA == randC or randC in tabB:
                randC=random.randrange(0, numberOfEdges)
            
            tabD=[i for i in range(1, numberOfEdges) if macierzSasiedztwa.matrix[randC][i]==1]

            if not len(tabD): continue
                
            randD=tabD[random.randint(0,len(tabD)-1)]  

            if randD in tabB or randD == randA: continue
                
            if randA in tabD or randB in tabD: continue
            break

        print(randA, randB)
        print(randC, randD)
        macierzSasiedztwa = swapEdges(macierzSasiedztwa, randA, randB, randC, randD)
        print(macierzSasiedztwa.matrix)
    return macierzSasiedztwa

def swapEdges( graph:Graph, a,b,c,d):
   
    graph.matrix[a][b]-=1
    graph.matrix[b][a]-=1
    graph.matrix[c][d]-=1
    graph.matrix[d][c]-=1
    graph.matrix[a][d]+=1
    graph.matrix[d][a]+=1
    graph.matrix[c][b]+=1
    graph.matrix[b][c]+=1

    return graph
