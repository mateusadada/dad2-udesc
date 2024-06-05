# Modifique para:

# - Ordenar uma sequência de 3.000, 10.000 e 50.000 elementos de valores variando entre 0 e 100.000
# - Utilize um contador (timer) para mostrar o tempo gasto (médio) na ordenação de cada uma das sequências acima, para cada algoritmo.

import random

def merge_sort(array):
    """
    Recursively divides the array, sorts the subarrays, and merges them back together.
    """
    if len(array) > 1:
        middle1 = len(array) // 2
        middle2 = middle1 + 1

        # Divide the array in half and recursively sort each half
        left_half = array[:middle1]
        right_half = array[middle2:]
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves back into the original array
        merge(array, left_half, right_half)

def merge(array, left_half, right_half):
    """
    Merges two sorted subarrays back into the original array.
    """
    left_index = 0
    right_index = 0
    combined_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] <= right_half[right_index]:
            array[combined_index] = left_half[left_index]
            left_index += 1
        else:
            array[combined_index] = right_half[right_index]
            right_index += 1
        combined_index += 1

    # Copy any remaining elements from the left or right half
    while left_index < len(left_half):
        array[combined_index] = left_half[left_index]
        left_index += 1
        combined_index += 1

    while right_index < len(right_half):
        array[combined_index] = right_half[right_index]
        right_index += 1
        combined_index += 1

# Generate an unsorted array of 100 elements
vector = [round((i + 1) * random.random() * 1000) for i in range(100)]

# Print the unsorted array
print("------------ Unsorted Vector -----------")
print(",".join(map(str, vector)))

# Sort the array using merge sort
merge_sort(vector)

# Print the sorted array
print("\n----------- Sorted Vector --------------")
print(",".join(map(str, vector)))
