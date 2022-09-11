#function 
def optionNum(num):
    if ( num == 1):
        print ("uno")
    elif (num == 2):
        print ("dos")
    elif (num ==3):
        print ("tres")
    else:
        print ("Error")

#main algorithm
option = "s"

while ( option == "s" ) :
    num = int(input("Ingrese un numero entre el 1 y 3: "))
    optionNum(num)

    option = input("Desea continuar? (s/n)")
    
