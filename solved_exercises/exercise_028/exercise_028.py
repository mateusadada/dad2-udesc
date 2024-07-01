# Utilize o TimSort nativo do Python para ordenar uma lista (lista.sort()) de 10 milhões de elementos e conte o tempo.

import time
import random

lista = [round((random.random() * 20000000)) for i in range(10000000)]

inicial = time.time()

lista.sort()

print('Lista ordenada')
print(lista)

final = time.time()
tempo_gasto = final - inicial

print(f'\n\033[33m10.000.000 elementos\033[m com tempo gasto de \033[33m{tempo_gasto} segundos\033[m')
