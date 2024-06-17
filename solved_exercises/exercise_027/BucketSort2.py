# Modifique para:
# Ordenar uma sequência de 10.000.000 (dez milhões) de elementos variando entre 0 e 20.000.000 (20 milhões).
# Utilize um contador (timer) para mostrar o tempo gasto na ordenação com cada algoritmo.

# ordena cada bucket individualmente com o insertion sort
def insertion_sort(bucket):
    for i in range (1, len (bucket)):
        var = bucket[i]
        j = i - 1
        while (j >= 0 and var < bucket[j]):
            bucket[j + 1] = bucket[j]
            j = j - 1
        bucket[j + 1] = var

def bucket_sort(input_list):
    # Encontrar o valor máximo na lista e usar o comprimento da lista para determinar qual valor da lista vai para qual intervalo
    max_value = max(input_list)
    size = max_value/len(input_list)

    # Criar n buckets vazios onde n é igual ao comprimento da lista de entrada
    buckets_list= []
    for x in range(len(input_list)):
        buckets_list.append([])

    # Colocar os elementos da lista em grupos diferentes com base no tamanho (size)
    for i in range(len(input_list)):
        j = int (input_list[i] / size)
        if j != len (input_list):
            buckets_list[j].append(input_list[i])
        else:
            buckets_list[len(input_list) - 1].append(input_list[i])

    # Ordenar os elementos dentro dos buckets usando o insertion sort
    for z in range(len(input_list)):
        insertion_sort(buckets_list[z])

    # Concatenar os buckets individualmente ordenados em uma única lista
    final_output = []
    for x in range(len (input_list)):
        final_output = final_output + buckets_list[x]
    return final_output

#input_list = [1.20, 0.22, 0.43, 0.36, 0.39, 0.27]
input_list = [1.2, 9000, 3, 58, 0.45, 27] # Aqui ocorre falha no bucket e apenas insertion sort faz a ordenação
print('ORIGINAL LIST:')
print(input_list)
sorted_list = bucket_sort(input_list)
print('SORTED LIST:')
print(sorted_list)
