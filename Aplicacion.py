from tkinter import*
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from SortingUNSAAC import*
from GeneradorArreglos import*
from time import*

def VentanaInsertSort():
    #Regresamos a su forma anterior
    root.geometry("750x425+340+100")
    #Limpiamos todas las ventanas abiertas
    lienzoMergeSort.pack_forget()
    lienzoShellSort.pack_forget()
    lienzoRadixSort.pack_forget()
    lienzoBubbleSort.pack_forget()
    lienzoHeapSort.pack_forget()
    lienzoQuickSort.pack_forget()
    lienzoBucketSort.pack_forget()
    lienzoSelectionSort.pack_forget()
    lienzoCombSort.pack_forget()
    lienzoArregloDefinido.pack_forget()
    #Eliminamos la ventanas de resultados:
    VentanaSelectionOrdenado.destroy()
    VentanaMergeOrdenado.destroy()
    VentanaShellOrdenado.destroy()
    VentanaBubbleOrdenado.destroy()
    VentanaBucketOrdenado.destroy()
    VentanaCombOrdenado.destroy()
    VentanaQuickOrdenado.destroy()
    VentanaRadixOrdenado.destroy()
    VentanaHeapOrdenado.destroy()
    #Mostramos la ventana requerida
    lienzoInsertSort.pack()

def VentanaSalir():
    #Regresamos a su forma anterior
    root.geometry("750x425+340+100")
    #Limpiamos todas las ventanas abiertas
    lienzoInsertSort.pack_forget()
    lienzoMergeSort.pack_forget()
    lienzoShellSort.pack_forget()
    lienzoRadixSort.pack_forget()
    lienzoBubbleSort.pack_forget()
    lienzoHeapSort.pack_forget()
    lienzoQuickSort.pack_forget()
    lienzoBucketSort.pack_forget()
    lienzoSelectionSort.pack_forget()
    lienzoCombSort.pack_forget()
    lienzoArregloDefinido.pack_forget()
    #Eliminamos la ventanas de resultados:
    VentanaSelectionOrdenado.destroy()
    VentanaMergeOrdenado.destroy()
    VentanaShellOrdenado.destroy()
    VentanaBubbleOrdenado.destroy()
    VentanaBucketOrdenado.destroy()
    VentanaCombOrdenado.destroy()
    VentanaQuickOrdenado.destroy()
    VentanaRadixOrdenado.destroy()
    VentanaHeapOrdenado.destroy()
    VentanaInsertOrdenado.destroy()
    
def VentanaMergeSort():
    #Regresamos a su forma anterior
    root.geometry("750x425+340+100")
    #Limpiamos todas las ventanas abiertas
    lienzoInsertSort.pack_forget()
    lienzoShellSort.pack_forget()
    lienzoRadixSort.pack_forget()
    lienzoBubbleSort.pack_forget()
    lienzoHeapSort.pack_forget()
    lienzoQuickSort.pack_forget()
    lienzoBucketSort.pack_forget()
    lienzoSelectionSort.pack_forget()
    lienzoCombSort.pack_forget()
    lienzoArregloDefinido.pack_forget()
    #Eliminamos la ventanas de resultados:
    VentanaInsertOrdenado.destroy()
    VentanaSelectionOrdenado.destroy()
    VentanaShellOrdenado.destroy()
    VentanaBubbleOrdenado.destroy()
    VentanaBucketOrdenado.destroy()
    VentanaCombOrdenado.destroy()
    VentanaQuickOrdenado.destroy()
    VentanaRadixOrdenado.destroy()
    VentanaHeapOrdenado.destroy()
    #Mostramos lo que queremos
    lienzoMergeSort.pack()
def VentanaShellSort():
    #Regresamos a su forma anterior
    root.geometry("750x425+340+100")
    #Limpiamos todas las ventanas abiertas
    lienzoInsertSort.pack_forget()
    lienzoMergeSort.pack_forget()
    lienzoRadixSort.pack_forget()
    lienzoBubbleSort.pack_forget()
    lienzoHeapSort.pack_forget()
    lienzoQuickSort.pack_forget()
    lienzoBucketSort.pack_forget()
    lienzoSelectionSort.pack_forget()
    lienzoCombSort.pack_forget()
    lienzoArregloDefinido.pack_forget()
    #Eliminamos la ventanas de resultados:
    VentanaInsertOrdenado.destroy()
    VentanaMergeOrdenado.destroy()
    VentanaSelectionOrdenado.destroy()
    VentanaBubbleOrdenado.destroy()
    VentanaBucketOrdenado.destroy()
    VentanaCombOrdenado.destroy()
    VentanaQuickOrdenado.destroy()
    VentanaRadixOrdenado.destroy()
    VentanaHeapOrdenado.destroy()
    #Mostramos la ventana requerida
    lienzoShellSort.pack()    

def VentanaRadixSort():
    #Regresamos a su forma anterior
    root.geometry("750x425+340+100")
    #Limpiamos todas las ventanas abiertas
    lienzoInsertSort.pack_forget()
    lienzoMergeSort.pack_forget()
    lienzoShellSort.pack_forget()
    lienzoBubbleSort.pack_forget()
    lienzoHeapSort.pack_forget()
    lienzoQuickSort.pack_forget()
    lienzoBucketSort.pack_forget()
    lienzoSelectionSort.pack_forget()
    lienzoCombSort.pack_forget()
    lienzoArregloDefinido.pack_forget()
    #Eliminamos la ventanas de resultados:
    VentanaInsertOrdenado.destroy()
    VentanaMergeOrdenado.destroy()
    VentanaShellOrdenado.destroy()
    VentanaBubbleOrdenado.destroy()
    VentanaBucketOrdenado.destroy()
    VentanaCombOrdenado.destroy()
    VentanaQuickOrdenado.destroy()
    VentanaSelectionOrdenado.destroy()
    VentanaHeapOrdenado.destroy()
    #Mostramos la ventana requerida
    lienzoRadixSort.pack() 

def VentanaBubbleSort():
    #Regresamos a su forma anterior
    root.geometry("750x425+340+100")
    #Limpiamos todas las ventanas abiertas
    lienzoInsertSort.pack_forget()
    lienzoMergeSort.pack_forget()
    lienzoShellSort.pack_forget()
    lienzoRadixSort.pack_forget()
    lienzoHeapSort.pack_forget()
    lienzoQuickSort.pack_forget()
    lienzoBucketSort.pack_forget()
    lienzoSelectionSort.pack_forget()
    lienzoCombSort.pack_forget()
    lienzoArregloDefinido.pack_forget()
    #Eliminamos la ventanas de resultados:
    VentanaInsertOrdenado.destroy()
    VentanaMergeOrdenado.destroy()
    VentanaShellOrdenado.destroy()
    VentanaSelectionOrdenado.destroy()
    VentanaBucketOrdenado.destroy()
    VentanaCombOrdenado.destroy()
    VentanaQuickOrdenado.destroy()
    VentanaRadixOrdenado.destroy()
    VentanaHeapOrdenado.destroy()
    #Mostramos la ventana requerida
    lienzoBubbleSort.pack() 
    
def VentanaHeapSort():
    #Regresamos a su forma anterior
    root.geometry("750x425+340+100")
    #Limpiamos todas las ventanas abiertas
    lienzoInsertSort.pack_forget()
    lienzoMergeSort.pack_forget()
    lienzoShellSort.pack_forget()
    lienzoRadixSort.pack_forget()
    lienzoBubbleSort.pack_forget()
    lienzoQuickSort.pack_forget()
    lienzoBucketSort.pack_forget()
    lienzoSelectionSort.pack_forget()
    lienzoCombSort.pack_forget()
    lienzoArregloDefinido.pack_forget()
    #Eliminamos la ventanas de resultados:
    VentanaInsertOrdenado.destroy()
    VentanaMergeOrdenado.destroy()
    VentanaShellOrdenado.destroy()
    VentanaBubbleOrdenado.destroy()
    VentanaBucketOrdenado.destroy()
    VentanaCombOrdenado.destroy()
    VentanaQuickOrdenado.destroy()
    VentanaRadixOrdenado.destroy()
    VentanaSelectionOrdenado.destroy()
    #Mostramos la ventana requerida
    lienzoHeapSort.pack() 

def VentanaQuickSort():
    #Regresamos a su forma anterior
    root.geometry("750x425+340+100")
    #Limpiamos todas las ventanas abiertas
    lienzoInsertSort.pack_forget()
    lienzoMergeSort.pack_forget()
    lienzoShellSort.pack_forget()
    lienzoRadixSort.pack_forget()
    lienzoBubbleSort.pack_forget()
    lienzoHeapSort.pack_forget()
    lienzoBucketSort.pack_forget()
    lienzoSelectionSort.pack_forget()
    lienzoCombSort.pack_forget()
    lienzoArregloDefinido.pack_forget()
    #Eliminamos la ventanas de resultados:
    VentanaInsertOrdenado.destroy()
    VentanaMergeOrdenado.destroy()
    VentanaShellOrdenado.destroy()
    VentanaBubbleOrdenado.destroy()
    VentanaBucketOrdenado.destroy()
    VentanaCombOrdenado.destroy()
    VentanaSelectionOrdenado.destroy()
    VentanaRadixOrdenado.destroy()
    VentanaHeapOrdenado.destroy()
    #Mostramos la ventana requerida
    lienzoQuickSort.pack()

def VentanaBucketSort():
    #Regresamos a su forma anterior
    root.geometry("750x425+340+100")
    #Limpiamos todas las ventanas abiertas
    lienzoInsertSort.pack_forget()
    lienzoMergeSort.pack_forget()
    lienzoShellSort.pack_forget()
    lienzoRadixSort.pack_forget()
    lienzoBubbleSort.pack_forget()
    lienzoHeapSort.pack_forget()
    lienzoQuickSort.pack_forget()
    lienzoSelectionSort.pack_forget()
    lienzoCombSort.pack_forget()
    lienzoArregloDefinido.pack_forget()
    #Eliminamos la ventanas de resultados:
    VentanaInsertOrdenado.destroy()
    VentanaMergeOrdenado.destroy()
    VentanaShellOrdenado.destroy()
    VentanaBubbleOrdenado.destroy()
    VentanaSelectionOrdenado.destroy()
    VentanaCombOrdenado.destroy()
    VentanaQuickOrdenado.destroy()
    VentanaRadixOrdenado.destroy()
    VentanaHeapOrdenado.destroy()
    #Mostramos la ventana requerida
    lienzoBucketSort.pack()

def VentanaSelectionSort():
    #Regresamos a su forma anterior
    root.geometry("750x425+340+100")
    #Limpiamos todas las ventanas abiertas
    lienzoInsertSort.pack_forget()
    lienzoMergeSort.pack_forget()
    lienzoShellSort.pack_forget()
    lienzoRadixSort.pack_forget()
    lienzoBubbleSort.pack_forget()
    lienzoHeapSort.pack_forget()
    lienzoQuickSort.pack_forget()
    lienzoBucketSort.pack_forget()
    lienzoCombSort.pack_forget()
    lienzoArregloDefinido.pack_forget()
    #Eliminamos la ventanas de resultados:
    VentanaInsertOrdenado.destroy()
    VentanaMergeOrdenado.destroy()
    VentanaShellOrdenado.destroy()
    VentanaBubbleOrdenado.destroy()
    VentanaBucketOrdenado.destroy()
    VentanaCombOrdenado.destroy()
    VentanaQuickOrdenado.destroy()
    VentanaRadixOrdenado.destroy()
    VentanaHeapOrdenado.destroy()
    #Mostramos la ventana requerida
    lienzoSelectionSort.pack()

def VentanaCombSort():
    #Regresamos a su forma anterior
    root.geometry("750x425+340+100")
    #Limpiamos todas las ventanas abiertas
    lienzoInsertSort.pack_forget()
    lienzoMergeSort.pack_forget()
    lienzoShellSort.pack_forget()
    lienzoRadixSort.pack_forget()
    lienzoBubbleSort.pack_forget()
    lienzoHeapSort.pack_forget()
    lienzoQuickSort.pack_forget()
    lienzoBucketSort.pack_forget()
    lienzoSelectionSort.pack_forget()
    lienzoArregloDefinido.pack_forget()
    #Eliminamos la ventanas de resultados:
    VentanaInsertOrdenado.destroy()
    VentanaMergeOrdenado.destroy()
    VentanaShellOrdenado.destroy()
    VentanaBubbleOrdenado.destroy()
    VentanaBucketOrdenado.destroy()
    VentanaSelectionOrdenado.destroy()
    VentanaQuickOrdenado.destroy()
    VentanaRadixOrdenado.destroy()
    VentanaHeapOrdenado.destroy()
    #Mostramos la ventana requerida
    lienzoCombSort.pack()

def VentanaArregloDefinido():
    #Regresamos a su forma anterior
    root.geometry("750x425+340+100")
    #Limpiamos todas las ventanas abiertas
    lienzoInsertSort.pack_forget()
    lienzoMergeSort.pack_forget()
    lienzoShellSort.pack_forget()
    lienzoRadixSort.pack_forget()
    lienzoBubbleSort.pack_forget()
    lienzoHeapSort.pack_forget()
    lienzoQuickSort.pack_forget()
    lienzoBucketSort.pack_forget()
    lienzoSelectionSort.pack_forget()
    lienzoCombSort.pack_forget()
    #Eliminamos la ventanas de resultados:
    VentanaSelectionOrdenado.destroy()
    VentanaMergeOrdenado.destroy()
    VentanaShellOrdenado.destroy()
    VentanaBubbleOrdenado.destroy()
    VentanaBucketOrdenado.destroy()
    VentanaCombOrdenado.destroy()
    VentanaQuickOrdenado.destroy()
    VentanaRadixOrdenado.destroy()
    VentanaHeapOrdenado.destroy()
    VentanaInsertOrdenado.destroy()
    #Mostramos la ventana requerida
    lienzoArregloDefinido.pack()

