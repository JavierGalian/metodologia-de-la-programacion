from io import open

vehiculos = []
#fichero = open ('TP5/datos/vehiculos.txt','r',encoding="utf-8")
#print(fichero.read())
#fichero.close()

#with open("TP5/datos/vehiculos.txt" , 'r' , encoding="utf-8") as archivo:
 #   for linea in archivo:
  #      vehiculo = [linea.rstrip("\n").split(";") for linea in archivo] 
        #lineas = [linea.split() for linea in archivo]
#for linea in vehiculo:
 #   print(linea)
archivo = open ('TP5/datos/vehiculos.txt','r',encoding="utf-8")
for linea in archivo:
    vehiculo=linea.rstrip("\n").split(";")
    vehiculos.append(vehiculo)

print(vehiculos)




#veh = ast.literal_eval(vehiculos)
#print(veh)



#def cargarVehiculos(archivo):
 #   listaVehiculos = []
  #  for linea in archivo:
   #     vehiculo = linea.rstrip("\n").split(";") 


#salida = []
#with open('archivo.txt', 'r') as f:
 #   lineas = [linea.split() for linea in f]

#for linea in lineas:
 #   print(linea)