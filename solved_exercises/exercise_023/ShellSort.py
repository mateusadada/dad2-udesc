# Modifique para:

# - Ordenar uma sequência de 3.000, 10.000 e 50.000 elementos de valores variando entre 0 e 100.000
# - Utilize um contador (timer) para mostrar o tempo gasto (médio) na ordenação de cada uma das sequências acima, para cada algoritmo

import random
import time

def shell_sort(array):
    n = len(array)
    h = 1
    while h <= n // 3:
        h = h * 3 + 1

    while h > 0:
        for outer in range(h, n):
            temp = array[outer]
            inner = outer
            while inner > h - 1 and array[inner - h] >= temp:
                array[inner] = array[inner - h]
                inner -= h
            array[inner] = temp
        h = (h - 1) // 3

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

    # Ordena o array usando shell sort
    shell_sort(vetor)

    # Final do tempo gasto
    final = time.time()
    tempo_gasto = final - inicial
    tempo_armazenado.append(tempo_gasto)

    # Mostra o array ordenado
    print(f"\n----------- sorted vetor de {worth} elementos --------------")
    print(", ".join(map(str, vetor)))

for index, worth2 in enumerate(tempo_armazenado):
    print(f'\n\033[33m{quantidade_elementos[index]} elementos\033[m com tempo gasto de \033[33m{worth2} segundos\033[m')