def CrearVentanaOrdenarArregloDefinido():
    
    if(opcion.get()!=1 and opcion.get()!=2 and opcion.get()!=3 and opcion.get()!=4 and opcion.get()!=5 and opcion.get()!=6 and opcion.get()!=7 and opcion.get()!=8 and opcion.get()!=9 and opcion.get()!=10 ):
        messagebox.showwarning("Alerta","Por favor seleccione un algoritmo de ordenacion")
    else:
        EntradaDefinido=EntradaArregloDefinido.get("1.0",END)
        #Transfrmamos el arreglo ingresado como texto a numeros:
        
        A=EntradaDefinido.replace("[","")[::-1].replace("]","")[::-1].replace(","," ")
        A=A.split()
        ArregloDefinido=[]
        tiempoOrdenacion=0.0
        tiempoInicio=0.0
        tiempoFin=0.0

        #============================================================================
        #Saber que opcion se selecciono:
        cadena=""
        NoHayError=True
        if(opcion.get()==1):
            cadena="Insert Sort"
            #Transformamos la entrada a numeros
            for x in range(len(A)):
                if(not('.'in A[x])):
                    ArregloDefinido.append(int(A[x]))
                else:
                    ArregloDefinido.append(float(A[x]))
            
        elif(opcion.get()==2):
            cadena="Merge Sort"
            #Transformamos la entrada a numeros
            for x in range(len(A)):
                if(not('.'in A[x])):
                    ArregloDefinido.append(int(A[x]))
                else:
                    ArregloDefinido.append(float(A[x]))
        elif(opcion.get()==3):
            cadena="Shell Sort"
            #Transformamos la entrada a numeros
            for x in range(len(A)):
                if(not('.'in A[x])):
                    ArregloDefinido.append(int(A[x]))
                else:
                    ArregloDefinido.append(float(A[x]))
        elif(opcion.get()==4):
            cadena="Radix Sort"
            #Aqui hay restricciones
            #Transformaos la entrada a numeros
            for x in range(len(A)):
                if(not('.'in A[x]) and int(A[x])>=0):#Que sean enteros y positivos
                    ArregloDefinido.append(int(A[x]))
                else:
                    #Mostrar error:
                    messagebox.showerror("Error","Hay error en el elemento cuyo valor es: "+A[x]+"\nTodos los elementos del arreglo ingresado \n deben de ser ENTEROS >=0")
                    NoHayError=False
                    #Salir del bucle
                    break
        elif(opcion.get()==5):
            cadena="Bubble Sort"
            #Transformaos la entrada a numeros
            for x in range(len(A)):
                if(not('.'in A[x])):
                    ArregloDefinido.append(int(A[x]))
                else:
                    ArregloDefinido.append(float(A[x]))

        elif(opcion.get()==6):
            cadena="Heap Sort"
            #Transformaos la entrada a numeros
            for x in range(len(A)):
                if(not('.'in A[x])):
                    ArregloDefinido.append(int(A[x]))
                else:
                    ArregloDefinido.append(float(A[x]))
        elif(opcion.get()==7):
            cadena="Quick Sort"
            #Transformaos la entrada a numeros
            for x in range(len(A)):
                if(not('.'in A[x])):
                    ArregloDefinido.append(int(A[x]))
                else:
                    ArregloDefinido.append(float(A[x]))
        elif(opcion.get()==8):
            cadena="Bucket Sort"
            #Restriccion:Elementos >=0 y <1 de preferencia cantidad de elementos >=10
            for x in range(len(A)):
                if(not(float(A[x])>=0 and float(A[x])<1)):#not('0.'in A[x])):
                    #Mostrar Error
                    messagebox.showerror("Error en el arreglo Ingresado","Hay error en el elemento cuyo valor es: "+A[x]+"\n Todos los elementos del arreglo ingresado \n deben de ser >=0 y <1")
                    NoHayError=False
                    break
                else:
                    ArregloDefinido.append(float(A[x]))

        elif(opcion.get()==9):
            cadena="Selection Sort"
            for x in range(len(A)):
                if(not('.'in A[x])):
                    ArregloDefinido.append(int(A[x]))
                else:
                    ArregloDefinido.append(float(A[x]))

        else:
            cadena="Comb Sort"
            for x in range(len(A)):
                if(not('.'in A[x])):
                    ArregloDefinido.append(int(A[x]))
                else:
                    ArregloDefinido.append(float(A[x]))

        #Se halla el tiempo que toma cada algoritmo:
        #Creamos la ventana si no hay errores:
        if(NoHayError):
            #Segun la opcion marcada hallamos el resultado:
            if(opcion==1):
                #Ordenar por insert sort
                tiempoInicio=perf_counter()
                InsertSort(ArregloDefinido,len(ArregloDefinido))
                tiempoFin=perf_counter()
                tiempoOrdenacion=tiempoFin-tiempoInicio
            elif(opcion==2):
                #Ordenar por Merge sort
                tiempoInicio=perf_counter()
                MergeSort(ArregloDefinido,0,len(ArregloDefinido)-1)
                tiempoFin=perf_counter()
                tiempoOrdenacion=tiempoFin-tiempoInicio
            elif(opcion==3):
                #Ordenar por Shell sort
                tiempoInicio=perf_counter()
                ShellSort(ArregloDefinido,len(ArregloDefinido))
                tiempoFin=perf_counter()
                tiempoOrdenacion=tiempoFin-tiempoInicio
            elif(opcion==4):
                #Ordenar por Radix sort
                tiempoInicio=perf_counter()
                RadixSort(ArregloDefinido,len(ArregloDefinido))
                tiempoFin=perf_counter()
                tiempoOrdenacion=tiempoFin-tiempoInicio
            elif(opcion==5):
                #Ordenar por Bubble sort
                tiempoInicio=perf_counter()
                BubbleSort(ArregloDefinido,len(ArregloDefinido))
                tiempoFin=perf_counter()
                tiempoOrdenacion=tiempoFin-tiempoInicio
            elif(opcion==6):
                #Ordenar por Heap sort
                tiempoInicio=perf_counter()
                HeapSort(ArregloDefinido,len(ArregloDefinido))
                tiempoFin=perf_counter()
                tiempoOrdenacion=tiempoFin-tiempoInicio
            elif(opcion==7):
                #Ordenar por Quick sort
                tiempoInicio=perf_counter()
                QuickSort(ArregloDefinido,0,len(ArregloDefinido)-1)
                tiempoFin=perf_counter()
                tiempoOrdenacion=tiempoFin-tiempoInicio
            elif(opcion==8):
                #Ordenar por Bucket sort
                tiempoInicio=perf_counter()
                BucketSort(ArregloDefinido,len(ArregloDefinido))
                tiempoFin=perf_counter()
                tiempoOrdenacion=tiempoFin-tiempoInicio
            elif(opcion==9):
                #Ordenar por Selection sort
                tiempoInicio=perf_counter()
                SelectionSort(ArregloDefinido,len(ArregloDefinido))
                tiempoFin=perf_counter()
                tiempoOrdenacion=tiempoFin-tiempoInicio
            else:
                #Ordenar por Comb sort
                tiempoInicio=perf_counter()
                CombSort(ArregloDefinido)
                tiempoFin=perf_counter()
                tiempoOrdenacion=tiempoFin-tiempoInicio

            #Creamos la ventana
            VentanaResultadosArregloDefinido=Toplevel()
            VentanaResultadosArregloDefinido.title("Resultados:")
            VentanaResultadosArregloDefinido.iconbitmap("Logo-UNSAAC.ico")
            VentanaResultadosArregloDefinido.configure(bg="#9D1321")
            VentanaResultadosArregloDefinido.geometry("%dx%d+%d+%d" % (550,480,700,150)) #Tamaño y posicion
            #Mostramos las matrices  de ordenacion:(esto podria ir dentro de cada if o elif)
            Label(VentanaResultadosArregloDefinido, text="El arreglo ordenado por el algoritmo\n"+cadena+" es:", fg="#FFD767",bg="#9D1321",font=('Calibri', 12)).place(x=10,y=10)
            ResultadosOrdenarArregloDefinido=ScrolledText(VentanaResultadosArregloDefinido, width=23,  height=17,bg="#7092BE")
            ResultadosOrdenarArregloDefinido.place(x=20,y=74)
            Label(VentanaResultadosArregloDefinido, text="El tiempo que tomó ordenar por el algoritmo\n"+cadena+" es:", fg="#FFD767",bg="#9D1321",font=('Calibri', 13)).place(x=230,y=90)
            TiempoOrdenarArregloDefinido=Entry(VentanaResultadosArregloDefinido,bg="#C3A88B",font=('consolas', 12),bd=5,width=23)
            TiempoOrdenarArregloDefinido.place(x=300,y=150)

            #Mostramos los datos en el scrolltext.
            #mostramos las matrices en el form Mejor Caso
            #ResultadosOrdenarArregloDefinido.delete("1.0","end")#Para borrar el contenido anterior 
            StrMejor=", ".join([str(_) for _ in ArregloDefinido])
            ResultadosOrdenarArregloDefinido.insert(END, "[ "+StrMejor+" ]")

            #Escribimos el tiempo de ejecucion.
            TiempoOrdenarArregloDefinido.insert(END, str(tiempoOrdenacion))

            #No se hace otra accion hasta que se cierre esta ventana:(Se puede omitir)
            VentanaResultadosArregloDefinido.transient(master=root)
            VentanaResultadosArregloDefinido.grab_set()
            root.wait_window(VentanaResultadosArregloDefinido)




def VerificarOpcion():
    if(opcion.get()==8):#Cuando se marco Bucket Sort
        messagebox.showinfo("Precaucion","Asegurese de que los elementos pertenezcan al rango [0,1>")
    else:#Para cuando la opcion marcada es Radix Sort
        messagebox.showinfo("Precaucion","Asegurese de que los elementos sean 'Enteros' mayores o iguales que cero")

#BTNINSERT SORT
def PressBtnInsert():
    #VentanaInsertOrdenado.destroy()
    #Extraemos la cantidad ingresada:
    longitud=int(tamanioInsert.get())
    #Creamos las matrices Mejor,Peor y caso promedio(Haciendo uso de la libreria GeneradorArreglos)
    MejorInsert,PromedioInsert,PeorInsert=GenArreglosInsertSort(longitud)
    #Convertimos a string y lo mostramos en el scrolltext:

    #mostramos las matrices en el form Mejor Caso
    txtMejorCasoInsert.delete("1.0","end")#Para borrar el contenido anterior 
    StrMejor=", ".join([str(_) for _ in MejorInsert])
    txtMejorCasoInsert.insert(END, "[ "+StrMejor+" ]")

    #mostramos las matrices en el form Caso Promedio
    txtPromedioCasoInsert.delete("1.0","end")#Para borrar el contenido anterior 
    StrPromedio=", ".join([str(_) for _ in PromedioInsert])
    txtPromedioCasoInsert.insert(END, "[ "+StrPromedio+" ]")

    #mostramos las matrices en el form Peor Caso
    txtPeorCasoInsert.delete("1.0","end")#Para borrar el contenido anterior 
    StrPeor=", ".join([str(_) for _ in PeorInsert])
    txtPeorCasoInsert.insert(END, "[ "+StrPeor+" ]")

    #Cambia de posicion de la ventana princpal para mostrar las 3 matrices ordenadas.
    root.geometry("750x425+15+100")
    global VentanaInsertOrdenado
    VentanaInsertOrdenado=Toplevel()
    VentanaInsertOrdenado.title("InsertionSort")
    VentanaInsertOrdenado.iconbitmap("Logo-UNSAAC.ico")
    VentanaInsertOrdenado.configure(bg="#4C4A6C")
    VentanaInsertOrdenado.geometry("%dx%d+%d+%d" % (640,365,710,150)) #Tamaño y posicion
    Label(VentanaInsertOrdenado, text="Los Arreglos Ordenados, son:", fg="black",bg="#4C4A6C",font=('Doppio One Regular', 11)).place(x=10,y=10)#FFD767"'Calibri'
    
    #Titulos:
    Label(VentanaInsertOrdenado, text="Mejor Caso", fg="#EEEFF1",bg="#4C4A6C",font=('Doppio One Regular', 12)).place(x=60,y=30)
    txtMejorCasoInsertResul=ScrolledText(VentanaInsertOrdenado, width=23,  height=17,bg="#7092BE")
    txtMejorCasoInsertResul.place(x=10,y=56)
    Label(VentanaInsertOrdenado, text="Caso Promedio", fg="#EEEFF1",bg="#4C4A6C",font=('Doppio One Regular', 12)).place(x=260,y=30)
    txtPromedioCasoInsertResul=ScrolledText(VentanaInsertOrdenado, width=23,  height=17,bg="#EEEFF1")
    txtPromedioCasoInsertResul.place(x=220,y=56)
    Label(VentanaInsertOrdenado, text="Peor Caso", fg="#EEEFF1",bg="#4C4A6C",font=('Doppio One Regular', 12)).place(x=490,y=30)
    txtPeorCasoInsertResul=ScrolledText(VentanaInsertOrdenado, width=23,  height=17,bg="#8080C0")
    txtPeorCasoInsertResul.place(x=430,y=56)

    #Mostramos los arreglos ordenados:(llamamos al modulo que contiene a todos los modulos de ordenacion)

    #Medimos el tiempo Mejor:
    tiempoInicio=0.0
    tiempoFin=0.0
    tiempoInicio=perf_counter()
    InsertSort(MejorInsert,len(MejorInsert))
    tiempoFin=perf_counter()
    tiempoOrdenacion=tiempoFin-tiempoInicio
    ResultadosMejorInsert.delete(0,END)
    ResultadosMejorInsert.insert(END, str(tiempoOrdenacion))

    #Medimos el tiempo Promedio:
    tiempoInicio=0.0
    tiempoFin=0.0
    tiempoInicio=perf_counter()
    InsertSort(PromedioInsert,len(PromedioInsert))
    tiempoFin=perf_counter()
    tiempoOrdenacion=tiempoFin-tiempoInicio
    ResultadosPromedioInsert.delete(0,END)#Para borrar el contenido anterior 
    ResultadosPromedioInsert.insert(END, str(tiempoOrdenacion))

    #Medimos el tiempo Peor:
    tiempoInicio=0.0
    tiempoFin=0.0
    tiempoInicio=perf_counter()
    InsertSort(PeorInsert,len(PeorInsert))
    tiempoFin=perf_counter()
    tiempoOrdenacion=tiempoFin-tiempoInicio
    ResultadosPeorInsert.delete(0,END)#Para borrar el contenido anterior 
    ResultadosPeorInsert.insert(END, str(tiempoOrdenacion))


    #Convertimos a strings los resultados:
    #mostramos las matrices en el form Mejor Caso
    txtMejorCasoInsertResul.delete("1.0","end")#Para borrar el contenido anterior 
    StrMejorInsertSort=", ".join([str(_) for _ in MejorInsert])
    txtMejorCasoInsertResul.insert(END, "[ "+StrMejorInsertSort+" ]")

    #mostramos las matrices en el form Caso Promedio
    txtPromedioCasoInsertResul.delete("1.0","end")#Para borrar el contenido anterior 
    StrPromedioInsertSort=", ".join([str(_) for _ in PromedioInsert])
    txtPromedioCasoInsertResul.insert(END, "[ "+StrPromedioInsertSort+" ]")

    #mostramos las matrices en el form Peor Caso
    txtPeorCasoInsertResul.delete("1.0","end")#Para borrar el contenido anterior 
    StrPeorInsertSort=", ".join([str(_) for _ in PeorInsert])
    txtPeorCasoInsertResul.insert(END, "[ "+StrPeorInsertSort+" ]")

    




