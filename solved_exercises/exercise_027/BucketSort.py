# Modifique para:
# Ordenar uma sequência de 10.000.000 (dez milhões) de elementos variando entre 0 e 20.000.000 (20 milhões).
# Utilize um contador (timer) para mostrar o tempo gasto na ordenação com cada algoritmo.

# algoritmo insertion sort para ordenação de recipientes individuais
def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key

def bucket_sort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)] # cria uma lista de listas de tamanho n

    # coloca cada elemento em um recipiente diferente conforme o valor de bi
    for num in arr:
        bi = int(n * num)
        buckets[bi].append(num)

    # ordena cada recipiente utilizando o insertion sort
    for bucket in buckets:
        insertion_sort(bucket)

    # concatna todos os recipientes novamente no array
    index = 0
    for bucket in buckets:
        for num in bucket:
            arr[index] = num
            index += 1

# funciona para ordenar elementos num intervalo 0..1
arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
#OldRange = (OldMax - OldMin) # OldRange = (9999999999 - 0)
#NewRange = (NewMax - NewMin)
#NewValue = (((OldValue - OldMin) * NewRange) / OldRange) + NewMin
bucket_sort(arr)
print("Sorted array is:")
print(" ".join(map(str, arr)))
