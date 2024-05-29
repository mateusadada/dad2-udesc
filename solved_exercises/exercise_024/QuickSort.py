# Modifique para ordenar uma sequência de 1 milhão de elementos (variando entre 0 e 2 milhões)
# e mostrar o tempo médio gasto com a ordenação

import random
import time

# Classifica recursivamente o array fornecido usando o algoritmo QuickSort.
def quick_sort(array):
    def _quick_sort(arr, start, end):
        if end - start >= 1:
            pivot = arr[start]
            i = start
            k = end
            while k > i:
                while arr[i] <= pivot and i <= end and k > i:
                    i += 1
                while arr[k] > pivot and k >= start and k >= i:
                    k -= 1
                if k > i:
                    arr[i], arr[k] = arr[k], arr[i]
            arr[start], arr[k] = arr[k], arr[start]
            _quick_sort(arr, start, k - 1)
            _quick_sort(arr, k + 1, end)
        else:
            return

    _quick_sort(array, 0, len(array) - 1)
    return array

# Gera um array não ordenado de 1000000 elementos
vetor = [round((random.random() * 2000000)) for i in range(1000000)]

# Mostra o array não ordenado
print("\n------------ disordered vetor de 1000000 elementos -----------")
print(", ".join(map(str, vetor)))

# Início do tempo gasto
inicial = time.time()

# Ordena o array usando quick sort
sorted_vetor = quick_sort(vetor)

# Final do tempo gasto
final = time.time()
tempo_gasto = final - inicial

# Mostra o array ordenado
print("\n----------- sorted vetor de 1000000 elementos --------------")
print(", ".join(map(str, sorted_vetor)))

print(f'\n\033[33m1000000 elementos\033[m com tempo gasto de \033[33m{tempo_gasto} segundos\033[m')