#BTN MERGE SORT
def PressBtnMerge():

    #Extraemos la cantidad ingresada:
    longitud=int(tamanioMerge.get())
    #Creamos las matrices Mejor,Peor y caso promedio(Haciendo uso de la libreria GeneradorArreglos)
    MejorMerge,PromedioMerge,PeorMerge=GenArreglosMergeSort(longitud)
    #Convertimos a string y lo mostramos en el scrolltext:
    #mostramos las matrices en el form Mejor Caso
    txtMejorCasoMerge.delete("1.0","end")#Para borrar el contenido anterior 
    StrMejor=", ".join([str(_) for _ in MejorMerge])
    txtMejorCasoMerge.insert(END, "[ "+StrMejor+" ]")

    #mostramos las matrices en el form Caso Promedio
    txtPromedioCasoMerge.delete("1.0","end")#Para borrar el contenido anterior 
    StrPromedio=", ".join([str(_) for _ in PromedioMerge])
    txtPromedioCasoMerge.insert(END, "[ "+StrPromedio+" ]")

    #mostramos las matrices en el form Peor Caso
    txtPeorCasoMerge.delete("1.0","end")#Para borrar el contenido anterior 
    StrPeor=", ".join([str(_) for _ in PeorMerge])
    txtPeorCasoMerge.insert(END, "[ "+StrPeor+" ]")

    root.geometry("750x425+15+100")
    global VentanaMergeOrdenado
    VentanaMergeOrdenado=Toplevel()
    VentanaMergeOrdenado.title("MergeSort")
    VentanaMergeOrdenado.iconbitmap("Logo-UNSAAC.ico")
    VentanaMergeOrdenado.configure(bg="#4C4A6C")
    #VentanaInsertOrdenado.configure(bg="#9D1321")
    VentanaMergeOrdenado.geometry("%dx%d+%d+%d" % (640,365,710,150)) #Tamaño y posicion
    Label(VentanaMergeOrdenado, text="Los Arreglos Ordenados, son:", fg="black",bg="#4C4A6C",font=('Doppio One Regular', 11)).place(x=10,y=10)#FFD767"'Calibri'
    Label(VentanaMergeOrdenado, text="Mejor Caso", fg="#EEEFF1",bg="#4C4A6C",font=('Doppio One Regular', 12)).place(x=60,y=30)
    txtMejorCasoMergeResul=ScrolledText(VentanaMergeOrdenado, width=23,  height=17,bg="#7092BE")
    txtMejorCasoMergeResul.place(x=10,y=56)
    Label(VentanaMergeOrdenado, text="Caso Promedio", fg="#EEEFF1",bg="#4C4A6C",font=('Doppio One Regular', 12)).place(x=260,y=30)
    txtPromedioCasoMergeResul=ScrolledText(VentanaMergeOrdenado, width=23,  height=17,bg="#EEEFF1")
    txtPromedioCasoMergeResul.place(x=220,y=56)
    Label(VentanaMergeOrdenado, text="Peor Caso", fg="#EEEFF1",bg="#4C4A6C",font=('Doppio One Regular', 12)).place(x=490,y=30)
    txtPeorCasoMergeResul=ScrolledText(VentanaMergeOrdenado, width=23,  height=17,bg="#8080C0")
    txtPeorCasoMergeResul.place(x=430,y=56)


    #Mostramos los arreglos ordenados:(llamamos al modulo que contiene a todos los modulos de ordenacion)

    #Medimos el tiempo Mejor:
    tiempoInicio=0.0
    tiempoFin=0.0
    tiempoInicio=perf_counter()
    MergeSort(MejorMerge,0,len(MejorMerge)-1)
    tiempoFin=perf_counter()
    tiempoOrdenacion=tiempoFin-tiempoInicio
    ResultadosMejorMerge.delete(0,END)
    ResultadosMejorMerge.insert(END, str(tiempoOrdenacion))

    #Medimos el tiempo Promedio:
    tiempoInicio=0.0
    tiempoFin=0.0
    tiempoInicio=perf_counter()
    MergeSort(PromedioMerge,0,len(PromedioMerge)-1)
    tiempoFin=perf_counter()
    tiempoOrdenacion=tiempoFin-tiempoInicio
    ResultadosPromedioMerge.delete(0,END)#Para borrar el contenido anterior 
    ResultadosPromedioMerge.insert(END, str(tiempoOrdenacion))

    #Medimos el tiempo Peor:
    tiempoInicio=0.0
    tiempoFin=0.0
    tiempoInicio=perf_counter()
    MergeSort(PeorMerge,0,len(PeorMerge)-1)
    tiempoFin=perf_counter()
    tiempoOrdenacion=tiempoFin-tiempoInicio
    ResultadosPeorMerge.delete(0,END)#Para borrar el contenido anterior 
    ResultadosPeorMerge.insert(END, str(tiempoOrdenacion))


    
    #Convertimos a strings los resultados:
    #mostramos las matrices en el form Mejor Caso
    txtMejorCasoMergeResul.delete("1.0","end")#Para borrar el contenido anterior 
    StrMejorMergeSort=", ".join([str(_) for _ in MejorMerge])
    txtMejorCasoMergeResul.insert(END, "[ "+StrMejorMergeSort+" ]")

    #mostramos las matrices en el form Caso Promedio
    txtPromedioCasoMergeResul.delete("1.0","end")#Para borrar el contenido anterior 
    StrPromedioMergeSort=", ".join([str(_) for _ in PromedioMerge])
    txtPromedioCasoMergeResul.insert(END, "[ "+StrPromedioMergeSort+" ]")

    #mostramos las matrices en el form Peor Caso
    txtPeorCasoMergeResul.delete("1.0","end")#Para borrar el contenido anterior 
    StrPeorMergeSort=", ".join([str(_) for _ in PeorMerge])
    txtPeorCasoMergeResul.insert(END, "[ "+StrPeorMergeSort+" ]")



#BTN SHELL SORT
def PressBtnShell():

    #Extraemos la cantidad ingresada:
    longitud=int(tamanioShell.get())
    #Creamos las matrices Mejor,Peor y caso promedio(Haciendo uso de la libreria GeneradorArreglos)
    MejorShell,PromedioShell,PeorShell=GenArreglosShellSort(longitud)
    #Convertimos a string y lo mostramos en el scrolltext:
    #mostramos las matrices en el form Mejor Caso
    txtMejorCasoShell.delete("1.0","end")#Para borrar el contenido anterior 
    StrMejor=", ".join([str(_) for _ in MejorShell])
    txtMejorCasoShell.insert(END, "[ "+StrMejor+" ]")

    #mostramos las matrices en el form Caso Promedio
    txtPromedioCasoShell.delete("1.0","end")#Para borrar el contenido anterior 
    StrPromedio=", ".join([str(_) for _ in PromedioShell])
    txtPromedioCasoShell.insert(END, "[ "+StrPromedio+" ]")

    #mostramos las matrices en el form Peor Caso
    txtPeorCasoShell.delete("1.0","end")#Para borrar el contenido anterior 
    StrPeor=", ".join([str(_) for _ in PeorShell])
    txtPeorCasoShell.insert(END, "[ "+StrPeor+" ]")


    root.geometry("750x425+15+100")
    global VentanaShellOrdenado
    VentanaShellOrdenado=Toplevel()
    VentanaShellOrdenado.title("ShellSort")
    VentanaShellOrdenado.iconbitmap("Logo-UNSAAC.ico")
    VentanaShellOrdenado.configure(bg="#4C4A6C")
    #VentanaInsertOrdenado.configure(bg="#9D1321")
    VentanaShellOrdenado.geometry("%dx%d+%d+%d" % (640,365,710,150)) #Tamaño y posicion
    Label(VentanaShellOrdenado, text="Los Arreglos Ordenados, son:", fg="black",bg="#4C4A6C",font=('Doppio One Regular', 11)).place(x=10,y=10)
    Label(VentanaShellOrdenado, text="Mejor Caso", fg="#EEEFF1",bg="#4C4A6C",font=('Doppio One Regular', 12)).place(x=60,y=30)
    txtMejorCasoShellResul=ScrolledText(VentanaShellOrdenado, width=23,  height=17,bg="#7092BE")
    txtMejorCasoShellResul.place(x=10,y=56)
    Label(VentanaShellOrdenado, text="Caso Promedio", fg="#EEEFF1",bg="#4C4A6C",font=('Doppio One Regular', 12)).place(x=260,y=30)
    txtPromedioCasoShellResul=ScrolledText(VentanaShellOrdenado, width=23,  height=17,bg="#EEEFF1")
    txtPromedioCasoShellResul.place(x=220,y=56)
    Label(VentanaShellOrdenado, text="Peor Caso", fg="#EEEFF1",bg="#4C4A6C",font=('Doppio One Regular', 12)).place(x=490,y=30)
    txtPeorCasoShellResul=ScrolledText(VentanaShellOrdenado, width=23,  height=17,bg="#8080C0")
    txtPeorCasoShellResul.place(x=430,y=56)



    #Mostramos los arreglos ordenados:(llamamos al modulo que contiene a todos los modulos de ordenacion)

    #Medimos el tiempo Mejor:
    tiempoInicio=0.0
    tiempoFin=0.0
    tiempoInicio=perf_counter()
    ShellSort(MejorShell,len(MejorShell))
    tiempoFin=perf_counter()
    tiempoOrdenacion=tiempoFin-tiempoInicio
    ResultadosMejorShell.delete(0,END)
    ResultadosMejorShell.insert(END, str(tiempoOrdenacion))

    #Medimos el tiempo Promedio:
    tiempoInicio=0.0
    tiempoFin=0.0
    tiempoInicio=perf_counter()
    ShellSort(PromedioShell,len(PromedioShell))
    tiempoFin=perf_counter()
    tiempoOrdenacion=tiempoFin-tiempoInicio
    ResultadosPromedioShell.delete(0,END)#Para borrar el contenido anterior 
    ResultadosPromedioShell.insert(END, str(tiempoOrdenacion))

    #Medimos el tiempo Peor:
    tiempoInicio=0.0
    tiempoFin=0.0
    tiempoInicio=perf_counter()
    ShellSort(PeorShell,len(PeorShell))
    tiempoFin=perf_counter()
    tiempoOrdenacion=tiempoFin-tiempoInicio
    ResultadosPeorShell.delete(0,END)#Para borrar el contenido anterior 
    ResultadosPeorShell.insert(END, str(tiempoOrdenacion))


    
    #Convertimos a strings los resultados:
    #mostramos las matrices en el form Mejor Caso
    txtMejorCasoShellResul.delete("1.0","end")#Para borrar el contenido anterior 
    StrMejorShellSort=", ".join([str(_) for _ in MejorShell])
    txtMejorCasoShellResul.insert(END, "[ "+StrMejorShellSort+" ]")

    #mostramos las matrices en el form Caso Promedio
    txtPromedioCasoShellResul.delete("1.0","end")#Para borrar el contenido anterior 
    StrPromedioShellSort=", ".join([str(_) for _ in PromedioShell])
    txtPromedioCasoShellResul.insert(END, "[ "+StrPromedioShellSort+" ]")

    #mostramos las matrices en el form Peor Caso
    txtPeorCasoShellResul.delete("1.0","end")#Para borrar el contenido anterior 
    StrPeorShellSort=", ".join([str(_) for _ in PeorShell])
    txtPeorCasoShellResul.insert(END, "[ "+StrPeorShellSort+" ]")



#BTN RADIX SORT
def PressBtnRadix():

    #Extraemos la cantidad ingresada:
    longitud=int(tamanioRadix.get())
    #Creamos las matrices Mejor,Peor y caso promedio(Haciendo uso de la libreria GeneradorArreglos)
    MejorRadix,PromedioRadix,PeorRadix=GenArreglosRadixSort(longitud)
    #Convertimos a string y lo mostramos en el scrolltext:
    #mostramos las matrices en el form Mejor Caso
    txtMejorCasoRadix.delete("1.0","end")#Para borrar el contenido anterior 
    StrMejor=", ".join([str(_) for _ in MejorRadix])
    txtMejorCasoRadix.insert(END, "[ "+StrMejor+" ]")

    #mostramos las matrices en el form Caso Promedio
    txtPromedioCasoRadix.delete("1.0","end")#Para borrar el contenido anterior 
    StrPromedio=", ".join([str(_) for _ in PromedioRadix])
    txtPromedioCasoRadix.insert(END, "[ "+StrPromedio+" ]")

    #mostramos las matrices en el form Peor Caso
    txtPeorCasoRadix.delete("1.0","end")#Para borrar el contenido anterior 
    StrPeor=", ".join([str(_) for _ in PeorRadix])
    txtPeorCasoRadix.insert(END, "[ "+StrPeor+" ]")

    root.geometry("750x425+15+100")
    global VentanaRadixOrdenado
    VentanaRadixOrdenado=Toplevel()
    VentanaRadixOrdenado.title("RadixSort")
    VentanaRadixOrdenado.iconbitmap("Logo-UNSAAC.ico")
    VentanaRadixOrdenado.configure(bg="#4C4A6C")
    #VentanaInsertOrdenado.configure(bg="#9D1321")
    VentanaRadixOrdenado.geometry("%dx%d+%d+%d" % (640,365,710,150)) #Tamaño y posicion
    Label(VentanaRadixOrdenado, text="Los Arreglos Ordenados, son:", fg="black",bg="#4C4A6C",font=('Doppio One Regular', 11)).place(x=10,y=10)
    Label(VentanaRadixOrdenado, text="Mejor Caso", fg="#EEEFF1",bg="#4C4A6C",font=('Doppio One Regular', 12)).place(x=60,y=30)
    txtMejorCasoRadixResul=ScrolledText(VentanaRadixOrdenado, width=23,  height=17,bg="#7092BE")
    txtMejorCasoRadixResul.place(x=10,y=56)
    Label(VentanaRadixOrdenado, text="Caso Promedio", fg="#EEEFF1",bg="#4C4A6C",font=('Doppio One Regular', 12)).place(x=260,y=30)
    txtPromedioCasoRadixResul=ScrolledText(VentanaRadixOrdenado, width=23,  height=17,bg="#EEEFF1")
    txtPromedioCasoRadixResul.place(x=220,y=56)
    Label(VentanaRadixOrdenado, text="Peor Caso", fg="#EEEFF1",bg="#4C4A6C",font=('Doppio One Regular', 12)).place(x=490,y=30)
    txtPeorCasoRadixResul=ScrolledText(VentanaRadixOrdenado, width=23,  height=17,bg="#8080C0")
    txtPeorCasoRadixResul.place(x=430,y=56)

    #Mostramos los arreglos ordenados:(llamamos al modulo que contiene a todos los modulos de ordenacion)

    #Medimos el tiempo Mejor:
    tiempoInicio=0.0
    tiempoFin=0.0
    tiempoInicio=perf_counter()
    RadixSort(MejorRadix,len(MejorRadix))
    tiempoFin=perf_counter()
    tiempoOrdenacion=tiempoFin-tiempoInicio
    ResultadosMejorRadix.delete(0,END)
    ResultadosMejorRadix.insert(END, str(tiempoOrdenacion))

    #Medimos el tiempo Promedio:
    tiempoInicio=0.0
    tiempoFin=0.0
    tiempoInicio=perf_counter()
    RadixSort(PromedioRadix,len(PromedioRadix))
    tiempoFin=perf_counter()
    tiempoOrdenacion=tiempoFin-tiempoInicio
    ResultadosPromedioRadix.delete(0,END)#Para borrar el contenido anterior 
    ResultadosPromedioRadix.insert(END, str(tiempoOrdenacion))

    #Medimos el tiempo Peor:
    tiempoInicio=0.0
    tiempoFin=0.0
    tiempoInicio=perf_counter()
    RadixSort(PeorRadix,len(PeorRadix))
    tiempoFin=perf_counter()
    tiempoOrdenacion=tiempoFin-tiempoInicio
    ResultadosPeorRadix.delete(0,END)#Para borrar el contenido anterior 
    ResultadosPeorRadix.insert(END, str(tiempoOrdenacion))

    #Convertimos a strings los resultados:
    #mostramos las matrices en el form Mejor Caso
    txtMejorCasoRadixResul.delete("1.0","end")#Para borrar el contenido anterior 
    StrMejorRadixSort=", ".join([str(_) for _ in MejorRadix])
    txtMejorCasoRadixResul.insert(END, "[ "+StrMejorRadixSort+" ]")

    #mostramos las matrices en el form Caso Promedio
    txtPromedioCasoRadixResul.delete("1.0","end")#Para borrar el contenido anterior 
    StrPromedioRadixSort=", ".join([str(_) for _ in PromedioRadix])
    txtPromedioCasoRadixResul.insert(END, "[ "+StrPromedioRadixSort+" ]")

    #mostramos las matrices en el form Peor Caso
    txtPeorCasoRadixResul.delete("1.0","end")#Para borrar el contenido anterior 
    StrPeorRadixSort=", ".join([str(_) for _ in PeorRadix])
    txtPeorCasoRadixResul.insert(END, "[ "+StrPeorRadixSort+" ]")


