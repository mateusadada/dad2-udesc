# Modifique para:
# Ordenar uma sequência de 10.000.000 (dez milhões) de elementos variando entre 0 e 20.000.000 (20 milhões).
# Utilize um contador (timer) para mostrar o tempo gasto na ordenação com cada algoritmo.

import time
import random

def count_sort(input_array):
	# Finding the maximum element of input_array.
	M = max(input_array)

	# Initializing count_array with 0
	count_array = [0] * (M + 1)

	# Mapping each element of input_array as an index of count_array
	for num in input_array:
		count_array[num] += 1

	# Calculating prefix sum at every index of count_array
	for i in range(1, M + 1):
		count_array[i] += count_array[i - 1]

	# Creating output_array from count_array
	output_array = [0] * len(input_array)

	for i in range(len(input_array) - 1, -1, -1):
		output_array[count_array[input_array[i]] - 1] = input_array[i]
		count_array[input_array[i]] -= 1

	return output_array

# Driver code
if __name__ == "__main__":
	# Input array
	input_array = [round((random.random() * 20000000)) for i in range(10000000)]

	inicial = time.time()

	# Output array
	output_array = count_sort(input_array)

	final = time.time()
	tempo_gasto = final - inicial

	for num in output_array:
		print(num, end=" ")

	print(f'\n\033[33m10.000.000 elementos\033[m com tempo gasto de \033[33m{tempo_gasto} segundos\033[m')
