# Modifique para:

# - Ordenar uma sequência de 3.000, 10.000 e 50.000 elementos de valores variando entre 0 e 100.000
# - Utilize um contador (timer) para mostrar o tempo gasto (médio) na ordenação de cada uma das sequências acima, para cada algoritmo.

import random
import time

def selection_sort(arr):
    for i in range(len(arr)):
        index_min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[index_min]:
                index_min = j
        if index_min != i:
            arr[index_min], arr[i] = arr[i], arr[index_min]

quantidade_elementos = (3000, 10000, 50000)
tempo_armazenado = []

for worth in quantidade_elementos:
    # Gera um array não ordenado de 100000 elementos
    vetor = [round((random.random() * 100000)) for i in range(worth)]
    
    # Print the unsorted array
    print(f"\n------------ unsorted array de {worth} elementos -----------")
    print(", ".join(map(str, vetor)))

    # Início do tempo gasto
    inicial = time.time()
    
    selection_sort(vetor)
    
    # Final do tempo gasto
    final = time.time()
    tempo_gasto = final - inicial
    tempo_armazenado.append(tempo_gasto)

    # Mostra o array ordenado
    print(f"\n----------- sorted vetor de {worth} elementos --------------")
    print(", ".join(map(str, vetor)))

for index, worth2 in enumerate(tempo_armazenado):
    print(f'\n\033[33m{quantidade_elementos[index]} elementos\033[m com tempo gasto de \033[33m{worth2} segundos\033[m')
