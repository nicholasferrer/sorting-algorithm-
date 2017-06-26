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
    for i in range(1, len(lista)):
        teste = True
        pos = i
        for j in range(i):  # Acha a posição do primeiro elemento menor que o elemento atual
            if lista[i] < lista[j] and teste:
                pos = j
                teste = False
        aux = lista[i]  # Salva o valor atual
        for j in range(i, pos, -1):  # Passa todos os elementos entre 'pos' e 'i' uma casa pra frente
            lista[j] = lista[j - 1]
        lista[pos] = aux                # Bota o valor atual na posição certa

    return lista

num = int(input("Quantos numeros deseja no vetor?" ))
inicio = timeit.default_timer()
print(InsertionSort(num))
fim = timeit.default_timer()
print("Duração: %f" % (fim - inicio))
