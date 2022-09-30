import csv


# ----------- MAIN ---------
estudiantes = {}
archivo = open ('TP5/datos/vehiculos.txt','r',encoding="utf-8")
for linea in archivo:
    estudiante=linea.rstrip("\n").split(";")
    estudiantes.append(estudiante)
#cambiarStrInteger(vehiculos)
print(estudiantes)