#BTN BUBBLE SORT
def PressBtnBubble():

    #Extraemos la cantidad ingresada:
    longitud=int(tamanioBubble.get())
    #Creamos las matrices Mejor,Peor y caso promedio(Haciendo uso de la libreria GeneradorArreglos)
    MejorBubble,PromedioBubble,PeorBubble=GenArreglosBubbleSort(longitud)
    #Convertimos a string y lo mostramos en el scrolltext:
    #mostramos las matrices en el form Mejor Caso
    txtMejorCasoBubble.delete("1.0","end")#Para borrar el contenido anterior 
    StrMejor=", ".join([str(_) for _ in MejorBubble])
    txtMejorCasoBubble.insert(END, "[ "+StrMejor+" ]")

    #mostramos las matrices en el form Caso Promedio
    txtPromedioCasoBubble.delete("1.0","end")#Para borrar el contenido anterior 
    StrPromedio=", ".join([str(_) for _ in PromedioBubble])
    txtPromedioCasoBubble.insert(END, "[ "+StrPromedio+" ]")

    #mostramos las matrices en el form Peor Caso
    txtPeorCasoBubble.delete("1.0","end")#Para borrar el contenido anterior 
    StrPeor=", ".join([str(_) for _ in PeorBubble])
    txtPeorCasoBubble.insert(END, "[ "+StrPeor+" ]")



    root.geometry("750x425+15+100")
    global VentanaBubbleOrdenado
    VentanaBubbleOrdenado=Toplevel()
    VentanaBubbleOrdenado.title("BubbleSort")
    VentanaBubbleOrdenado.iconbitmap("Logo-UNSAAC.ico")
    VentanaBubbleOrdenado.configure(bg="#4C4A6C")
    #VentanaInsertOrdenado.configure(bg="#9D1321")
    VentanaBubbleOrdenado.geometry("%dx%d+%d+%d" % (640,365,710,150)) #Tamaño y posicion
    Label(VentanaBubbleOrdenado, text="Los Arreglos Ordenados, son:", fg="black",bg="#4C4A6C",font=('Doppio One Regular', 11)).place(x=10,y=10)
    Label(VentanaBubbleOrdenado, text="Mejor Caso", fg="#EEEFF1",bg="#4C4A6C",font=('Doppio One Regular', 12)).place(x=60,y=30)
    txtMejorCasoBubbleResul=ScrolledText(VentanaBubbleOrdenado, width=23,  height=17,bg="#7092BE")
    txtMejorCasoBubbleResul.place(x=10,y=56)
    Label(VentanaBubbleOrdenado, text="Caso Promedio", fg="#EEEFF1",bg="#4C4A6C",font=('Doppio One Regular', 12)).place(x=260,y=30)
    txtPromedioCasoBubbleResul=ScrolledText(VentanaBubbleOrdenado, width=23,  height=17,bg="#EEEFF1")
    txtPromedioCasoBubbleResul.place(x=220,y=56)
    Label(VentanaBubbleOrdenado, text="Peor Caso", fg="#EEEFF1",bg="#4C4A6C",font=('Doppio One Regular', 12)).place(x=490,y=30)
    txtPeorCasoBubbleResul=ScrolledText(VentanaBubbleOrdenado, width=23,  height=17,bg="#8080C0")
    txtPeorCasoBubbleResul.place(x=430,y=56)

    #Mostramos los arreglos ordenados:(llamamos al modulo que contiene a todos los modulos de ordenacion)

    #Medimos el tiempo Mejor:
    tiempoInicio=0.0
    tiempoFin=0.0
    tiempoInicio=perf_counter()
    BubbleSort(MejorBubble,len(MejorBubble))
    tiempoFin=perf_counter()
    tiempoOrdenacion=tiempoFin-tiempoInicio
    ResultadosMejorBubble.delete(0,END)
    ResultadosMejorBubble.insert(END, str(tiempoOrdenacion))

    #Medimos el tiempo Promedio:
    tiempoInicio=0.0
    tiempoFin=0.0
    tiempoInicio=perf_counter()
    BubbleSort(PromedioBubble,len(PromedioBubble))
    tiempoFin=perf_counter()
    tiempoOrdenacion=tiempoFin-tiempoInicio
    ResultadosPromedioBubble.delete(0,END)#Para borrar el contenido anterior 
    ResultadosPromedioBubble.insert(END, str(tiempoOrdenacion))

    #Medimos el tiempo Peor:
    tiempoInicio=0.0
    tiempoFin=0.0
    tiempoInicio=perf_counter()
    BubbleSort(PeorBubble,len(PeorBubble))
    tiempoFin=perf_counter()
    tiempoOrdenacion=tiempoFin-tiempoInicio
    ResultadosPeorBubble.delete(0,END)#Para borrar el contenido anterior 
    ResultadosPeorBubble.insert(END, str(tiempoOrdenacion))

    #Convertimos a strings los resultados:
    #mostramos las matrices en el form Mejor Caso
    txtMejorCasoBubbleResul.delete("1.0","end")#Para borrar el contenido anterior 
    StrMejorBubbleSort=", ".join([str(_) for _ in MejorBubble])
    txtMejorCasoBubbleResul.insert(END, "[ "+StrMejorBubbleSort+" ]")

    #mostramos las matrices en el form Caso Promedio
    txtPromedioCasoBubbleResul.delete("1.0","end")#Para borrar el contenido anterior 
    StrPromedioBubbleSort=", ".join([str(_) for _ in PromedioBubble])
    txtPromedioCasoBubbleResul.insert(END, "[ "+StrPromedioBubbleSort+" ]")

    #mostramos las matrices en el form Peor Caso
    txtPeorCasoBubbleResul.delete("1.0","end")#Para borrar el contenido anterior 
    StrPeorBubbleSort=", ".join([str(_) for _ in PeorBubble])
    txtPeorCasoBubbleResul.insert(END, "[ "+StrPeorBubbleSort+" ]")



#BTN HEAP SORT
def PressBtnHeap():

    #Extraemos la cantidad ingresada:
    longitud=int(tamanioHeap.get())
    #Creamos las matrices Mejor,Peor y caso promedio(Haciendo uso de la libreria GeneradorArreglos)
    MejorHeap,PromedioHeap,PeorHeap=GenArreglosHeapSort(longitud)
    #Convertimos a string y lo mostramos en el scrolltext:
    #mostramos las matrices en el form Mejor Caso
    txtMejorCasoHeap.delete("1.0","end")#Para borrar el contenido anterior 
    StrMejor=", ".join([str(_) for _ in MejorHeap])
    txtMejorCasoHeap.insert(END, "[ "+StrMejor+" ]")

    #mostramos las matrices en el form Caso Promedio
    txtPromedioCasoHeap.delete("1.0","end")#Para borrar el contenido anterior 
    StrPromedio=", ".join([str(_) for _ in PromedioHeap])
    txtPromedioCasoHeap.insert(END, "[ "+StrPromedio+" ]")

    #mostramos las matrices en el form Peor Caso
    txtPeorCasoHeap.delete("1.0","end")#Para borrar el contenido anterior 
    StrPeor=", ".join([str(_) for _ in PeorHeap])
    txtPeorCasoHeap.insert(END, "[ "+StrPeor+" ]")


    root.geometry("750x425+15+100")
    global VentanaHeapOrdenado
    VentanaHeapOrdenado=Toplevel()
    VentanaHeapOrdenado.title("HeapSort")
    VentanaHeapOrdenado.iconbitmap("Logo-UNSAAC.ico")
    VentanaHeapOrdenado.configure(bg="#4C4A6C")
    #VentanaInsertOrdenado.configure(bg="#9D1321")
    VentanaHeapOrdenado.geometry("%dx%d+%d+%d" % (640,365,710,150)) #Tamaño y posicion
    Label(VentanaHeapOrdenado, text="Los Arreglos Ordenados, son:", fg="black",bg="#4C4A6C",font=('Doppio One Regular', 11)).place(x=10,y=10)
    Label(VentanaHeapOrdenado, text="Mejor Caso", fg="#EEEFF1",bg="#4C4A6C",font=('Doppio One Regular', 12)).place(x=60,y=30)
    txtMejorCasoHeapResul=ScrolledText(VentanaHeapOrdenado, width=23,  height=17,bg="#7092BE")
    txtMejorCasoHeapResul.place(x=10,y=56)
    Label(VentanaHeapOrdenado, text="Caso Promedio", fg="#EEEFF1",bg="#4C4A6C",font=('Doppio One Regular', 12)).place(x=260,y=30)
    txtPromedioCasoHeapResul=ScrolledText(VentanaHeapOrdenado, width=23,  height=17,bg="#EEEFF1")
    txtPromedioCasoHeapResul.place(x=220,y=56)
    Label(VentanaHeapOrdenado, text="Peor Caso", fg="#EEEFF1",bg="#4C4A6C",font=('Doppio One Regular', 12)).place(x=490,y=30)
    txtPeorCasoHeapResul=ScrolledText(VentanaHeapOrdenado, width=23,  height=17,bg="#8080C0")
    txtPeorCasoHeapResul.place(x=430,y=56)


    #Mostramos los arreglos ordenados:(llamamos al modulo que contiene a todos los modulos de ordenacion)

    #Medimos el tiempo Mejor:
    tiempoInicio=0.0
    tiempoFin=0.0
    tiempoInicio=perf_counter()
    HeapSort(MejorHeap,len(MejorHeap))
    tiempoFin=perf_counter()
    tiempoOrdenacion=tiempoFin-tiempoInicio
    ResultadosMejorHeap.delete(0,END)
    ResultadosMejorHeap.insert(END, str(tiempoOrdenacion))

    #Medimos el tiempo Promedio:
    tiempoInicio=0.0
    tiempoFin=0.0
    tiempoInicio=perf_counter()
    HeapSort(PromedioHeap,len(PromedioHeap))
    tiempoFin=perf_counter()
    tiempoOrdenacion=tiempoFin-tiempoInicio
    ResultadosPromedioHeap.delete(0,END)#Para borrar el contenido anterior 
    ResultadosPromedioHeap.insert(END, str(tiempoOrdenacion))

    #Medimos el tiempo Peor:
    tiempoInicio=0.0
    tiempoFin=0.0
    tiempoInicio=perf_counter()
    HeapSort(PeorHeap,len(PeorHeap))
    tiempoFin=perf_counter()
    tiempoOrdenacion=tiempoFin-tiempoInicio
    ResultadosPeorHeap.delete(0,END)#Para borrar el contenido anterior 
    ResultadosPeorHeap.insert(END, str(tiempoOrdenacion))

    #Convertimos a strings los resultados:
    #mostramos las matrices en el form Mejor Caso
    txtMejorCasoHeapResul.delete("1.0","end")#Para borrar el contenido anterior 
    StrMejorHeapSort=", ".join([str(_) for _ in MejorHeap])
    txtMejorCasoHeapResul.insert(END, "[ "+StrMejorHeapSort+" ]")

    #mostramos las matrices en el form Caso Promedio
    txtPromedioCasoHeapResul.delete("1.0","end")#Para borrar el contenido anterior 
    StrPromedioHeapSort=", ".join([str(_) for _ in PromedioHeap])
    txtPromedioCasoHeapResul.insert(END, "[ "+StrPromedioHeapSort+" ]")

    #mostramos las matrices en el form Peor Caso
    txtPeorCasoHeapResul.delete("1.0","end")#Para borrar el contenido anterior 
    StrPeorHeapSort=", ".join([str(_) for _ in PeorHeap])
    txtPeorCasoHeapResul.insert(END, "[ "+StrPeorHeapSort+" ]")

