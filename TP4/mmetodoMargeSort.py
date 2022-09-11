#Declaracion de Funciones
 
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
 
#Programa Principal
A=[6,5,3,1,8,7,2,4,9]
print (A)
A=mergesort(A)
print (A)