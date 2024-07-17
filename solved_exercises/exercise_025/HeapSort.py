# Modifique para:

# - Ordenar uma sequência de 3.000, 10.000 e 50.000 elementos de valores variando entre 0 e 100.000
# - Utilize um contador (timer) para mostrar o tempo gasto (médio) na ordenação de cada uma das sequências acima, para cada algoritmo.

import random
import time

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def build_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

def heap_sort(arr):
    build_heap(arr)
    n = len(arr)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

quantidade_elementos = (3000, 10000, 50000)
tempo_armazenado = []

for worth in quantidade_elementos:
    # Gera um array não ordenado de 100000 elementos
    vetor = [round((random.random() * 100000)) for i in range(worth)]
    
    # Print the unsorted array
    print(f"\n------------ unsorted array de {worth} elementos -----------")
    print(", ".join(map(str, vetor)))

    inicial = time.time()
    
    heap_sort(vetor)
    
    final = time.time()
    tempo_gasto = final - inicial
    tempo_armazenado.append(tempo_gasto)

    # Mostra o array ordenado
    print(f"\n----------- sorted vetor de {worth} elementos --------------")
    print(", ".join(map(str, vetor)))

for index, worth2 in enumerate(tempo_armazenado):
    print(f'\n\033[33m{quantidade_elementos[index]} elementos\033[m com tempo gasto de \033[33m{worth2} segundos\033[m')
