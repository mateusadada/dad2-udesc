# Inclua um método no programa anterior que permita inserir um novo registro com CODIGO, PLACA e
# ANO no final do arquivo VEICULOS.TXT

import os

def adicionar_registro(codigo, placa, ano):
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))

    caminho_veiculos = os.path.join(diretorio_atual, "VEICULOS.TXT")

    novo_registro = f"{codigo}{placa}{ano}\n"

    with open(caminho_veiculos, "a") as arquivo:
        arquivo.write(novo_registro)

codigo = input("Digite o código do veículo: ")
placa = input("Digite a placa do veículo: ")
ano = input("Digite o ano do veículo: ")

adicionar_registro(codigo, placa, ano)

print("Novo registro adicionado com sucesso!")