#BTN QUICK SORT
def PressBtnQuick():#Maximo tamaño es 990

    #Extraemos la cantidad ingresada:
    longitud=int(tamanioQuick.get())
    #Creamos las matrices Mejor,Peor y caso promedio(Haciendo uso de la libreria GeneradorArreglos)
    MejorQuick,PromedioQuick,PeorQuick=GenArreglosQuickSort(longitud)
    #Convertimos a string y lo mostramos en el scrolltext:
    #mostramos las matrices en el form Mejor Caso
    txtMejorCasoQuick.delete("1.0","end")#Para borrar el contenido anterior 
    StrMejor=", ".join([str(_) for _ in MejorQuick])
    txtMejorCasoQuick.insert(END, "[ "+StrMejor+" ]")

    #mostramos las matrices en el form Caso Promedio
    txtPromedioCasoQuick.delete("1.0","end")#Para borrar el contenido anterior 
    StrPromedio=", ".join([str(_) for _ in PromedioQuick])
    txtPromedioCasoQuick.insert(END, "[ "+StrPromedio+" ]")

    #mostramos las matrices en el form Peor Caso
    txtPeorCasoQuick.delete("1.0","end")#Para borrar el contenido anterior 
    StrPeor=", ".join([str(_) for _ in PeorQuick])
    txtPeorCasoQuick.insert(END, "[ "+StrPeor+" ]")


    root.geometry("750x425+15+100")
    global VentanaQuickOrdenado
    VentanaQuickOrdenado=Toplevel()
    VentanaQuickOrdenado.title("QuickSort")
    VentanaQuickOrdenado.iconbitmap("Logo-UNSAAC.ico")
    VentanaQuickOrdenado.configure(bg="#4C4A6C")
    #VentanaInsertOrdenado.configure(bg="#9D1321")
    VentanaQuickOrdenado.geometry("%dx%d+%d+%d" % (640,365,710,150)) #Tamaño y posicion
    Label(VentanaQuickOrdenado, text="Los Arreglos Ordenados, son:", fg="black",bg="#4C4A6C",font=('Doppio One Regular', 11)).place(x=10,y=10)
    Label(VentanaQuickOrdenado, text="Mejor Caso", fg="#EEEFF1",bg="#4C4A6C",font=('Doppio One Regular', 12)).place(x=60,y=30)
    txtMejorCasoQuickResul=ScrolledText(VentanaQuickOrdenado, width=23,  height=17,bg="#7092BE")
    txtMejorCasoQuickResul.place(x=10,y=56)
    Label(VentanaQuickOrdenado, text="Caso Promedio", fg="#EEEFF1",bg="#4C4A6C",font=('Doppio One Regular', 12)).place(x=260,y=30)
    txtPromedioCasoQuickResul=ScrolledText(VentanaQuickOrdenado, width=23,  height=17,bg="#EEEFF1")
    txtPromedioCasoQuickResul.place(x=220,y=56)
    Label(VentanaQuickOrdenado, text="Peor Caso", fg="#EEEFF1",bg="#4C4A6C",font=('Doppio One Regular', 12)).place(x=490,y=30)
    txtPeorCasoQuickResul=ScrolledText(VentanaQuickOrdenado, width=23,  height=17,bg="#8080C0")
    txtPeorCasoQuickResul.place(x=430,y=56)

    #Mostramos los arreglos ordenados:(llamamos al modulo que contiene a todos los modulos de ordenacion)

    #Medimos el tiempo Mejor:
    tiempoInicio=0.0
    tiempoFin=0.0
    tiempoInicio=perf_counter()
    QuickSort(MejorQuick,0,len(MejorQuick)-1)
    tiempoFin=perf_counter()
    tiempoOrdenacion=tiempoFin-tiempoInicio
    ResultadosMejorQuick.delete(0,END)
    ResultadosMejorQuick.insert(END, str(tiempoOrdenacion))

    #Medimos el tiempo Promedio:
    tiempoInicio=0.0
    tiempoFin=0.0
    tiempoInicio=perf_counter()
    QuickSort(PromedioQuick,0,len(PromedioQuick)-1)
    tiempoFin=perf_counter()
    tiempoOrdenacion=tiempoFin-tiempoInicio
    ResultadosPromedioQuick.delete(0,END)#Para borrar el contenido anterior 
    ResultadosPromedioQuick.insert(END, str(tiempoOrdenacion))

    #Medimos el tiempo Peor:
    tiempoInicio=0.0
    tiempoFin=0.0
    tiempoInicio=perf_counter()
    QuickSort(PeorQuick,0,len(PeorQuick)-1)
    tiempoFin=perf_counter()
    tiempoOrdenacion=tiempoFin-tiempoInicio
    ResultadosPeorQuick.delete(0,END)#Para borrar el contenido anterior 
    ResultadosPeorQuick.insert(END, str(tiempoOrdenacion))


    #Convertimos a strings los resultados:
    #mostramos las matrices en el form Mejor Caso
    txtMejorCasoQuickResul.delete("1.0","end")#Para borrar el contenido anterior 
    StrMejorQuickSort=", ".join([str(_) for _ in MejorQuick])
    txtMejorCasoQuickResul.insert(END, "[ "+StrMejorQuickSort+" ]")

    #mostramos las matrices en el form Caso Promedio
    txtPromedioCasoQuickResul.delete("1.0","end")#Para borrar el contenido anterior 
    StrPromedioQuickSort=", ".join([str(_) for _ in PromedioQuick])
    txtPromedioCasoQuickResul.insert(END, "[ "+StrPromedioQuickSort+" ]")

    #mostramos las matrices en el form Peor Caso
    txtPeorCasoQuickResul.delete("1.0","end")#Para borrar el contenido anterior 
    StrPeorQuickSort=", ".join([str(_) for _ in PeorQuick])
    txtPeorCasoQuickResul.insert(END, "[ "+StrPeorQuickSort+" ]")

#BTN BUCKET SORT
def PressBtnBucket():

    #Extraemos la cantidad ingresada:
    longitud=int(tamanioBucket.get())
    #Creamos las matrices Mejor,Peor y caso promedio(Haciendo uso de la libreria GeneradorArreglos)
    MejorBucket,PromedioBucket,PeorBucket=GenArreglosBucketSort(longitud)
    #Convertimos a string y lo mostramos en el scrolltext:
    #mostramos las matrices en el form Mejor Caso
    txtMejorCasoBucket.delete("1.0","end")#Para borrar el contenido anterior 
    StrMejor=", ".join([str(_) for _ in MejorBucket])
    txtMejorCasoBucket.insert(END, "[ "+StrMejor+" ]")

    #mostramos las matrices en el form Caso Promedio
    txtPromedioCasoBucket.delete("1.0","end")#Para borrar el contenido anterior 
    StrPromedio=", ".join([str(_) for _ in PromedioBucket])
    txtPromedioCasoBucket.insert(END, "[ "+StrPromedio+" ]")

    #mostramos las matrices en el form Peor Caso
    txtPeorCasoBucket.delete("1.0","end")#Para borrar el contenido anterior 
    StrPeor=", ".join([str(_) for _ in PeorBucket])
    txtPeorCasoBucket.insert(END, "[ "+StrPeor+" ]")

    root.geometry("750x425+15+100")
    global VentanaBucketOrdenado
    VentanaBucketOrdenado=Toplevel()
    VentanaBucketOrdenado.title("BucketSort")
    VentanaBucketOrdenado.iconbitmap("Logo-UNSAAC.ico")
    VentanaBucketOrdenado.configure(bg="#4C4A6C")
    #VentanaInsertOrdenado.configure(bg="#9D1321")
    VentanaBucketOrdenado.geometry("%dx%d+%d+%d" % (640,365,710,150)) #Tamaño y posicion
    Label(VentanaBucketOrdenado, text="Los Arreglos Ordenados, son:", fg="black",bg="#4C4A6C",font=('Doppio One Regular', 11)).place(x=10,y=10)
    Label(VentanaBucketOrdenado, text="Mejor Caso", fg="#EEEFF1",bg="#4C4A6C",font=('Doppio One Regular', 12)).place(x=60,y=30)
    txtMejorCasoBucketResul=ScrolledText(VentanaBucketOrdenado, width=23,  height=17,bg="#7092BE")
    txtMejorCasoBucketResul.place(x=10,y=56)
    Label(VentanaBucketOrdenado, text="Caso Promedio", fg="#EEEFF1",bg="#4C4A6C",font=('Doppio One Regular', 12)).place(x=260,y=30)
    txtPromedioCasoBucketResul=ScrolledText(VentanaBucketOrdenado, width=23,  height=17,bg="#EEEFF1")
    txtPromedioCasoBucketResul.place(x=220,y=56)
    Label(VentanaBucketOrdenado, text="Peor Caso", fg="#EEEFF1",bg="#4C4A6C",font=('Doppio One Regular', 12)).place(x=490,y=30)
    txtPeorCasoBucketResul=ScrolledText(VentanaBucketOrdenado, width=23,  height=17,bg="#8080C0")
    txtPeorCasoBucketResul.place(x=430,y=56)


    #Mostramos los arreglos ordenados:(llamamos al modulo que contiene a todos los modulos de ordenacion)

    #Medimos el tiempo Mejor:
    tiempoInicio=0.0
    tiempoFin=0.0
    tiempoInicio=perf_counter()
    BucketSort(MejorBucket,len(MejorBucket))
    tiempoFin=perf_counter()
    tiempoOrdenacion=tiempoFin-tiempoInicio
    ResultadosMejorBucket.delete(0,END)
    ResultadosMejorBucket.insert(END, str(tiempoOrdenacion))

    #Medimos el tiempo Promedio:
    tiempoInicio=0.0
    tiempoFin=0.0
    tiempoInicio=perf_counter()
    BucketSort(PromedioBucket,len(PromedioBucket))
    tiempoFin=perf_counter()
    tiempoOrdenacion=tiempoFin-tiempoInicio
    ResultadosPromedioBucket.delete(0,END)#Para borrar el contenido anterior 
    ResultadosPromedioBucket.insert(END, str(tiempoOrdenacion))

    #Medimos el tiempo Peor:
    tiempoInicio=0.0
    tiempoFin=0.0
    tiempoInicio=perf_counter()
    BucketSort(PeorBucket,len(PeorBucket))
    tiempoFin=perf_counter()
    tiempoOrdenacion=tiempoFin-tiempoInicio
    ResultadosPeorBucket.delete(0,END)#Para borrar el contenido anterior 
    ResultadosPeorBucket.insert(END, str(tiempoOrdenacion))


    #Convertimos a strings los resultados:
    #mostramos las matrices en el form Mejor Caso
    txtMejorCasoBucketResul.delete("1.0","end")#Para borrar el contenido anterior 
    StrMejorBucketSort=", ".join([str(_) for _ in MejorBucket])
    txtMejorCasoBucketResul.insert(END, "[ "+StrMejorBucketSort+" ]")

    #mostramos las matrices en el form Caso Promedio
    txtPromedioCasoBucketResul.delete("1.0","end")#Para borrar el contenido anterior 
    StrPromedioBucketSort=", ".join([str(_) for _ in PromedioBucket])
    txtPromedioCasoBucketResul.insert(END, "[ "+StrPromedioBucketSort+" ]")

    #mostramos las matrices en el form Peor Caso
    txtPeorCasoBucketResul.delete("1.0","end")#Para borrar el contenido anterior 
    StrPeorBucketSort=", ".join([str(_) for _ in PeorBucket])
    txtPeorCasoBucketResul.insert(END, "[ "+StrPeorBucketSort+" ]")

#BTN SELECTION SORT
def PressBtnSelection():

    #Extraemos la cantidad ingresada:
    longitud=int(tamanioSelection.get())
    #Creamos las matrices Mejor,Peor y caso promedio(Haciendo uso de la libreria GeneradorArreglos)
    MejorSelection,PromedioSelection,PeorSelection=GenArreglosSelectionSort(longitud)
    #Convertimos a string y lo mostramos en el scrolltext:
    #mostramos las matrices en el form Mejor Caso
    txtMejorCasoSelection.delete("1.0","end")#Para borrar el contenido anterior 
    StrMejor=", ".join([str(_) for _ in MejorSelection])
    txtMejorCasoSelection.insert(END, "[ "+StrMejor+" ]")

    #mostramos las matrices en el form Caso Promedio
    txtPromedioCasoSelection.delete("1.0","end")#Para borrar el contenido anterior 
    StrPromedio=", ".join([str(_) for _ in PromedioSelection])
    txtPromedioCasoSelection.insert(END, "[ "+StrPromedio+" ]")

    #mostramos las matrices en el form Peor Caso
    txtPeorCasoSelection.delete("1.0","end")#Para borrar el contenido anterior 
    StrPeor=", ".join([str(_) for _ in PeorSelection])
    txtPeorCasoSelection.insert(END, "[ "+StrPeor+" ]")


    root.geometry("750x425+15+100")
    global VentanaSelectionOrdenado
    VentanaSelectionOrdenado=Toplevel()
    VentanaSelectionOrdenado.title("SelectionSort")
    VentanaSelectionOrdenado.iconbitmap("Logo-UNSAAC.ico")
    VentanaSelectionOrdenado.configure(bg="#4C4A6C")
    #VentanaInsertOrdenado.configure(bg="#9D1321")
    VentanaSelectionOrdenado.geometry("%dx%d+%d+%d" % (640,365,710,150)) #Tamaño y posicion
    Label(VentanaSelectionOrdenado, text="Los Arreglos Ordenados, son:", fg="black",bg="#4C4A6C",font=('Doppio One Regular', 11)).place(x=10,y=10)
    Label(VentanaSelectionOrdenado, text="Mejor Caso", fg="#EEEFF1",bg="#4C4A6C",font=('Doppio One Regular', 12)).place(x=60,y=30)
    txtMejorCasoSelectionResul=ScrolledText(VentanaSelectionOrdenado, width=23,  height=17,bg="#7092BE")
    txtMejorCasoSelectionResul.place(x=10,y=56)
    Label(VentanaSelectionOrdenado, text="Caso Promedio", fg="#EEEFF1",bg="#4C4A6C",font=('Doppio One Regular', 12)).place(x=260,y=30)
    txtPromedioCasoSelectionResul=ScrolledText(VentanaSelectionOrdenado, width=23,  height=17,bg="#EEEFF1")
    txtPromedioCasoSelectionResul.place(x=220,y=56)
    Label(VentanaSelectionOrdenado, text="Peor Caso", fg="#EEEFF1",bg="#4C4A6C",font=('Doppio One Regular', 12)).place(x=490,y=30)
    txtPeorCasoSelectionResul=ScrolledText(VentanaSelectionOrdenado, width=23,  height=17,bg="#8080C0")
    txtPeorCasoSelectionResul.place(x=430,y=56)

    #Mostramos los arreglos ordenados:(llamamos al modulo que contiene a todos los modulos de ordenacion)

    #Medimos el tiempo Mejor:
    tiempoInicio=0.0
    tiempoFin=0.0
    tiempoInicio=perf_counter()
    SelectionSort(MejorSelection,len(MejorSelection))
    tiempoFin=perf_counter()
    tiempoOrdenacion=tiempoFin-tiempoInicio
    ResultadosMejorSelection.delete(0,END)
    ResultadosMejorSelection.insert(END, str(tiempoOrdenacion))

    #Medimos el tiempo Promedio:
    tiempoInicio=0.0
    tiempoFin=0.0
    tiempoInicio=perf_counter()
    SelectionSort(PromedioSelection,len(PromedioSelection))
    tiempoFin=perf_counter()
    tiempoOrdenacion=tiempoFin-tiempoInicio
    ResultadosPromedioSelection.delete(0,END)#Para borrar el contenido anterior 
    ResultadosPromedioSelection.insert(END, str(tiempoOrdenacion))

    #Medimos el tiempo Peor:
    tiempoInicio=0.0
    tiempoFin=0.0
    tiempoInicio=perf_counter()
    SelectionSort(PeorSelection,len(PeorSelection))
    tiempoFin=perf_counter()
    tiempoOrdenacion=tiempoFin-tiempoInicio
    ResultadosPeorSelection.delete(0,END)#Para borrar el contenido anterior 
    ResultadosPeorSelection.insert(END, str(tiempoOrdenacion))

    
    #Convertimos a strings los resultados:
    #mostramos las matrices en el form Mejor Caso
    txtMejorCasoSelectionResul.delete("1.0","end")#Para borrar el contenido anterior 
    StrMejorSelectionSort=", ".join([str(_) for _ in MejorSelection])
    txtMejorCasoSelectionResul.insert(END, "[ "+StrMejorSelectionSort+" ]")

    #mostramos las matrices en el form Caso Promedio
    txtPromedioCasoSelectionResul.delete("1.0","end")#Para borrar el contenido anterior 
    StrPromedioSelectionSort=", ".join([str(_) for _ in PromedioSelection])
    txtPromedioCasoSelectionResul.insert(END, "[ "+StrPromedioSelectionSort+" ]")

    #mostramos las matrices en el form Peor Caso
    txtPeorCasoSelectionResul.delete("1.0","end")#Para borrar el contenido anterior 
    StrPeorSelectionSort=", ".join([str(_) for _ in PeorSelection])
    txtPeorCasoSelectionResul.insert(END, "[ "+StrPeorSelectionSort+" ]")


