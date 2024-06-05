# Modifique para:

# - Ordenar uma sequência de 3.000, 10.000 e 50.000 elementos de valores variando entre 0 e 100.000
# - Utilize um contador (timer) para mostrar o tempo gasto (médio) na ordenação de cada uma das sequências acima, para cada algoritmo.

import random

def selection_sort(arr):
    for i in range(len(arr)):
        index_min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[index_min]:
                index_min = j
        if index_min != i:
            arr[index_min], arr[i] = arr[i], arr[index_min]

# Generate an unsorted vector of 100 elements
vetor = [round(random.random() * 1000) for i in range(100)]

# Print the unsorted vector
print("------------ unsorted vector -----------")
print(",".join(map(str, vetor)))

selection_sort(vetor)

# Print the sorted vector
print("\n----------- sorted vector --------------")
print(",".join(map(str, vetor)))
