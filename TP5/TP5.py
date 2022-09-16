from io import open
import os

def menu():
    print('1) Buscar por dominio')
    print('2) Mostrar el listado de vehiculos.')
    print('3) Reservar automovil por su dominio')
    print('4) Buscar un automovil por su dominio')
    print('5) Ordenar asc/desc por marca. ')
    print('6) Ordenar asc/desc por Precio Venta')
    print('0) Salir')
    eleccion = int(input('Elija una opción: '))
    while not((eleccion >= 0) and (eleccion <= 6)):
        eleccion = int(input('Elija una opción: '))
    os.system('cls')
    return eleccion

def mostrar(vehiculos):
    print('\n Dominio     Marca         Tipo        Modelo   Kilometraje Precio_Valuado   PrecioVenta   Estado')
    print('==========================================================================================================')
    for lista in vehiculos:
        print('{:^8}  {:^13} {:^13} {:^8} {:10} {:13.2f} {:15.2f} {:8}' .format(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7]))
    input("\nPresione <ENTER> para Continuar...")
                                            #{:10.2f}  {:10.2f}

def cambiarStrInteger(vehiculos):
    for fila in range(len(vehiculos)):
        vehiculos[fila][3]=int(vehiculos[fila][3])
        vehiculos[fila][4]=int(vehiculos[fila][4])
        vehiculos[fila][5]=float(vehiculos[fila][5])
        vehiculos[fila][6]=float(vehiculos[fila][6])

        
def busquedaBinaria(arreglo, busqueda):
    izquierda, derecha = 0, len(arreglo) - 1
    while izquierda <= derecha:
        indiceDelElementoDelMedio = (izquierda + derecha) // 2
        elementoDelMedio = arreglo[indiceDelElementoDelMedio][0]
        if elementoDelMedio == busqueda:
            return indiceDelElementoDelMedio
        if busqueda < elementoDelMedio:
            derecha = indiceDelElementoDelMedio - 1
        else:
            izquierda = indiceDelElementoDelMedio + 1
    # Si salimos del ciclo significa que no existe el valor
    return -1


def busquedaBinariaRecursiva(arreglo, busqueda, izquierda, derecha):
    if izquierda > derecha:
        return -1
    indiceDelElementoDelMedio = (izquierda + derecha) // 2
    elementoDelMedio = arreglo[indiceDelElementoDelMedio]
    print(elementoDelMedio)
    if elementoDelMedio == busqueda:
        return indiceDelElementoDelMedio
    if busqueda < elementoDelMedio:
        return busqueda_binaria_recursiva(arreglo, busqueda, izquierda, indiceDelElementoDelMedio - 1)
    else:
        return busqueda_binaria_recursiva(arreglo, busqueda, indiceDelElementoDelMedio + 1, derecha)



#---------- main ----------
vehiculos = []
archivo = open ('TP5/datos/vehiculos.txt','r',encoding="utf-8")
for linea in archivo:
    vehiculo=linea.rstrip("\n").split(";")
    vehiculos.append(vehiculo)
cambiarStrInteger(vehiculos)
vehiculos.sort()

opcion = 99
while  opcion!= 0:
    opcion = menu()
    if opcion == 1:
        dominio = input('ingrese el dominio que busca: ')
        pos = busquedaBinaria(vehiculos,dominio)
        if pos==-1:
            input('dominio no existe')
        else:
            vehiculosAux = []
            vehiculosAux.append(vehiculos[pos])
            mostrar(vehiculosAux)

