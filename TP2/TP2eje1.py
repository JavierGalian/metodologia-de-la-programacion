
import operator

def menu():
    print('1-Registrar prodructo')
    print('2-mostrar lista de productos')
    print('3-buscar producto por stock (desde-hasta)')
    print('4-precio mas alto de stock ')
    print('5-')
    print('6-eliminar productos cuyo stock sea igual a cero')
    print('7-salir')

def registrarProducto(listaProductos):
    producto=input('intruce el producto: ')
    codigo=input('ingrese codigo: ')
    descripcion=input('ingrese descripcion: ')
    precio=input('ingrese precio: ')
    stock=int(input('ingrese stock: '))
    listaProductos[producto]=[codigo,descripcion,precio,stock]

def mostrarProductos(listaProductos):
    print(listaProductos)

def busquedaPorIntervalos(listaProductos):
    minStock= int(input('ingrese stock minimo: '))
    maxStock= int(input('ingrese stock maximo: '))
    for productos, stock  in listaProductos.items():
        if (stock[3] >= minStock) & (stock[3] <= maxStock): 
            print(productos, stock)
            
def precioMasAlto(listaProductos):
    maxPrecio = max(listaProductos, key = listaProductos.get)
    print('producto con maximo precio: ',maxPrecio , listaProductos[maxPrecio])

def eliminarProducto(listaProductos):
    for productos, stock  in list(listaProductos.items()):
        if (stock[3] == 0): 
            print(productos, stock)
            del listaProductos[productos]
            print('eliminado')

option=0
clave=0
listaProductos = {}
while(option!=7):
    menu()
    option=int(input())
    if (option==1):
        
        registrarProducto(listaProductos)
    if (option==2):
        mostrarProductos(listaProductos)
    if (option==3):
        busquedaPorIntervalos(listaProductos)
    if (option==4):
        precioMasAlto(listaProductos)
    if (option==6):
        eliminarProducto(listaProductos)