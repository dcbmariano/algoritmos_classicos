# Retorna uma lista embaralhada de forma uniformemente aleatória
# Autor: Diego Mariano
# O código a seguir foi adaptado da função mergesort modificada
# Data: 26/06/2023

import random

def merge(lista, e, m, d):
    n1 = m - e + 1
    n2 = d - m
 
    # cria arrays temporários
    E = [0] * (n1)
    D = [0] * (n2)
 
    # Copia os dados para os arrays temporários E[] e D[]
    for i in range(0, n1):
        E[i] = lista[e + i]
 
    for j in range(0, n2):
        D[j] = lista[m + 1 + j]
 
    # Mescla os arrays temporários na lista[e..d]
    i = 0     # Índice inicial do primeiro subarray
    j = 0     # Índice inicial do segundo subarray
    k = e     # Índice inicial do subarray mesclado
    

    while i < n1 and j < n2:
        #if E[i] <= D[j]: # ordena pelo menor valor
        if random.random() < 0.5:  # aleatório
            lista[k] = E[i]
            i += 1
        else:
            lista[k] = D[j]
            j += 1
        k += 1
 
    # Copia os elementos remanescentes de E[], se houver algum
    while i < n1:
        lista[k] = E[i]
        i += 1
        k += 1
 
    # Copia os elementos remanescentes de D[], se houver algum
    while j < n2:
        lista[k] = D[j]
        j += 1
        k += 1
 
# e é para o índice esquerdo e d é o índice direito do sub-array da lista a ser classificado
 
 
def mergeSort(lista, e, d):
    if len(lista) == 1:
        return lista[0]

    if e < d:
        m = e+(d-e)//2
 
        # ordena a primeira e segunda metade
        mergeSort(lista, e, m)
        mergeSort(lista, m+1, d)
        merge(lista, e, m, d)
 

if __name__ == "__main__":

    # Teste
    lista = [2, 3, 4, 5, 6, 7]
    n = len(lista)

    print("Array de entrada:")
    for i in range(n):
        print("%d" % lista[i], end=" ")
     
    mergeSort(lista, 0, n-1)
    print("\n\nArray embaralhado:")

    for i in range(n):
        print("%d" % lista[i],end=" ")


print("\n\nExecutado com sucesso.")

# RESULTADO EXEMPLO:
# Array de entrada:
# 2 3 4 5 6 7 

# Array embaralhado:
# 7 6 2 3 4 5 

# Executado com sucesso.