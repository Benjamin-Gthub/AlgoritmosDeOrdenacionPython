import random


#Generador de arreglos para insert Sort:
def GenArreglosInsertSort(n):
    MejorCaso=[]
    PeorCaso=[]
    CasoPromedio=[]
    #Mejor caso
    for x in range(n):
        MejorCaso.append(x)
        PeorCaso.append(n-x)
        CasoPromedio.append(random.randrange(n))
    return MejorCaso,CasoPromedio,PeorCaso

#Generador de arreglos para merge sort:
def GenArreglosMergeSort(n):
    MejorCaso=[]
    PeorCaso=[]
    CasoPromedio=[]
    for x in range(n):
        MejorCaso.append(n-x)
        PeorCaso.append(x)
        CasoPromedio.append(random.randrange(n))
    return MejorCaso,CasoPromedio,PeorCaso

#Generador de arreglos para Shell sort:
def GenArreglosShellSort(n):
    MejorCaso=[]
    PeorCaso=[]
    CasoPromedio=[]
    for x in range(n):
        MejorCaso.append(x)
        PeorCaso.append(random.randrange(n))
        CasoPromedio.append(n-x)
    return MejorCaso,CasoPromedio,PeorCaso

#Generador de arreglos para Radix sort:---------------
def GenArreglosRadixSort(n):
    MejorCaso=[]
    PeorCaso=[]
    CasoPromedio=[]
    for x in range(n):
        MejorCaso.append(x)
        PeorCaso.append(n-x)
        CasoPromedio.append(random.randrange(n))
    return MejorCaso,CasoPromedio,PeorCaso
    

#Generador de arreglos para Bubble sort:
def GenArreglosBubbleSort(n):
    MejorCaso=[]
    PeorCaso=[]
    CasoPromedio=[]
    for x in range(n):
        MejorCaso.append(x)
        PeorCaso.append(n-x)
        CasoPromedio.append(random.randrange(n))
    return MejorCaso,CasoPromedio,PeorCaso

#Generador de arreglos para Heap sort:
def GenArreglosHeapSort(n):
    MejorCaso=[]
    PeorCaso=[]
    CasoPromedio=[]
    for x in range(n):
        MejorCaso.append(n-x)
        PeorCaso.append(x)
        CasoPromedio.append(random.randrange(n))
    return MejorCaso,CasoPromedio,PeorCaso

#Generador de arreglos para Quick sort:
def GenArreglosQuickSort(n):
    MejorCaso=[]
    PeorCaso=[]
    CasoPromedio=[]
    for x in range(n):
        MejorCaso.append(random.randrange(n))
        PeorCaso.append(x)
        CasoPromedio.append(n-x)
    return MejorCaso,CasoPromedio,PeorCaso

#Generador de arreglos para Bucket Sort:
def GenArreglosBucketSort(n):
    MejorCaso=[]
    PeorCaso=[]
    CasoPromedio=[]
    for x in range(n):
        MejorCaso.append(float(x/n))
        PeorCaso.append(float((n-x-1)/n))
        CasoPromedio.append(random.random())#Numeros aleatorios entre (0 y1>
    return MejorCaso,CasoPromedio,PeorCaso

#Generador de arreglos para Selection Sort:
def GenArreglosSelectionSort(n):
    MejorCaso=[]
    PeorCaso=[]
    CasoPromedio=[]
    for x in range(n):
        MejorCaso.append(x)
        PeorCaso.append(n-x)
        CasoPromedio.append(random.randrange(n))
    return MejorCaso,CasoPromedio,PeorCaso

#Generador de arreglos para Selection Sort:
def GenArreglosCombSort(n):
    MejorCaso=[]
    PeorCaso=[]
    CasoPromedio=[]
    for x in range(n):
        MejorCaso.append(x)
        PeorCaso.append(n-x)
        CasoPromedio.append(random.randrange(n))
    return MejorCaso,CasoPromedio,PeorCaso

