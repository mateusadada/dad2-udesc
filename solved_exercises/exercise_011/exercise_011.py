# Suponha que seja dado o seguinte conjunto de chaves a serem inseridas em uma tabela de dispersão com 11 posições:
# 113, 117, 97, 100, 114, 108, 116, 105 e 99. Apresente o conteúdo da tabela depois de todas as chaves serem inseridas
# com sondagem linear.

def hash(chave, tamanho):
    return chave % tamanho

def inserir_tabela(tabela, chave):
    tamanho = len(tabela)
    indice = hash(chave, tamanho)
    while tabela[indice] is not None:
        indice = (indice + 1) % tamanho
    tabela[indice] = chave

chaves = [113, 117, 97, 100, 114, 108, 116, 105, 99]

tamanho_tabela = 11

tabela_dispersao = [None] * tamanho_tabela

for chave in chaves:
    inserir_tabela(tabela_dispersao, chave)

for i, elemento in enumerate(tabela_dispersao):
    print(f'Posição {i}: {elemento}')