#BTN COMB SORT
def PressBtnComb():

    #Extraemos la cantidad ingresada:
    longitud=int(tamanioComb.get())
    #Creamos las matrices Mejor,Peor y caso promedio(Haciendo uso de la libreria GeneradorArreglos)
    MejorComb,PromedioComb,PeorComb=GenArreglosCombSort(longitud)
    #Convertimos a string y lo mostramos en el scrolltext:
    #mostramos las matrices en el form Mejor Caso
    txtMejorCasoComb.delete("1.0","end")#Para borrar el contenido anterior 
    StrMejor=", ".join([str(_) for _ in MejorComb])
    txtMejorCasoComb.insert(END, "[ "+StrMejor+" ]")

    #mostramos las matrices en el form Caso Promedio
    txtPromedioCasoComb.delete("1.0","end")#Para borrar el contenido anterior 
    StrPromedio=", ".join([str(_) for _ in PromedioComb])
    txtPromedioCasoComb.insert(END, "[ "+StrPromedio+" ]")

    #mostramos las matrices en el form Peor Caso
    txtPeorCasoComb.delete("1.0","end")#Para borrar el contenido anterior 
    StrPeor=", ".join([str(_) for _ in PeorComb])
    txtPeorCasoComb.insert(END, "[ "+StrPeor+" ]")


    root.geometry("750x425+15+100")
    global VentanaCombOrdenado
    VentanaCombOrdenado=Toplevel()
    VentanaCombOrdenado.title("CombSort")
    VentanaCombOrdenado.iconbitmap("Logo-UNSAAC.ico")
    VentanaCombOrdenado.configure(bg="#4C4A6C")
    #VentanaInsertOrdenado.configure(bg="#9D1321")
    VentanaCombOrdenado.geometry("%dx%d+%d+%d" % (640,365,710,150)) #Tamaño y posicion
    Label(VentanaCombOrdenado, text="Los Arreglos Ordenados, son:", fg="black",bg="#4C4A6C",font=('Doppio One Regular', 11)).place(x=10,y=10)
    Label(VentanaCombOrdenado, text="Mejor Caso", fg="#EEEFF1",bg="#4C4A6C",font=('Doppio One Regular', 12)).place(x=60,y=30)
    txtMejorCasoCombResul=ScrolledText(VentanaCombOrdenado, width=23,  height=17,bg="#7092BE")
    txtMejorCasoCombResul.place(x=10,y=56)
    Label(VentanaCombOrdenado, text="Caso Promedio", fg="#EEEFF1",bg="#4C4A6C",font=('Doppio One Regular', 12)).place(x=260,y=30)
    txtPromedioCasoCombResul=ScrolledText(VentanaCombOrdenado, width=23,  height=17,bg="#EEEFF1")
    txtPromedioCasoCombResul.place(x=220,y=56)
    Label(VentanaCombOrdenado, text="Peor Caso", fg="#EEEFF1",bg="#4C4A6C",font=('Doppio One Regular', 12)).place(x=490,y=30)
    txtPeorCasoCombResul=ScrolledText(VentanaCombOrdenado, width=23,  height=17,bg="#8080C0")
    txtPeorCasoCombResul.place(x=430,y=56)

    #Mostramos los arreglos ordenados:(llamamos al modulo que contiene a todos los modulos de ordenacion)

    #Medimos el tiempo Mejor:
    tiempoInicio=0.0
    tiempoFin=0.0
    tiempoInicio=perf_counter()
    CombSort(MejorComb)
    tiempoFin=perf_counter()
    tiempoOrdenacion=tiempoFin-tiempoInicio
    ResultadosMejorComb.delete(0,END)
    ResultadosMejorComb.insert(END, str(tiempoOrdenacion))

    #Medimos el tiempo Promedio:
    tiempoInicio=0.0
    tiempoFin=0.0
    tiempoInicio=perf_counter()
    CombSort(PromedioComb)
    tiempoFin=perf_counter()
    tiempoOrdenacion=tiempoFin-tiempoInicio
    ResultadosPromedioComb.delete(0,END)#Para borrar el contenido anterior 
    ResultadosPromedioComb.insert(END, str(tiempoOrdenacion))

    #Medimos el tiempo Peor:
    tiempoInicio=0.0
    tiempoFin=0.0
    tiempoInicio=perf_counter()
    CombSort(PeorComb)
    tiempoFin=perf_counter()
    tiempoOrdenacion=tiempoFin-tiempoInicio
    ResultadosPeorComb.delete(0,END)#Para borrar el contenido anterior 
    ResultadosPeorComb.insert(END, str(tiempoOrdenacion))


    #Convertimos a strings los resultados:
    #mostramos las matrices en el form Mejor Caso
    txtMejorCasoCombResul.delete("1.0","end")#Para borrar el contenido anterior 
    StrMejorCombSort=", ".join([str(_) for _ in MejorComb])
    txtMejorCasoCombResul.insert(END, "[ "+StrMejorCombSort+" ]")

    #mostramos las matrices en el form Caso Promedio
    txtPromedioCasoCombResul.delete("1.0","end")#Para borrar el contenido anterior 
    StrPromedioCombSort=", ".join([str(_) for _ in PromedioComb])
    txtPromedioCasoCombResul.insert(END, "[ "+StrPromedioCombSort+" ]")

    #mostramos las matrices en el form Peor Caso
    txtPeorCasoCombResul.delete("1.0","end")#Para borrar el contenido anterior 
    StrPeorCombSort=", ".join([str(_) for _ in PeorComb])
    txtPeorCasoCombResul.insert(END, "[ "+StrPeorCombSort+" ]")



#============================================================================================================================================

#Ventana Principal
#Creamos la ventana inicial
root=Tk()

#Empieza el bucle
root.geometry("750x425+340+100")#(tamaño) y (posicion) Posicion Anterior="725x400+340+100"
root.title("Metodos De Ordenacion")
root.iconbitmap("Logo-UNSAAC.ico")
#root.config(bg="#9D1321")#"#9D1321")
root.resizable(0,0)
#Definimos el menu:
barraMenu=Menu(root)


#Creamos las opciones del menu
mnuMetodos=Menu(barraMenu,background='#FFD767',tearoff=0)
#Asignar nombres a las opcioones del menu
mnuMetodos.add_command(label="Insertion Sort", command=VentanaInsertSort)
mnuMetodos.add_command(label="Merge Sort",command=VentanaMergeSort)
mnuMetodos.add_command(label="Shell Sort",command=VentanaShellSort)
mnuMetodos.add_command(label="Radix Sort",command=VentanaRadixSort)
mnuMetodos.add_command(label="Bubble Sort",command=VentanaBubbleSort)
mnuMetodos.add_command(label="Heap Sort",command=VentanaHeapSort)
mnuMetodos.add_command(label="Quick Sort",command=VentanaQuickSort)
mnuMetodos.add_command(label="Bucket Sort",command=VentanaBucketSort)
mnuMetodos.add_command(label="Selection Sort",command=VentanaSelectionSort)
mnuMetodos.add_command(label="Comb Sort",command=VentanaCombSort)
mnuMetodos.add_separator()
mnuMetodos.add_command(label="      Salir",command=VentanaSalir)

#Agregamos las opciones al menu de barras
barraMenu.add_cascade(label="AlgoritmosOrdenacion", menu=mnuMetodos)
#Plasmamos el menu en la pantalla principal
#root.config(menu=barraMenu)


#Creamos las opciones del menu
mnuOrdenar=Menu(barraMenu,background='#3AC8B6',tearoff=0)
#Asignar nombres a las opcioones del menu
#mnuOrdenar.add_command(label="Ordenar Arreglos")
#mnuOrdenar.add_command(label="Arreglo Aleatorio")
mnuOrdenar.add_command(label="Arreglo Definido",command=VentanaArregloDefinido)
#Agregamos las opciones al menu de barras
barraMenu.add_cascade(label="Ordenar", menu=mnuOrdenar)
#Plasmamos el menu en la pantalla principal
root.config(menu=barraMenu)


#===================== Creamos variables iniciales =================
#VentanaInsertOrdenado
VentanaInsertOrdenado=Toplevel()
VentanaInsertOrdenado.destroy()
VentanaBucketOrdenado=Toplevel()
VentanaBucketOrdenado.destroy()
VentanaMergeOrdenado=Toplevel()
VentanaMergeOrdenado.destroy()
VentanaBubbleOrdenado=Toplevel()
VentanaBubbleOrdenado.destroy()
VentanaCombOrdenado=Toplevel()
VentanaCombOrdenado.destroy()
VentanaQuickOrdenado=Toplevel()
VentanaQuickOrdenado.destroy()
VentanaHeapOrdenado=Toplevel()
VentanaHeapOrdenado.destroy()
VentanaRadixOrdenado=Toplevel()
VentanaRadixOrdenado.destroy()
VentanaSelectionOrdenado=Toplevel()
VentanaSelectionOrdenado.destroy()
VentanaShellOrdenado=Toplevel()
VentanaShellOrdenado.destroy()

#============== Creamos los lienzos de pantallas ===============================
#1.- Lienzo Caratula
lienzoCaratula=Frame(root,width=750,height=425)#Era 725, 400
lienzoCaratula.pack()

#LogoUnsaac=PhotoImage(file="Logo UNSAAC.png")
LogoUnsaac=PhotoImage(file="logo Informatica2.png")
#fondo=Label(lienzoCaratula,image=LogoUnsaac,bg="#9D1321").place(x=0,y=30)
fondo=Label(lienzoCaratula,image=LogoUnsaac).place(x=-2,y=0)
#Titulo De Aplicacion
#TemaGeneral=Label(lienzoCaratula,text="Metodos de\n Ordenacion", fg="#FFD767",bg="#9D1321",font=('Calibri', 46, 'bold')).place(x=300,y=130)

#2.- Lienzo vnt IsertSort
tamanioInsert=StringVar()
LogoInsert=PhotoImage(file="VentanaInsertSort2.png")
lienzoInsertSort=Frame(lienzoCaratula,width=750,height=425)#Era red, 720x300
Label(lienzoInsertSort,image=LogoInsert).place(x=-2,y=0)#Lo insertaremos cuando se crea.
#TemaInsertSort=Label(lienzoInsertSort,text="INSERT SORT (Mejor,peor y caso Promedio)", fg="#FFD767",bg="#9D1321",font=('Calibri', 16)).place(x=100,y=10)#bold
#lbInsertSort=Label(lienzoInsertSort,text="Ingrese un tamaño para\n crear los arreglos:", fg="#C3C3C3",bg="#9D1321",font=('Calibri', 16)).place(x=10,y=50)
entradaInsert=Entry(lienzoInsertSort,bg="#FFF",font=('consolas', 13),highlightbackground="gray",bd=5,textvariable=tamanioInsert).place(x=343,y=55)
btnInsertSort=Button(lienzoInsertSort,text="Generar",font=('Calibri', 13),bg="#C3C3C3",highlightbackground="black",command=PressBtnInsert).place(x=600,y=55)


#Creamos un lienzo donde se mostrara los resultados de las matrices
txtMejorCasoInsert=ScrolledText(lienzoInsertSort, width=24,  height=14,bg="#C3C3C3")
txtMejorCasoInsert.place(x=41,y=116)
txtPromedioCasoInsert=ScrolledText(lienzoInsertSort, width=23,  height=14,bg="#C3C3C3")
txtPromedioCasoInsert.place(x=289,y=116)
txtPeorCasoInsert=ScrolledText(lienzoInsertSort, width=23,  height=14,bg="#C3C3C3")
txtPeorCasoInsert.place(x=522,y=116)

#lblMejorCasoInsert=Label(lienzoInsertSort,text="Mejor Caso", fg="#C3C3C3",bg="#9D1321",font=('Calibri', 16)).place(x=53,y=130)
#lblPromedioCasoInsert=Label(lienzoInsertSort,text="Caso Promedio", fg="#C3C3C3",bg="#9D1321",font=('Calibri', 16)).place(x=280,y=130)
#lblPeorCasoInsert=Label(lienzoInsertSort,text="Peor Caso", fg="#C3C3C3",bg="#9D1321",font=('Calibri', 16)).place(x=520,y=130)


ResultadosMejorInsert=Entry(lienzoInsertSort,bg="#EEEFF1",font=('consolas', 12),bd=0,width=22)#,textvariable=resulInsertM)#bd=5 #,width=23
ResultadosMejorInsert.place(x=48,y=389)

ResultadosPromedioInsert=Entry(lienzoInsertSort,bg="#EEEFF1",font=('consolas', 12),bd=0,width=22)#,textvariable=resulInsertP)
ResultadosPromedioInsert.place(x=294,y=389)

ResultadosPeorInsert=Entry(lienzoInsertSort,bg="#EEEFF1",font=('consolas', 12),bd=0,width=22)#,textvariable=resulInsertPeor)
ResultadosPeorInsert.place(x=526,y=389)
#Paraa ejecutar con la tecla enter
#root.bind('<Return>',lambda event:PressBtnInsert())

#txtMejorCasoInsert=ScrolledText(lienzoInsertSort, width=16,  height=5).place(x=0,y=30)

#((((((((((((((((((((((((((((((((((((((((((((Ventana Merge Sort))))))))))))))))))))))))))))))))))))))))))))
#3.- Lienzo MergeSort
tamanioMerge=StringVar()
LogoMerge=PhotoImage(file="VentanaMergeSort2.png")
lienzoMergeSort=Frame(lienzoCaratula,width=750,height=425)#era 720 x 300
Label(lienzoMergeSort,image=LogoMerge).place(x=-2,y=0)
#txtMejorCasoMerge=ScrolledText(lienzoMergeSort, width=16,  height=5).place(x=0,y=30)
#TemaMergeSort=Label(lienzoMergeSort,text="MERGE SORT (Mejor,peor y caso Promedio)", fg="#FFD767",bg="#9D1321",font=('Calibri', 16)).place(x=100,y=10)#bold
#lbMergeSort=Label(lienzoMergeSort,text="Ingrese un tamaño para\n crear los arreglos:", fg="#C3C3C3",bg="#9D1321",font=('Calibri', 16)).place(x=10,y=50)
entradaMerge=Entry(lienzoMergeSort,bg="#FFF",font=('consolas', 13),highlightbackground="gray",bd=5,textvariable=tamanioMerge)
entradaMerge.place(x=343,y=55)
btnMergeSort=Button(lienzoMergeSort,text="Generar",font=('Calibri', 13),bg="#C3C3C3",highlightbackground="black",command=PressBtnMerge).place(x=600,y=55)

