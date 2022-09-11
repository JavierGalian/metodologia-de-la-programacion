#function
def cargarListIntervalo(numA,numB):
    listIntervalo = []
    for i in range(numA,numB+1):
        listIntervalo.append(i)
    return listIntervalo

def numPrimos(listIntervalo):
    listNumPrimos = []
    for i in listIntervalo:
        contador = 0
        for j in range(2,i):
            resto=(i%j)
            if (resto==0):
                contador+=1
        if (contador==0):
            listNumPrimos.append(i)
    return listNumPrimos

def validacion(numA,numB):
    if (numA==0)|(numB==0):
        return False
    else:
        if (numA>0) & (numB>0):
            if (numA<numB):
                return True
            else:
                print("Error... numero B es menor que numero A")
                return False
        else:
            print("Error... ingreso numeros menores que cero")
            return False
        

# main algorithm
opcion = True
while opcion:
    print("Ingrese un intervalo de numeros y se le mostrara los numeros primos")
    print("El algoritmo termina cuando ingrese el valor 0 (cero)")
    numA = int(input("num A: "))
    numB = int(input("num B: ")) 
    
    if (validacion(numA,numB)==False):
        print("<--------------------------------------------------------------------->")
    else:
        listIntervalo = cargarListIntervalo(numA,numB)
        listNumPrimos = numPrimos(listIntervalo)
        print("intervalos de numeros: ", listIntervalo)
        print("numeros primos: ", listNumPrimos)

print ("fin")

    
