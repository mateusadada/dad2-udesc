import random
import time

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

quantidade_elementos = (30, 10000, 50000)
tempo_armazenado = []

for worth in quantidade_elementos:
    # Gera um array não ordenado de `worth` elementos
    vetor = [round((random.random() * 100000)) for _ in range(worth)]
    
    # Print the unsorted array
    print(f"\n------------ unsorted array de {worth} elementos -----------")
    print(", ".join(map(str, vetor)))

    # Início do tempo gasto
    inicial = time.time()
    
    merge_sort(vetor)
    
    # Final do tempo gasto
    final = time.time()
    tempo_gasto = final - inicial
    tempo_armazenado.append(tempo_gasto)

    # Mostra o array ordenado
    print(f"\n----------- sorted vetor de {worth} elementos --------------")
    print(", ".join(map(str, vetor)))

for index, worth2 in enumerate(tempo_armazenado):
    print(f'\n\033[33m{quantidade_elementos[index]} elementos\033[m com tempo gasto de \033[33m{worth2} segundos\033[m')
