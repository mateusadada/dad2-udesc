# Modifique para ordenar uma sequência de 1 milhão de elementos (variando entre 0 e 2 milhões)
# e mostrar o tempo médio gasto com a ordenação

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

# Gera um array não ordenado de 1000000 elementos
vetor = [round((random.random() * 2000000)) for i in range(1000000)]

# Print the unsorted array
print("\n------------ unsorted array de 1000000 elementos -----------")
print(", ".join(map(str, vetor)))

# Início do tempo gasto
inicial = time.time()

# Ordena o array usando shell sort
shell_sort(vetor)

# Final do tempo gasto
final = time.time()
tempo_gasto = final - inicial

# Mostra o array ordenado
print("\n----------- sorted vetor de 1000000 elementos --------------")
print(", ".join(map(str, vetor)))

print(f'\n\033[33m1000000 elementos\033[m com tempo gasto de \033[33m{tempo_gasto} segundos\033[m')
