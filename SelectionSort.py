#Selection Sort

import random
import timeit

def cria_vetor(num):
    lista = []
    for i in range(num):
        x = random.randint(1,100)
        lista.append(x)
    return lista

def SelectionSort (num):
    lista = cria_vetor(num)
    print(lista)
    for i in range(len(lista)):
        menor = i
        for j in range(i, len(lista)):
            if lista[j] < lista[menor]:
                menor = j
        if menor != i:
            aux = lista[i]
            lista[i] = lista[menor]
            lista[menor] = aux
    return lista

num = int(input("Quantos numeros deseja no vetor?" ))
inicio = timeit.default_timer()
print(SelectionSort(num))
fim = timeit.default_timer()
print("Duração: %f" % (fim - inicio))
