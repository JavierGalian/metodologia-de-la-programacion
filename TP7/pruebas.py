

from multiprocessing.sharedctypes import Value


estudiantes = {}
archivo = open ('TP7/datos/tp07-Estudiantes.csv','r')
for linea in archivo:
    fila = linea.rstrip('\n').split(';')
    apellidoNombre = fila[0]
    dni = (fila[1])
    carrera = fila[2]
    if fila[3] == '':
        fila[3] = '-'
        nota = fila[3]
    else:
        nota = fila[3]   
    estudiantes [dni] = apellidoNombre,carrera,nota


#print (estudiantes)    

for keys,value in estudiantes.items():
    result = estudiantes.get(keys)
    #print(keys,result)
    print(value)