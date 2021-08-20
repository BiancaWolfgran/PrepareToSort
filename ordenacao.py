import time
import timeit
import random

#------MÉTODO BUBBLESORT------

def bubbleSort(lista):
    n = len(lista)
    for j in range(n-1):
        for i in range(n-1):
            if(lista[i] > lista[i+1]):
                lista[i], lista[i+1] = lista[i+1], lista[i]
                

#-----MÉTODO MERGESORT------

def mergeSort(lista):
    if len(lista) > 1:
 
         # procura meio da lista
        mid = len(lista)//2
 
        # divide a lista no meio
        L = lista[:mid]
 
        # divide em duas partes
        R = lista[mid:]
 
        # ordena a primeira metade
        mergeSort(L)
 
        # ordena segunda metade
        mergeSort(R)
 
        i = j = k = 0
 
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                lista[k] = L[i]
                i += 1
            else:
                lista[k] = R[j]
                j += 1
            k += 1
 
        # verifica de faltou algum elemento
        while i < len(L):
            lista[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            lista[k] = R[j]
            j += 1
            k += 1



 #-----MÉTODO HEAPSORT------

 #HEAP
def heapify(lista, n, i):
    largest = i  
    l = 2 * i + 1     
    r = 2 * i + 2     
 
    if l < n and lista[largest] < lista[l]:
        largest = l
 

    if r < n and lista[largest] < lista[r]:
        largest = r
 
    if largest != i:
        lista[i], lista[largest] = lista[largest], lista[i]  
 
        heapify(lista, n, largest)
 
#HEAPSORT
 
def heapSort(lista):
    n = len(lista)
 
    # maxheap
    for i in range(n//2 - 1, -1, -1):
        heapify(lista, n, i)
 
    for i in range(n-1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]  # swap
        heapify(lista, i, 0)


#LISTA COM ELEMENTOS ALEATÓRIOS
x=1000
lista=[random.randint(0, 100) for _ in range(x)]
print('ELEMENTOS ALEATORIOS: ')
#print(lista)



#calcular tempo de duração do metodo bubblesort
inicio = timeit.default_timer()
bubbleSort(lista)
fim = timeit.default_timer()
print ('tempo de duracao do bubblesort: %f' % (fim - inicio))

#calcular  tempo de duração do metodo mergesort
inicio = timeit.default_timer()
mergeSort(lista)
fim = timeit.default_timer()
print ('tempo de duracao do mergesort: %f' % (fim - inicio))


#calcular tempo de duração do metodo heapsort
inicio = timeit.default_timer()
heapSort(lista)
fim = timeit.default_timer()
print ('tempo de duracao do heapsort: %f' % (fim - inicio))

##################################################################

#LISTA ORDEM DECRESCENTE
lista = list(range(1000))
lista.sort(reverse = True)
print('\nELEMENTOS EM ORDEM DECRESCENTE: ')
#print(lista)


#calcular tempo de duração do metodo bubblesort
inicio = timeit.default_timer()
bubbleSort(lista)
fim = timeit.default_timer()
print ('tempo de duracao do bubblesort: %f' % (fim - inicio))

#calcular  tempo de duração do metodo mergesort
inicio = timeit.default_timer()
mergeSort(lista)
fim = timeit.default_timer()
print ('tempo de duracao do mergesort: %f' % (fim - inicio))


#calcular tempo de duração do metodo heapsort
inicio = timeit.default_timer()
heapSort(lista)
fim = timeit.default_timer()
print ('tempo de duracao do heapsort: %f' % (fim - inicio))


##########################################################

#LISTA ORDEM CRESCENTE
lista = list(range(1000))
print('\nELEMENTOS EM ORDEM CRESCENTE: ')
#print(lista)

#calcular tempo de duração do metodo bubblesort
inicio = timeit.default_timer()
bubbleSort(lista)
fim = timeit.default_timer()
print ('tempo de duracao do bubblesort: %f' % (fim - inicio))

#calcular  tempo de duração do metodo mergesort
inicio = timeit.default_timer()
mergeSort(lista)
fim = timeit.default_timer()
print ('tempo de duracao do mergesort: %f' % (fim - inicio))


#calcular tempo de duração do metodo heapsort
inicio = timeit.default_timer()
heapSort(lista)
fim = timeit.default_timer()
print ('tempo de duracao do heapsort: %f' % (fim - inicio))
