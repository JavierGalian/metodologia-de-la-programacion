from random import randint

def loadList():
    listNumAleatorios = []
    n=int(input("Cantidad de aleatorios: "))
    for i in range(n):
        listNumAleatorios.append(randint(0,1000))
    return listNumAleatorios

def shell(lst):
    n = len(lst)
    gap = n // 2 # … 112,48,21,7,5,1
    while gap > 0:
        for i in range(gap, n):
            tmp = lst[i]
            j = i
            while j >= gap and lst[j - gap] > tmp:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = tmp
        gap = gap // 2
    return lst

# ----- main -----
lista_1 = loadList()
print('lista numero 1: ', lista_1)
lista_1Ordenada = shell(lista_1)
lista_2 = loadList()
print('lista numero 2: ', lista_2)
lista_2Ordenada = shell(lista_2)

listasUnidas = lista_1+lista_2
listasUnidas = shell(listasUnidas)
print('listas unidas ordenada: ', listasUnidas)