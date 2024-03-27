# Implementar uma tabela hash com os métodos de sondagem linear e de sondagem quadrática.

#   Considere uma tabela de 7 posições;
#   Inicialize a tabela com None;
#   Insira os itens 14, 15, 1, 35 e 18 (nessa ordem) testando:
#       Inserção sem sondagem e exiba a tabela;
#       Inserção com sondagem linear e exiba a tabela;
#       Inserção com sondagem quadrática e exiba a tabela.

# – Descreva o que ocorre em cada tipo de inserção e verifique se todos os itens foram inseridos na tabela corretamente.

def hash_function(key, size):
    return key % size

def linear_probe(index, attempt, size):
    return (index + attempt) % size

def quadratic_probe(index, attempt, size):
    return (index + attempt**2) % size

def insert(table, key, probing_method='none'):
    size = len(table)
    index = hash_function(key, size)
    if table[index] is None:
        table[index] = key
        return True
    else:
        if probing_method == 'linear':
            attempt = 1
            while True:
                new_index = linear_probe(index, attempt, size)
                if table[new_index] is None:
                    table[new_index] = key
                    return True
                attempt += 1
        elif probing_method == 'quadratic':
            attempt = 1
            while True:
                new_index = quadratic_probe(index, attempt, size)
                if table[new_index] is None:
                    table[new_index] = key
                    return True
                attempt += 1
        else:
            print("Método de sondagem não reconhecido.")
            return False

def display_table(table):
    print("Tabela Hash:")
    for i, item in enumerate(table):
        print(f"Posição {i}: {item}")


tamanho_tabela = 7
tabela_hash = [None] * tamanho_tabela

print("Inserção sem sondagem:")
insert(tabela_hash, 14)
insert(tabela_hash, 15)
insert(tabela_hash, 1)
insert(tabela_hash, 35)
insert(tabela_hash, 18)
display_table(tabela_hash)

tabela_hash = [None] * tamanho_tabela

print("\nInserção com sondagem linear:")
insert(tabela_hash, 14, 'linear')
insert(tabela_hash, 15, 'linear')
insert(tabela_hash, 1, 'linear')
insert(tabela_hash, 35, 'linear')
insert(tabela_hash, 18, 'linear')
display_table(tabela_hash)

tabela_hash = [None] * tamanho_tabela

print("\nInserção com sondagem quadrática:")
insert(tabela_hash, 14, 'quadratic')
insert(tabela_hash, 15, 'quadratic')
insert(tabela_hash, 1, 'quadratic')
insert(tabela_hash, 35, 'quadratic')
insert(tabela_hash, 18, 'quadratic')
display_table(tabela_hash)
