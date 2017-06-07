#Insertion Sort

import random
import timeit

def cria_vetor(num):
    lista = []
    for i in range(num):
        x = random.randint(1,100)
        lista.append(x)
    return lista

def InsertionSort(num):
    lista = cria_vetor(num)
    print(lista)
    for i in range(1,num):
        if lista[i] < lista[i-1]:
            aux = lista[i-1]
            lista[i-1] = lista[i]
            lista[i] = aux
        while (i-1) != 0:
            i = i-1
            if lista[i] < lista[i - 1]:
                aux = lista[i - 1]
                lista[i - 1] = lista[i]
                lista[i] = aux
    return lista

num = int(input("Quantos numeros deseja no vetor?" ))
inicio = timeit.default_timer()
print(InsertionSort(num))
fim = timeit.default_timer()
print("Duração: %f" % (fim - inicio))
