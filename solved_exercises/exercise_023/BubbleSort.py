# Modifique para:

# - Ordenar uma sequência de 3.000, 10.000 e 50.000 elementos de valores variando entre 0 e 100.000
# - Utilize um contador (timer) para mostrar o tempo gasto (médio) na ordenação de cada uma das sequências acima, para cada algoritmo

import random
import time

def BubbleSort(lista_quantidade_elementos):
    tempo_armazenado = []
    
    for worth in lista_quantidade_elementos:
        # Gera um array não ordenado de 100000 elementos
        vetor = [round((random.random() * 100000)) for i in range(worth)]

        # Mostra o array não ordenado
        print(f"\n----------- vetor desordenado de {worth} elementos -----------")
        print(", ".join(map(str, vetor)))

        # Início do tempo gasto
        inicial = time.time()

        # Ordena o array usando bubble sort
        n = len(vetor)
        t = 1
        while t == 1:
            t = 0
            for i in range(n-1):
                if vetor[i] > vetor[i+1]:
                    t = 1
                    vetor[i], vetor[i+1] = vetor[i+1], vetor[i]

        # Final do tempo gasto
        final = time.time()
        tempo_gasto = final - inicial
        tempo_armazenado.append(tempo_gasto)

        # Mostra o array ordenado
        print(f"\n----------- vetor ordenado de {worth} elementos --------------")
        print(", ".join(map(str, vetor)))
        
    for index, worth2 in enumerate(tempo_armazenado):
        print(f'\n\033[33m{lista_quantidade_elementos[index]} elementos\033[m com tempo gasto de \033[33m{worth2} segundos\033[m')

quantidade_elementos = (3000, 10000, 50000)
BubbleSort(quantidade_elementos)
