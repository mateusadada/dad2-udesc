# Modifique para:

# - Ordenar uma sequência de 3.000, 10.000 e 50.000 elementos de valores variando entre 0 e 100.000
# - Utilize um contador (timer) para mostrar o tempo gasto (médio) na ordenação de cada uma das sequências acima, para cada algoritmo

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

quantidade_elementos = (3000, 10000, 50000)
tempo_armazenado = []

for worth in quantidade_elementos:
    # Gera um array não ordenado de 100000 elementos
    vetor = [round((random.random() * 100000)) for i in range(worth)]

    # Mostra o array não ordenado
    print(f"\n------------ disordered vetor de {worth} elementos -----------")
    print(", ".join(map(str, vetor)))

    # Início do tempo gasto
    inicial = time.time()
    
    # Ordena o array usando quick sort
    sorted_vetor = quick_sort(vetor)
    
    # Final do tempo gasto
    final = time.time()
    tempo_gasto = final - inicial
    tempo_armazenado.append(tempo_gasto)

    # Mostra o array ordenado
    print(f"\n----------- sorted vetor de {worth} elementos --------------")
    print(", ".join(map(str, sorted_vetor)))
    
for index, worth2 in enumerate(tempo_armazenado):
    print(f'\n\033[33m{quantidade_elementos[index]} elementos\033[m com tempo gasto de \033[33m{worth2} segundos\033[m')
