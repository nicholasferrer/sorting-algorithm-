#Bubble Sort
import random
import timeit
def cria_vetor(num):
    lista = []
    for i in range(num):
        x = random.randint(1,100)
        lista.append(x)
    return lista

def BubbleSort(num):
    lista = cria_vetor(num)
    print(lista)
    for i in range(len(lista)):
        for j in range(len(lista)- i - 1):
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
    return lista

num = int(input("Quantos numeros deseja no vetor?" ))
inicio = timeit.default_timer()
print(BubbleSort(num))
fim = timeit.default_timer()
print("Duração: %f" % (fim - inicio))
