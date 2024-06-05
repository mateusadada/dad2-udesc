# Modifique para ordenar uma sequência de 1 milhão de elementos (variando entre 0 e 2 milhões)
# e mostrar o tempo médio gasto com a ordenação.

import random

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

if __name__ == "__main__":
    # Gera um array não ordenado de 100 elementos
    vector = [round(random.random() * 1000) for i in range(100)]

    # Imprime o array não ordenado
    print("------------ unsorted vector -----------")
    print(",".join(map(str, vector)))

    heap_sort(vector)

    # Imprime o array ordenado
    print("\n----------- sorted vector --------------")
    print(",".join(map(str, vector)))