#Creamos un lienzo donde se mostrara los resultados de las matrices
txtMejorCasoMerge=ScrolledText(lienzoMergeSort, width=24,  height=14,bg="#C3C3C3")
txtMejorCasoMerge.place(x=41,y=116)
txtPromedioCasoMerge=ScrolledText(lienzoMergeSort, width=23,  height=14,bg="#C3C3C3")
txtPromedioCasoMerge.place(x=289,y=116)
txtPeorCasoMerge=ScrolledText(lienzoMergeSort, width=23,  height=14,bg="#C3C3C3")
txtPeorCasoMerge.place(x=522,y=116)

#lblMejorCasoMerge=Label(lienzoMergeSort,text="Mejor Caso", fg="#C3C3C3",bg="#9D1321",font=('Calibri', 16)).place(x=53,y=130)
#lblPromedioCasoMerge=Label(lienzoMergeSort,text="Caso Promedio", fg="#C3C3C3",bg="#9D1321",font=('Calibri', 16)).place(x=280,y=130)
#lblPeorCasoMerge=Label(lienzoMergeSort,text="Peor Caso", fg="#C3C3C3",bg="#9D1321",font=('Calibri', 16)).place(x=520,y=130)

ResultadosMejorMerge=Entry(lienzoMergeSort,bg="#C3A88B",font=('consolas', 12),bd=0,width=22)
ResultadosMejorMerge.place(x=48,y=389)
ResultadosPromedioMerge=Entry(lienzoMergeSort,bg="#C3A88B",font=('consolas', 12),bd=0,width=22)
ResultadosPromedioMerge.place(x=294,y=389)
ResultadosPeorMerge=Entry(lienzoMergeSort,bg="#C3A88B",font=('consolas', 12),bd=0,width=22)
ResultadosPeorMerge.place(x=526,y=389)



#((((((((((((((((((((((((((((((((((((((((((((Ventana Shell Sort))))))))))))))))))))))))))))))))))))))))))))
#4.- Lienzo Shell Sort
tamanioShell=StringVar()
LogoShell=PhotoImage(file="VentanaShellSort2.png")
lienzoShellSort=Frame(lienzoCaratula,width=750,height=425)
Label(lienzoShellSort,image=LogoShell).place(x=-2,y=0)

#TemaShellSort=Label(lienzoShellSort,text="SHELL SORT (Mejor,peor y caso Promedio)", fg="#FFD767",bg="#9D1321",font=('Calibri', 16)).place(x=100,y=10)#bold
#lbShellSort=Label(lienzoShellSort,text="Ingrese un tamaño para\n crear los arreglos:", fg="#C3C3C3",bg="#9D1321",font=('Calibri', 16)).place(x=10,y=50)
entradaShell=Entry(lienzoShellSort,bg="#FFF",font=('consolas', 13),highlightbackground="gray",bd=5,textvariable=tamanioShell)
entradaShell.place(x=343,y=55)
btnShellSort=Button(lienzoShellSort,text="Generar",font=('Calibri', 13),bg="#C3C3C3",highlightbackground="black",command=PressBtnShell).place(x=600,y=55)

#Creamos un lienzo donde se mostrara los resultados de las matrices
txtMejorCasoShell=ScrolledText(lienzoShellSort, width=24,  height=14,bg="#C3C3C3")
txtMejorCasoShell.place(x=41,y=116)
txtPromedioCasoShell=ScrolledText(lienzoShellSort, width=23,  height=14,bg="#C3C3C3")
txtPromedioCasoShell.place(x=289,y=116)
txtPeorCasoShell=ScrolledText(lienzoShellSort, width=23,  height=14,bg="#C3C3C3")
txtPeorCasoShell.place(x=522,y=116)

#lblMejorCasoShell=Label(lienzoShellSort,text="Mejor Caso", fg="#C3C3C3",bg="#9D1321",font=('Calibri', 16)).place(x=53,y=130)
#lblPromedioCasoShell=Label(lienzoShellSort,text="Caso Promedio", fg="#C3C3C3",bg="#9D1321",font=('Calibri', 16)).place(x=280,y=130)
#lblPeorCasoShell=Label(lienzoShellSort,text="Peor Caso", fg="#C3C3C3",bg="#9D1321",font=('Calibri', 16)).place(x=520,y=130)

ResultadosMejorShell=Entry(lienzoShellSort,bg="#C3A88B",font=('consolas', 12),bd=0,width=22)
ResultadosMejorShell.place(x=48,y=389)
ResultadosPromedioShell=Entry(lienzoShellSort,bg="#C3A88B",font=('consolas', 12),bd=0,width=22)
ResultadosPromedioShell.place(x=294,y=389)
ResultadosPeorShell=Entry(lienzoShellSort,bg="#C3A88B",font=('consolas', 12),bd=0,width=22)
ResultadosPeorShell.place(x=526,y=389)



#((((((((((((((((((((((((((((((((((((((((((((Ventana Radix Sort))))))))))))))))))))))))))))))))))))))))))))
#5.- Lienzo Radix Sort
tamanioRadix=StringVar()
LogoRadix=PhotoImage(file="VentanaRadixSort2.png")
lienzoRadixSort=Frame(lienzoCaratula,width=750,height=425)
Label(lienzoRadixSort,image=LogoRadix).place(x=-2,y=0)

#TemaRadixSort=Label(lienzoRadixSort,text="RADIX SORT (Mejor,peor y caso Promedio)", fg="#FFD767",bg="#9D1321",font=('Calibri', 16)).place(x=100,y=10)#bold
#lbRadixSort=Label(lienzoRadixSort,text="Ingrese un tamaño para\n crear los arreglos:", fg="#C3C3C3",bg="#9D1321",font=('Calibri', 16)).place(x=10,y=50)
entradaRadix=Entry(lienzoRadixSort,bg="#FFF",font=('consolas', 13),highlightbackground="gray",bd=5,textvariable=tamanioRadix).place(x=343,y=55)
btnRadixSort=Button(lienzoRadixSort,text="Generar",font=('Calibri', 13),bg="#C3C3C3",highlightbackground="black",command=PressBtnRadix).place(x=600,y=55)

#Creamos un lienzo donde se mostrara los resultados de las matrices
txtMejorCasoRadix=ScrolledText(lienzoRadixSort, width=24,  height=14,bg="#C3C3C3")
txtMejorCasoRadix.place(x=41,y=116)
txtPromedioCasoRadix=ScrolledText(lienzoRadixSort, width=23,  height=14,bg="#C3C3C3")
txtPromedioCasoRadix.place(x=289,y=116)
txtPeorCasoRadix=ScrolledText(lienzoRadixSort, width=23,  height=14,bg="#C3C3C3")
txtPeorCasoRadix.place(x=522,y=116)

#lblMejorCasoRadix=Label(lienzoRadixSort,text="Mejor Caso", fg="#C3C3C3",bg="#9D1321",font=('Calibri', 16)).place(x=53,y=130)
#lblPromedioCasoRadix=Label(lienzoRadixSort,text="Caso Promedio", fg="#C3C3C3",bg="#9D1321",font=('Calibri', 16)).place(x=280,y=130)
#lblPeorCasoRadix=Label(lienzoRadixSort,text="Peor Caso", fg="#C3C3C3",bg="#9D1321",font=('Calibri', 16)).place(x=520,y=130)

ResultadosMejorRadix=Entry(lienzoRadixSort,bg="#C3A88B",font=('consolas', 12),bd=0,width=22)
ResultadosMejorRadix.place(x=48,y=389)
ResultadosPromedioRadix=Entry(lienzoRadixSort,bg="#C3A88B",font=('consolas', 12),bd=0,width=22)
ResultadosPromedioRadix.place(x=294,y=389)
ResultadosPeorRadix=Entry(lienzoRadixSort,bg="#C3A88B",font=('consolas', 12),bd=0,width=22)
ResultadosPeorRadix.place(x=526,y=389)


#((((((((((((((((((((((((((((((((((((((((((((Ventana Bubble Sort))))))))))))))))))))))))))))))))))))))))))))
#6.- Lienzo Bubble Sort
tamanioBubble=StringVar()
LogoBubble=PhotoImage(file="VentanaBubbleSort2.png")
lienzoBubbleSort=Frame(lienzoCaratula,width=750,height=425)
Label(lienzoBubbleSort,image=LogoBubble).place(x=-2,y=0)

#TemaBubbleSort=Label(lienzoBubbleSort,text="BUBBLE SORT (Mejor,peor y caso Promedio)", fg="#FFD767",bg="#9D1321",font=('Calibri', 16)).place(x=100,y=10)#bold
#lbBubbleSort=Label(lienzoBubbleSort,text="Ingrese un tamaño para\n crear los arreglos:", fg="#C3C3C3",bg="#9D1321",font=('Calibri', 16)).place(x=10,y=50)
entradaBubble=Entry(lienzoBubbleSort,bg="#FFF",font=('consolas', 13),highlightbackground="gray",bd=5,textvariable=tamanioBubble)
entradaBubble.place(x=343,y=55)
btnBubbleSort=Button(lienzoBubbleSort,text="Generar",font=('Calibri', 13),bg="#C3C3C3",highlightbackground="black",command=PressBtnBubble).place(x=600,y=55)

#Creamos un lienzo donde se mostrara los resultados de las matrices
txtMejorCasoBubble=ScrolledText(lienzoBubbleSort, width=24,  height=14,bg="#C3C3C3")
txtMejorCasoBubble.place(x=41,y=116)
txtPromedioCasoBubble=ScrolledText(lienzoBubbleSort, width=23,  height=14,bg="#C3C3C3")
txtPromedioCasoBubble.place(x=289,y=116)
txtPeorCasoBubble=ScrolledText(lienzoBubbleSort, width=23,  height=14,bg="#C3C3C3")
txtPeorCasoBubble.place(x=522,y=116)

#lblMejorCasoBubble=Label(lienzoBubbleSort,text="Mejor Caso", fg="#C3C3C3",bg="#9D1321",font=('Calibri', 16)).place(x=53,y=130)
#lblPromedioCasoBubble=Label(lienzoBubbleSort,text="Caso Promedio", fg="#C3C3C3",bg="#9D1321",font=('Calibri', 16)).place(x=280,y=130)
#lblPeorCasoBubble=Label(lienzoBubbleSort,text="Peor Caso", fg="#C3C3C3",bg="#9D1321",font=('Calibri', 16)).place(x=520,y=130)

ResultadosMejorBubble=Entry(lienzoBubbleSort,bg="#C3A88B",font=('consolas', 12),bd=0,width=22)
ResultadosMejorBubble.place(x=48,y=389)
ResultadosPromedioBubble=Entry(lienzoBubbleSort,bg="#C3A88B",font=('consolas', 12),bd=0,width=22)
ResultadosPromedioBubble.place(x=294,y=389)
ResultadosPeorBubble=Entry(lienzoBubbleSort,bg="#C3A88B",font=('consolas', 12),bd=0,width=22)
ResultadosPeorBubble.place(x=526,y=389)



#((((((((((((((((((((((((((((((((((((((((((((Ventana Heap Sort))))))))))))))))))))))))))))))))))))))))))))
#7.- Lienzo Heap Sort
tamanioHeap=StringVar()
LogoHeap=PhotoImage(file="VentanaHeapSort2.png")
lienzoHeapSort=Frame(lienzoCaratula,width=750,height=425)
Label(lienzoHeapSort,image=LogoHeap).place(x=-2,y=0)

#TemaHeapSort=Label(lienzoHeapSort,text="HEAP SORT (Mejor,peor y caso Promedio)", fg="#FFD767",bg="#9D1321",font=('Calibri', 16)).place(x=100,y=10)#bold
#lbHeapSort=Label(lienzoHeapSort,text="Ingrese un tamaño para\n crear los arreglos:", fg="#C3C3C3",bg="#9D1321",font=('Calibri', 16)).place(x=10,y=50)
entradaHeap=Entry(lienzoHeapSort,bg="#FFF",font=('consolas', 13),highlightbackground="gray",bd=5,textvariable=tamanioHeap)
entradaHeap.place(x=343,y=55)
btnHeapSort=Button(lienzoHeapSort,text="Generar",font=('Calibri', 13),bg="#C3C3C3",highlightbackground="black",command=PressBtnHeap).place(x=600,y=55)

#Creamos un lienzo donde se mostrara los resultados de las matrices
txtMejorCasoHeap=ScrolledText(lienzoHeapSort, width=24,  height=14,bg="#C3C3C3")
txtMejorCasoHeap.place(x=41,y=116)
txtPromedioCasoHeap=ScrolledText(lienzoHeapSort, width=23,  height=14,bg="#C3C3C3")
txtPromedioCasoHeap.place(x=289,y=116)
txtPeorCasoHeap=ScrolledText(lienzoHeapSort, width=23,  height=14,bg="#C3C3C3")
txtPeorCasoHeap.place(x=522,y=116)

#lblMejorCasoHeap=Label(lienzoHeapSort,text="Mejor Caso", fg="#C3C3C3",bg="#9D1321",font=('Calibri', 16)).place(x=53,y=130)
#lblPromedioCasoHeap=Label(lienzoHeapSort,text="Caso Promedio", fg="#C3C3C3",bg="#9D1321",font=('Calibri', 16)).place(x=280,y=130)
#lblPeorCasoHeap=Label(lienzoHeapSort,text="Peor Caso", fg="#C3C3C3",bg="#9D1321",font=('Calibri', 16)).place(x=520,y=130)

ResultadosMejorHeap=Entry(lienzoHeapSort,bg="#C3A88B",font=('consolas', 12),bd=0,width=22)
ResultadosMejorHeap.place(x=48,y=389)
ResultadosPromedioHeap=Entry(lienzoHeapSort,bg="#C3A88B",font=('consolas', 12),bd=0,width=22)
ResultadosPromedioHeap.place(x=294,y=389)
ResultadosPeorHeap=Entry(lienzoHeapSort,bg="#C3A88B",font=('consolas', 12),bd=0,width=22)
ResultadosPeorHeap.place(x=526,y=389)



#((((((((((((((((((((((((((((((((((((((((((((Ventana Quick Sort))))))))))))))))))))))))))))))))))))))))))))
#8.- Lienzo Quick Sort
tamanioQuick=StringVar()
LogoQuick=PhotoImage(file="VentanaQuickSort2.png")
lienzoQuickSort=Frame(lienzoCaratula,width=750,height=425)
Label(lienzoQuickSort,image=LogoQuick).place(x=-2,y=0)

#TemaQuickSort=Label(lienzoQuickSort,text="QUICK SORT (Mejor,peor y caso Promedio)", fg="#FFD767",bg="#9D1321",font=('Calibri', 16)).place(x=100,y=10)#bold
#lbQuickSort=Label(lienzoQuickSort,text="Ingrese un tamaño para\n crear los arreglos:", fg="#C3C3C3",bg="#9D1321",font=('Calibri', 16)).place(x=10,y=50)
entradaQuick=Entry(lienzoQuickSort,bg="#FFF",font=('consolas', 13),highlightbackground="gray",bd=5,textvariable=tamanioQuick)
entradaQuick.place(x=343,y=55)
btnQuickSort=Button(lienzoQuickSort,text="Generar",font=('Calibri', 13),bg="#C3C3C3",highlightbackground="black",command=PressBtnQuick).place(x=600,y=55)

