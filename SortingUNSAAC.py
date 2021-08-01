import math 
#Librerias de Python:

#1.- Ordenacion Insert Sort(listo)
def InsertSort(A,n):
  #el arreglo de numeros
  for j in range(1,n):#
    key=A[j]
    i=j-1
    while i>=0 and A[i]>=key:#le aumentamos  ""="" para numeros repetidos
      A[i+1]=A[i]
      i=i-1
    A[i+1]=key

#2.- Ordenacion Merge Sort(listo)
def MergeSort(arr, l, r):
    
    if l < r:
        # Encontrar Indice medio del Arreglo
        m = (l + r) // 2

        # Ordenar la parte Izquierda usando merge sort
        MergeSort(arr, l, m)

        # Ordenar la parte Derecha usando merge sort
        MergeSort(arr, m + 1, r)

        # merge the two half (mezclar o unir las dos divisiones)
        merge(arr, l, m, r)
        
def merge(arr, l, m, r):
    # Hallar la longitud del arreglo izquierdo
    nL = m - l + 1

    # Hallar la longitud del arreglo Derecho
    nR = r - m

    # Crear dos arreglos vacios
    L = [0] * (nL + 1)
    R = [0] * (nR + 1)

    # copiar los elementos del arreglo izquierdo en L
    for i in range(0, nL):
        L[i] = arr[l + i]

    # copiar los elementos del arreglo Derecho en R
    for j in range(0, nR):
        R[j] = arr[m + 1 + j]

    # poner valores infinitos(grandes) a los valores finales de los arreglos L y R
    L[nL] = math.inf
    R[nR] = math.inf

    #Iterarar sobre L y R
    #Copiar  los elementos menores de L y R en el arreglo
    i = 0
    j = 0
    for k in range(l, r + 1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1

  
#3.- Ordenacion Shell Sort(listo)
def ShellSort(lista,n):
    sublista = n//2 #Divide a la mitad
    while sublista > 0: #Mientras haya elementos en la division
        for inicio in range(sublista):#Recorrer desde la posicion 0 hasta la posicion n//2
            shell(lista, inicio, sublista)
        sublista = sublista//2


def shell(lista, inicio, gap):
    for i in range(inicio + gap, len(lista), gap):
        x = lista[i]
        pos = i
        while pos >= gap and lista[pos - gap] > x:
            lista[pos] = lista[pos - gap]
            pos -= gap
        lista[pos] =x


#4.- Ordenacion Radix Sort(listo)
def RadixSort(listToSort,n):
  RADIX = 10
  isMaxLength = False
  temporary = -1
  local = 1

  while not isMaxLength:
    isMaxLength = True

    buckets = [list() for _ in range(RADIX)]

    for  element in listToSort:
      temporary = element / local
      buckets[math.floor(temporary % RADIX)].append(element)
      if isMaxLength and temporary > 0:
        isMaxLength = False

    index = 0

    for bucketIndex in range(RADIX):
      newBuckets = buckets[bucketIndex]
      for element in newBuckets:
        listToSort[index] = element
        index += 1

    local *= RADIX


        
#5.- Ordenacion Bubble Sort(listo)
def BubbleSort(lista,n):
    for i in range(n):
        for j in range(i + 1,n):
            if (lista[i] > lista[j]):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux


#6.- Ordenacion Heap Sort(listo) Estructurar el arreglo en forma de arbol binario(cada nodo padre tiene que ser mayor a ambos hijos)
def HeapSort(arr,n):
  
  for i in range(n//2, -1, -1):
      heapify(arr, n, i)
  
  for i in range(n-1, 0, -1):
      # cambiar de posicion
      arr[i], arr[0] = arr[0], arr[i]
  
      # elemento raiz Heapify
      heapify(arr, i, 0)


def heapify(arr, n, i):
  #encontrar el mayor entre la raiz y los hijos
  largest = i
  l = 2 * i + 1
  r = 2 * i + 2
  
  if l < n and arr[i] < arr[l]:
      largest = l
  
  if r < n and arr[largest] < arr[r]:
      largest = r
  
  #Si la raíz no es mayor, cambiar por el mayor y seguir iterando
  if largest != i:
      arr[i], arr[largest] = arr[largest], arr[i]
      heapify(arr, n, largest)
  

                
#7.- Ordenacion Quick Sort(listo)
#       
def partition(array, low, high):

  # Escoger el elementos que esta mas a la derecha como pivote
  pivot = array[high]

  # puntero para el elemento mayor
  i = low - 1

  #Recorrer todos los elementos
  # Compara todos los elementos con el pivote
  for j in range(low, high):
    if array[j] <= pivot:
      #si se encuentra un elemento más pequeño que el pivote
      #intercambiarlo con el elemento mayor señalado por i
      i = i + 1

      #intercambiando elemento en i con elemento en j
      (array[i], array[j]) = (array[j], array[i])

  # intercambiar el elemento pivote con el elemento mayor especificado por i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # devolver la posición desde donde se realiza la partición
  return i + 1

# Funcion para realizar QuickSort
def QuickSort(array, low, high):
  if low < high:
    pi = partition(array, low, high)
    QuickSort(array, low, pi - 1)
    QuickSort(array, pi + 1, high)

    
#8.- Ordenacion Bucket Sort(listo)(Como minimo el arreglo debe de tener 11 elementos)

def BucketSort(array,n):
    bucket = []

    # Crear cuberos o casillas vacias
    for i in range(len(array)):
        bucket.append([])

    # Innsertar los elementos en sus respectivas casillas
    for j in array:#Recorrer todos los elementos del arreglo
        index_b = int(10 * j) #Insertar en su respeciva casilla
        bucket[index_b].append(j)

    # Ordenar los elementos que estan dentro de una casilla
    for i in range(len(array)):
        InsertSort(bucket[i],len(bucket[i]))#bucket[i] = sorted(bucket[i])

    # Almacenar todos los cambios en el array general
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1

            
#9.- Ordenacion Selection Sort(listo)

def SelectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # Seleccionamos al elemento menor en cada iteracion
            if array[i] < array[min_idx]:
                min_idx = i
         
        # Ponemos el elemento menor en la posicion correcta
        (array[step], array[min_idx]) = (array[min_idx], array[step])
            
#10.- Ordenacion Comb Sort

def CombSort(inputArr):
    outputArr=inputArr
    gap = len(outputArr)
    swaps = True
    while gap > 1 or swaps:
        gap = max(1, int(gap / 1.3))  # pivot minimo es 1
        swaps = False
        for i in range(len(outputArr) - gap):
            j = i+gap
            if outputArr[i] > outputArr[j]:
                outputArr[i], outputArr[j] = outputArr[j], outputArr[i]
                swaps = True


