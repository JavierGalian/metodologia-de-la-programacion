with open("vehiculos.txt") as file_object:
    leer = file_object.read()
    print(leer.rstrip())