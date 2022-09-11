#CasosPractico04:
import os
from random import randint
#Borrar pantalla:
def detectSystem():
    if os.name == "nt":
        borrar = "cls"
    else:
        borrar = "clear"
    return borrar

def cleanScrean():
    os.system(detectSystem())

#Modulos del Trabajo__________________
def cargarLista():
    #lista = [6, 0, 3, 2, 5, 7, 4, 1]
    lista = []
    n=int(input("Cantidad de aleatorios: "))
    for i in range(n):
        lista.append(randint(0,1000))
    return lista

def mostrarLista(lista):
    print(lista)


#METODO QUICKSORT

def quickSort(lst, start, stop):
    #print(start,stop)
    if stop - start > 0:
        pivot, left, right = lst[start], start, stop
        #print(pivot)
        #print(lst)
        while left <= right:
            while lst[left] < pivot:
                left += 1
            while lst[right] > pivot:
                right -= 1
            if left <= right:
                lst[left], lst[right] = lst[right], lst[left]
                left += 1
                right -= 1
        quickSort(lst, start, right)
        quickSort(lst, left, stop)
    return lst



# METODO MERGE

def mergesort(A):
    if(len(A) <= 1):
        return A
 
    izq=[]
    der=[]
    medio=len(A)//2
    for i in range(0,medio):
        izq.append(A[i])
    for i in range(medio,len(A)):
        der.append(A[i])
 
    izq=mergesort(izq)
    der=mergesort(der)
 
    return merge(izq,der)
 
def merge(izq,der):
    arreglo=[]
    i=0
    j=0
    while(i < len(izq) and j < len(der)):
        if(izq[i] <= der[j]):
            arreglo.append(izq[i])
            i=i+1
        else:
            arreglo.append(der[j])
            j=j+1
    while(i < len(izq)):
        arreglo.append(izq[i])
        i=i+1
    while(j < len(der)):
        arreglo.append(der[j])
        j=j+1
       
    return arreglo


def menu():
    print('metodo que desea realizar:')
    print('1- metodo quicksort')
    option=int(input())
    return option


#Programa Principal
cleanScrean()
lista = cargarLista()
mostrarLista(lista)
#quickSort(lista,0,len(lista)-1)
#print("la lista ordenada es:")
#mostrarLista(lista)     #Muestra la lista ya ordenada

option=menu()