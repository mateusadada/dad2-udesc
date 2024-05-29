# Modifique para:

# - Ordenar uma sequência de 3.000, 10.000 e 50.000 elementos de valores variando entre 0 e 100.000
# - Utilize um contador (timer) para mostrar o tempo gasto (médio) na ordenação de cada uma das sequências acima, para cada algoritmo

import random
import time

def insertion_sort(array):
    # Início do tempo gasto
    inicial = time.time()
    
    """Classifica o array utilizando a classificacao por insercao"""
    for next_index in range(1, len(array)):
        insert = array[next_index]  # armazena o valor no elemento atual
        move_item = next_index
        while move_item > 0 and array[move_item - 1] > insert:
            array[move_item] = array[move_item - 1]  # desloca o elemento direito um slot
            move_item -= 1
        array[move_item] = insert  # coloca o elemento inserido
        
    # Final do tempo gasto
    final = time.time()
    tempo_gasto = final - inicial
    tempo_armazenado.append(tempo_gasto)

def main(lista_quantidade_elementos):
    for worth in lista_quantidade_elementos:
        """Gera um vetor desordenado de 100000 elementos, ordena-o e imprime o resultado"""
        vetor = [round((random.random() * 100000)) for i in range(worth)]

        print(f"\n------------ vetor desordenado de {worth} elementos -----------")
        print(", ".join(map(str, vetor)))

        insertion_sort(vetor)

        print(f"\n----------- vetor ordenado de {worth} elementos --------------")
        print(", ".join(map(str, vetor)))
        
    for index, worth2 in enumerate(tempo_armazenado):
        print(f'\n\033[33m{lista_quantidade_elementos[index]} elementos\033[m com tempo gasto de \033[33m{worth2} segundos\033[m')

tempo_armazenado = []
quantidade_elementos = (3000, 10000, 50000)
main(quantidade_elementos)
