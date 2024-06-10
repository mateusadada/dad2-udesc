# Modifique para ordenar uma sequência de 1 milhão de elementos (variando entre 0 e 2 milhões)
# e mostrar o tempo médio gasto com a ordenação.

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

# Gera um array não ordenado de 1000000 elementos
vetor = [round((random.random() * 2000000)) for i in range(1000000)]

# Print the unsorted array
print("\n------------ unsorted array de 1000000 elementos -----------")
print(", ".join(map(str, vetor)))

# Início do tempo gasto
inicial = time.time()

# Ordena o array usando shell sort
heap_sort(vetor)

# Final do tempo gasto
final = time.time()
tempo_gasto = final - inicial

# Mostra o array ordenado
print("\n----------- sorted vetor de 1000000 elementos --------------")
print(", ".join(map(str, vetor)))

print(f'\n\033[33m1000000 elementos\033[m com tempo gasto de \033[33m{tempo_gasto} segundos\033[m')
