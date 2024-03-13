# Inclua um método no programa anterior que solicite
# o código do veículo e permita alterar os atributos do 
# campo PLACA e ANO no arquivo VEICULOS.TXT. 
# Utilize a busca sequencial p/ localizar o código

import os

def buscar_veiculo_por_codigo(codigo, registros):
    for idx, registro in enumerate(registros):
        if registro[:3] == codigo:
            return idx
    return -1

diretorio_atual = os.path.dirname(os.path.abspath(__file__))

caminho_veiculos = os.path.join(diretorio_atual, "VEICULOS.TXT")

with open(caminho_veiculos, "r") as arquivo:
    registros = arquivo.readlines()

codigo_busca = input("Digite o código do veículo que deseja alterar: ")

indice = buscar_veiculo_por_codigo(codigo_busca, registros)

if indice != -1:
    nova_placa = input("Digite a nova placa: ")
    novo_ano = input("Digite o novo ano: ")

    novo_registro = codigo_busca.ljust(3) + nova_placa.ljust(7) + novo_ano + '\n'
    registros[indice] = novo_registro

    with open(caminho_veiculos, "w") as arquivo:
        arquivo.writelines(registros)
    print("Veículo atualizado com sucesso!")
else:
    print("Veículo não encontrado.")
