import os

def menu():
    print('1) Cargar vehiculos...')
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

def agregar(vehiculos):
    dominio = input("INGRESE DOMINIO: ")
    while dominio != "0":
    # Dominio, Marca, Tipo, Modelo, Kilometraje, precValuado, estado
        marca = input("MARCA: R=Renault, F=Ford, C=Citroen: ")
        tipo = input("TIPO: U=Utilitario A=Automovil")
        modelo = int(input("MODELO: "))
        kilometraje = int(input("KILOMETRAJE: "))
        precValuado = float(input("PRECIO VALUADO: "))
        precVenta = precValuado + precValuado * 10 / 100
        estado = "D"
        vehiculos.append([dominio, marca, tipo, modelo, kilometraje, precValuado, precVenta, estado])
        dominio = input("INGRESE DOMINIO (0 para terminar): ")
    return vehiculos

def mostrar(vehiculos):
    print('\n Dominio Marca Tipo Modelo Kilometraje Precio_Valuado  PrecioVenta Estado')
    print(' ========================================================================')
    for lista in vehiculos:
        print('{:^6}  {:^6} {:^6} {:^6} {:8} {:10.2f}  {:10.2f} {:8}' .format(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7]))
    input("\nPresione <ENTER> para Continuar...")

def  buscarPorDominio(vehiculos, domiAux):
    pos = -1
    for i, item in enumerate(vehiculos):
        if item[0] == domiAux:
            pos = i
            break
    return pos

def reservar(vehiculos):
    dominio = input('ingrese dominio del vehiculo que desea reservar')
    pos = buscarPorDominio(vehiculos,dominio)
    
    vehiculosAux=[]
    vehiculosAux.append(vehiculos[pos]) 
    mostrar(vehiculosAux)

    vehiculos[pos][7]='R'
    return vehiculos

def inicializar():
    vehiculos = []
    vehiculos = [['CCCCCCC', 'R', 'U', 2030, 3, 3, 3, 'D'],
                ['AAAAAAA', 'C', 'U', 2010, 1, 1, 1, 'D'],
                ['BBBBBBB', 'F', 'U', 2020, 2, 2, 2, 'D'],
                ['ZZZZZZZ', 'R', 'A', 2021, 25, 25, 25, 'D'],
                ['FFFFFFF', 'C', 'U', 2022, 5, 5, 5, 'D']]    
    return vehiculos  

def bubbleSortAscendente(vehiculos,posicion):
    n = len(vehiculos)
    for i in range(n):
        for j in range(0, n-1):
            if vehiculos[j][posicion] > vehiculos[j+1][posicion]:
                vehiculos[j], vehiculos[j+1] = vehiculos[j+1], vehiculos[j]
    return vehiculos

def bubbleSortDescendente(vehiculos,posicion):
    n = len(vehiculos)
    for i in range(n):
        for j in range(0, n-1):
            if vehiculos[j][posicion] < vehiculos[j+1][posicion]:
                vehiculos[j], vehiculos[j+1] = vehiculos[j+1], vehiculos[j]
    return vehiculos

def menuOrdenamiento():
    print('1) Ascendente')
    print('2) Descendente')
    eleccion = int(input('Elija una opción: '))
    while not((eleccion >= 1) and (eleccion <= 2)):
        eleccion = int(input('Elija una opción: '))
    os.system('cls')
    return eleccion

def presionarTecla():
    input("Press key.....")
           

#  ---   main -----
vehiculos = inicializar()
opcion = 99
while opcion != 0:
    opcion = menu()
    if opcion == 1:
        vehiculos = agregar(vehiculos)
    elif opcion == 2:
        mostrar(vehiculos)
    elif opcion == 3:
        reservar(vehiculos)
    elif opcion == 4:
        domiAux = input("INGRESE DOMINIO A BUSCAR: ")
        pos = buscarPorDominio(vehiculos, domiAux)
        if pos == -1:
            print("DOMINIO NO ENCONTRADO..")
        else:
            vehiculosAux=[]
            vehiculosAux.append(vehiculos[pos]) 
            mostrar(vehiculosAux)
    elif opcion==5:
        opcOrden=menuOrdenamiento()
        if opcOrden==1:
            bubbleSortAscendente(vehiculos,1)
            mostrar(vehiculos)
        elif opcOrden==2:
            bubbleSortDescendente(vehiculos,1)
            mostrar(vehiculos)
    elif opcion==6:
        opcOrden=menuOrdenamiento()
        if opcOrden==1:
            bubbleSortAscendente(vehiculos,6)
            mostrar(vehiculos)
        elif opcOrden==2:
            bubbleSortDescendente(vehiculos,6)
            mostrar(vehiculos)
    elif opcion == 0:
        print("FIN DEL PROGRAMA...")
        presionarTecla() 