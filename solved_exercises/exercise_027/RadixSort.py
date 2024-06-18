# Modifique para:
# Ordenar uma sequência de 10.000.000 (dez milhões) de elementos variando entre 0 e 20.000.000 (20 milhões).
# Utilize um contador (timer) para mostrar o tempo gasto na ordenação com cada algoritmo.

import time
import random

# Python program for implementation of Radix Sort
# A function to do counting sort of arr[] according to
# the digit represented by exp.

def countingSort(arr, exp1):

    n = len(arr)

    # The output array elements that will have sorted arr
    output = [0] * (n)

    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]

# Method to do Radix Sort


def radixSort(arr):

    # Find the maximum number to know number of digits
    max1 = max(arr)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp >= 1:
        countingSort(arr, exp)
        exp *= 10


# Driver code
arr = [round((random.random() * 20000000)) for i in range(10000000)]

# Início do tempo gasto
inicial = time.time()

# Function Call
radixSort(arr)

# Final do tempo gasto
final = time.time()
tempo_gasto = final - inicial

for i in range(len(arr)):
    print(arr[i], end=" ")

print(f'\n\033[33m10.000.000 elementos\033[m com tempo gasto de \033[33m{tempo_gasto} segundos\033[m')
