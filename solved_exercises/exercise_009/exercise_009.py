# Inclua um novo método no programa anterior que 
# exclua um registro com um determinado código (por 
# exemplo, CODIGO = 004). Utilize a busca binária p/ 
# localizar o código do registro a ser excluído

import os

def excluir_registro(codigo, arquivo):
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))

    caminho_arquivo = os.path.join(diretorio_atual, arquivo)

    registros = []
    with open(caminho_arquivo, "r") as f:
        registros = f.readlines()

    inicio = 0
    fim = len(registros) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        registro_atual = registros[meio][:3]
        if registro_atual == codigo:
            del registros[meio]
            print(f"Registro com código {codigo} excluído com sucesso!")
            with open(caminho_arquivo, "w") as f:
                f.writelines(registros)
            return
        elif registro_atual < codigo:
            inicio = meio + 1
        else:
            fim = meio - 1
    print(f"Registro com código {codigo} não encontrado.")

codigo_para_excluir = input("Digite o código do registro que deseja excluir: ")

excluir_registro(codigo_para_excluir, "VEICULOS.TXT")
