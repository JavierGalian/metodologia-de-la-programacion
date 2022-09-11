def menu():
    print('1-ingresar vehiculo')
    print('2-mostrar vehiculos')
    print('3-reservar un vehiculo')
    print('4-buscar un vehiculo por dominio')
    print('5-mostrarvehiculos en forma descendente por marca')
    print('6-mostrar vehiculos en forma descendente por precio(solo disponibles) ')

def agregarVehiculos(vehiculos):


    
repeteir = True
vehuculos=[]
while (repetir):
    menu()
    option=int(input())
    if (option==1):
        agregarVehiculo(vehiculos)