#Creamos un lienzo donde se mostrara los resultados de las matrices
txtMejorCasoQuick=ScrolledText(lienzoQuickSort, width=24,  height=14,bg="#C3C3C3")
txtMejorCasoQuick.place(x=41,y=116)
txtPromedioCasoQuick=ScrolledText(lienzoQuickSort, width=23,  height=14,bg="#C3C3C3")
txtPromedioCasoQuick.place(x=289,y=116)
txtPeorCasoQuick=ScrolledText(lienzoQuickSort, width=23,  height=14,bg="#C3C3C3")
txtPeorCasoQuick.place(x=522,y=116)

#lblMejorCasoQuick=Label(lienzoQuickSort,text="Mejor Caso", fg="#C3C3C3",bg="#9D1321",font=('Calibri', 16)).place(x=53,y=130)
#lblPromedioCasoQuick=Label(lienzoQuickSort,text="Caso Promedio", fg="#C3C3C3",bg="#9D1321",font=('Calibri', 16)).place(x=280,y=130)
#lblPeorCasoQuick=Label(lienzoQuickSort,text="Peor Caso", fg="#C3C3C3",bg="#9D1321",font=('Calibri', 16)).place(x=520,y=130)

ResultadosMejorQuick=Entry(lienzoQuickSort,bg="#C3A88B",font=('consolas', 12),bd=0,width=22)
ResultadosMejorQuick.place(x=48,y=389)
ResultadosPromedioQuick=Entry(lienzoQuickSort,bg="#C3A88B",font=('consolas', 12),bd=0,width=22)
ResultadosPromedioQuick.place(x=294,y=389)
ResultadosPeorQuick=Entry(lienzoQuickSort,bg="#C3A88B",font=('consolas', 12),bd=0,width=22)
ResultadosPeorQuick.place(x=526,y=389)



#((((((((((((((((((((((((((((((((((((((((((((Ventana Bucket Sort))))))))))))))))))))))))))))))))))))))))))))
#9.- Lienzo Bucket Sort
tamanioBucket=StringVar()
LogoBucket=PhotoImage(file="VentanaBucketSort2.png")
lienzoBucketSort=Frame(lienzoCaratula,width=750,height=425)
Label(lienzoBucketSort,image=LogoBucket).place(x=-2,y=0)

#TemaBucketSort=Label(lienzoBucketSort,text="BUCKET SORT (Mejor,peor y caso Promedio)", fg="#FFD767",bg="#9D1321",font=('Calibri', 16)).place(x=100,y=10)#bold
#lbBucketSort=Label(lienzoBucketSort,text="Ingrese un tamaño para\n crear los arreglos:", fg="#C3C3C3",bg="#9D1321",font=('Calibri', 16)).place(x=10,y=50)
entradaBucket=Entry(lienzoBucketSort,bg="#FFF",font=('consolas', 13),highlightbackground="gray",bd=5,textvariable=tamanioBucket)
entradaBucket.place(x=343,y=55)
btnBucketSort=Button(lienzoBucketSort,text="Generar",font=('Calibri', 13),bg="#C3C3C3",highlightbackground="black",command=PressBtnBucket).place(x=600,y=55)

#Creamos un lienzo donde se mostrara los resultados de las matrices
txtMejorCasoBucket=ScrolledText(lienzoBucketSort, width=24,  height=14,bg="#C3C3C3")
txtMejorCasoBucket.place(x=41,y=116)
txtPromedioCasoBucket=ScrolledText(lienzoBucketSort, width=23,  height=14,bg="#C3C3C3")
txtPromedioCasoBucket.place(x=289,y=116)
txtPeorCasoBucket=ScrolledText(lienzoBucketSort, width=23,  height=14,bg="#C3C3C3")
txtPeorCasoBucket.place(x=522,y=116)

#lblMejorCasoBucket=Label(lienzoBucketSort,text="Mejor Caso", fg="#C3C3C3",bg="#9D1321",font=('Calibri', 16)).place(x=53,y=130)
#lblPromedioCasoBucket=Label(lienzoBucketSort,text="Caso Promedio", fg="#C3C3C3",bg="#9D1321",font=('Calibri', 16)).place(x=280,y=130)
#lblPeorCasoBucket=Label(lienzoBucketSort,text="Peor Caso", fg="#C3C3C3",bg="#9D1321",font=('Calibri', 16)).place(x=520,y=130)

ResultadosMejorBucket=Entry(lienzoBucketSort,bg="#C3A88B",font=('consolas', 12),bd=0,width=22)
ResultadosMejorBucket.place(x=48,y=389)
ResultadosPromedioBucket=Entry(lienzoBucketSort,bg="#C3A88B",font=('consolas', 12),bd=0,width=22)
ResultadosPromedioBucket.place(x=294,y=389)
ResultadosPeorBucket=Entry(lienzoBucketSort,bg="#C3A88B",font=('consolas', 12),bd=0,width=22)
ResultadosPeorBucket.place(x=526,y=389)



#((((((((((((((((((((((((((((((((((((((((((((Ventana Selection Sort))))))))))))))))))))))))))))))))))))))))))))
#10.- Lienzo Selecion Sort
tamanioSelection=StringVar()
LogoSelection=PhotoImage(file="VentanaSelectionSort2.png")
lienzoSelectionSort=Frame(lienzoCaratula,width=750,height=425)
Label(lienzoSelectionSort,image=LogoSelection).place(x=-2,y=0)

#TemaSelectionSort=Label(lienzoSelectionSort,text="SELECTION SORT (Mejor,peor y caso Promedio)", fg="#FFD767",bg="#9D1321",font=('Calibri', 16)).place(x=100,y=10)#bold
#lbSelectionSort=Label(lienzoSelectionSort,text="Ingrese un tamaño para\n crear los arreglos:", fg="#C3C3C3",bg="#9D1321",font=('Calibri', 16)).place(x=10,y=50)
entradaSelection=Entry(lienzoSelectionSort,bg="#FFF",font=('consolas', 13),highlightbackground="gray",bd=5,textvariable=tamanioSelection)
entradaSelection.place(x=343,y=55)
btnSelectionSort=Button(lienzoSelectionSort,text="Generar",font=('Calibri', 13),bg="#C3C3C3",highlightbackground="black",command=PressBtnSelection).place(x=600,y=55)

#Creamos un lienzo donde se mostrara los resultados de las matrices
txtMejorCasoSelection=ScrolledText(lienzoSelectionSort, width=24,  height=14,bg="#C3C3C3")
txtMejorCasoSelection.place(x=41,y=116)
txtPromedioCasoSelection=ScrolledText(lienzoSelectionSort, width=23,  height=14,bg="#C3C3C3")
txtPromedioCasoSelection.place(x=289,y=116)
txtPeorCasoSelection=ScrolledText(lienzoSelectionSort, width=23,  height=14,bg="#C3C3C3")
txtPeorCasoSelection.place(x=522,y=116)

#lblMejorCasoSelection=Label(lienzoSelectionSort,text="Mejor Caso", fg="#C3C3C3",bg="#9D1321",font=('Calibri', 16)).place(x=53,y=130)
#lblPromedioCasoSelection=Label(lienzoSelectionSort,text="Caso Promedio", fg="#C3C3C3",bg="#9D1321",font=('Calibri', 16)).place(x=280,y=130)
#lblPeorCasoSelection=Label(lienzoSelectionSort,text="Peor Caso", fg="#C3C3C3",bg="#9D1321",font=('Calibri', 16)).place(x=520,y=130)

ResultadosMejorSelection=Entry(lienzoSelectionSort,bg="#C3A88B",font=('consolas', 12),bd=0,width=22)
ResultadosMejorSelection.place(x=48,y=389)
ResultadosPromedioSelection=Entry(lienzoSelectionSort,bg="#C3A88B",font=('consolas', 12),bd=0,width=22)
ResultadosPromedioSelection.place(x=294,y=389)
ResultadosPeorSelection=Entry(lienzoSelectionSort,bg="#C3A88B",font=('consolas', 12),bd=0,width=22)
ResultadosPeorSelection.place(x=526,y=389)


#((((((((((((((((((((((((((((((((((((((((((((Ventana Comb Sort))))))))))))))))))))))))))))))))))))))))))))
#11.- Lienzo Comb Sort
tamanioComb=StringVar()
LogoComb=PhotoImage(file="VentanaCombSort2.png")
lienzoCombSort=Frame(lienzoCaratula,width=750,height=425)
Label(lienzoCombSort,image=LogoComb).place(x=-2,y=0)

#TemaCombSort=Label(lienzoCombSort,text="COMB SORT (Mejor,peor y caso Promedio)", fg="#FFD767",bg="#9D1321",font=('Calibri', 16)).place(x=100,y=10)#bold
#lbCombSort=Label(lienzoCombSort,text="Ingrese un tamaño para\n crear los arreglos:", fg="#C3C3C3",bg="#9D1321",font=('Calibri', 16)).place(x=10,y=50)
entradaComb=Entry(lienzoCombSort,bg="#FFF",font=('consolas', 13),highlightbackground="gray",bd=5,textvariable=tamanioComb)
entradaComb.place(x=343,y=55)
btnCombSort=Button(lienzoCombSort,text="Generar",font=('Calibri', 13),bg="#C3C3C3",highlightbackground="black",command=PressBtnComb).place(x=600,y=55)

#Creamos un lienzo donde se mostrara los resultados de las matrices
txtMejorCasoComb=ScrolledText(lienzoCombSort, width=24,  height=14,bg="#C3C3C3")
txtMejorCasoComb.place(x=41,y=116)
txtPromedioCasoComb=ScrolledText(lienzoCombSort, width=23,  height=14,bg="#C3C3C3")
txtPromedioCasoComb.place(x=289,y=116)
txtPeorCasoComb=ScrolledText(lienzoCombSort, width=23,  height=14,bg="#C3C3C3")
txtPeorCasoComb.place(x=522,y=116)

#lblMejorCasoComb=Label(lienzoCombSort,text="Mejor Caso", fg="#C3C3C3",bg="#9D1321",font=('Calibri', 16)).place(x=53,y=130)
#lblPromedioCasoComb=Label(lienzoCombSort,text="Caso Promedio", fg="#C3C3C3",bg="#9D1321",font=('Calibri', 16)).place(x=280,y=130)
#lblPeorCasoComb=Label(lienzoCombSort,text="Peor Caso", fg="#C3C3C3",bg="#9D1321",font=('Calibri', 16)).place(x=520,y=130)

ResultadosMejorComb=Entry(lienzoCombSort,bg="#C3A88B",font=('consolas', 12),bd=0,width=22)
ResultadosMejorComb.place(x=48,y=389)
ResultadosPromedioComb=Entry(lienzoCombSort,bg="#C3A88B",font=('consolas', 12),bd=0,width=22)
ResultadosPromedioComb.place(x=294,y=389)
ResultadosPeorComb=Entry(lienzoCombSort,bg="#C3A88B",font=('consolas', 12),bd=0,width=22)
ResultadosPeorComb.place(x=526,y=389)

#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[Menu Ordenar]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

#((((((((((((((((((((((((((((((((((((((((((Ventana Ordenar Arreglo Aleatorio))))))))))))))))))))))))))))))))))))))))))
#Creamos un lienzo para ordenar un Arreglo Aleatorio
lienzoArregloAleatorio=Frame(lienzoCaratula,width=750,height=425)
#...
#...
#...
#((((((((((((((((((((((((((((((((((((((((((Ventana Ordenar Arreglo Definido))))))))))))))))))))))))))))))))))))))))))
#"#3AC8B6"
#TemaArregloDefinido=Label(lienzoArregloDefinido,text="ORDENAR UN ARREGLO DEFINIDA POR EL USUARIO", fg="#FFD767",bg="#9D1321",font=('Calibri', 16)).place(x=100,y=10)#bold
#lbArregloDefinido=Label(lienzoArregloDefinido,text="Ingrese el arreglo a\n ordenar:", fg="#C3C3C3",bg="#4C5C83",font=('Calibri', 16)).place(x=10,y=10)
LogoArrayOrdenado=PhotoImage(file="VentanaArrayOrdenado4.png")
lienzoArregloDefinido=Frame(lienzoCaratula,width=750,height=425)
Label(lienzoArregloDefinido,image=LogoArrayOrdenado).place(x=-2,y=0)
EntradaArregloDefinido=ScrolledText(lienzoArregloDefinido, width=49,  height=11,bg="#EEEFF1")#Estaba sin fuente(font) font=('consolas', 12)
EntradaArregloDefinido.place(x=222,y=36)
#lbPropositoArregloDefinido=Label(lienzoArregloDefinido,text="Ordenar por:", fg="#C3C3C3",bg="#4C5C83",font=('Calibri', 16)).place(x=10,y=180)
#lbOpcionesArregloDefinido=Label(lienzoArregloDefinido,width=50,height=9,bg="#EFE4B0").place(x=30,y=264)#y=195
opcion=IntVar()
rdBtnInsertSort=Radiobutton(lienzoArregloDefinido,text="Insertion Sort",variable=opcion,value=1).place(x=40,y=270)#195+25=220
rdBtnMergeSort=Radiobutton(lienzoArregloDefinido,text="Merge Sort",variable=opcion,value=2).place(x=40,y=305)#230
rdBtnShellSort=Radiobutton(lienzoArregloDefinido,text="Shell Sort",variable=opcion,value=3).place(x=40,y=340)#265
rdBtnRadixSort=Radiobutton(lienzoArregloDefinido,text="Radix Sort",variable=opcion,value=4,command=VerificarOpcion).place(x=40,y=375)#300
rdBtnBubbleSort=Radiobutton(lienzoArregloDefinido,text="Bubble Sort",variable=opcion,value=5).place(x=150,y=270)#195
rdBtnHeapSort=Radiobutton(lienzoArregloDefinido,text="Heap Sort",variable=opcion,value=6).place(x=150,y=305)#230
rdBtnQuickSort=Radiobutton(lienzoArregloDefinido,text="Quick Sort",variable=opcion,value=7).place(x=150,y=340)#265
rdBtnBucketSort=Radiobutton(lienzoArregloDefinido,text="Bucket Sort",variable=opcion,value=8,command=VerificarOpcion).place(x=150,y=375)#300
rdBtnSelectionSort=Radiobutton(lienzoArregloDefinido,text="Selection Sort",variable=opcion,value=9).place(x=260,y=270)#195
rdBtnCombSort=Radiobutton(lienzoArregloDefinido,text="Comb Sort",variable=opcion,value=10).place(x=260,y=305)#230

btnArregloDefinido=Button(lienzoArregloDefinido,text="Ordenar",font=('Calibri', 16),bg="#C3C3C3",highlightbackground="black",command=CrearVentanaOrdenarArregloDefinido).place(x=445,y=264)

root.mainloop()
