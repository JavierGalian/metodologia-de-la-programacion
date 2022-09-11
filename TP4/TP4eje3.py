import os

from random import randint

def presionarTecla():
    input("Press Enter.....")


def menu():
    print('elegir metodo que desea implementar')
    print('1-metodo mergeSort')
    print('2-metodo quickSort')
    print('3-metodo shell')
    print('0-salir')
    option = int(input('Elija una opción: '))
    while not((option >= 0) and (option <= 3)):
        option = int(input('Elija una opción: '))
    os.system('cls')
    return option

    option = int(input())

def loadList():
    listNumAleatorios = []
    n=int(input("Cantidad de aleatorios: "))
    for i in range(n):
        listNumAleatorios.append(randint(0,1000))
    return listNumAleatorios

# ----- INICIO MERGE SORT -----
 
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

# ----- FIN MERGE SORT -----


# ----- INICIO QUICK SORT -----
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

# ----- FIN QUICK SORT -----


# ----- INICIO SHELL -----
def shell(lst):
    n = len(lst)
    gap = n // 2 # … 112,48,21,7,5,1
    while gap > 0:
        for i in range(gap, n):
            tmp = lst[i]
            j = i
            while j >= gap and lst[j - gap] > tmp:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = tmp
        gap = gap // 2
    return lst

# ----- FIN SHELL -----

# --- main ---
option = 99
while option!=0:
    option = menu()
    if option==1:
        listNumAleatorios = loadList()
        print('lista Creada: ', listNumAleatorios)
        listNumAleatoriosOrdenada = mergesort(listNumAleatorios)
        print('lista ordenada: ', listNumAleatoriosOrdenada)
        input("\nPresione <ENTER> para Continuar...")
    elif option==2:
        listNumAleatorios = loadList()
        print('lista Creada: ', listNumAleatorios)
        listNumAleatoriosOrdenada = quickSort(listNumAleatorios,0,len(listNumAleatorios)-1)
        print('lista ordenada: ', listNumAleatoriosOrdenada)
        input("\nPresione <ENTER> para Continuar...")
    elif option==3:
        listNumAleatorios = loadList()
        print('lista Creada: ', listNumAleatorios)
        listNumAleatoriosOrdenada = shell(listNumAleatorios)
        print('lista ordenada: ', listNumAleatoriosOrdenada)
        input("\nPresione <ENTER> para Continuar...")
    elif option == 0:
        print("FIN DEL PROGRAMA...")
        presionarTecla() 