# Criar um programa que carregue um arquivo chamado “contatos.txt”, contendo nomes e números de contatos tal
# como os dados a seguir:

# Nome:Celular
# Guilherme:(41) 9 9123-4567
# Rafaela:(47) 9 2002-2222
# Eduardo:(48) 9 9876-5432
# Mercado:(47) 3003-1010

# Inclua um laço de repetição para buscar por um determinado 
# contato, exibindo na tela apenas o número deste contato. Para 
# sair do laço utilize “sair”

import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))

caminho_contatos = os.path.join(diretorio_atual, "contatos.txt")

with open(caminho_contatos, "r") as arquivo:
    linhas = arquivo.readlines()

contatos = {}

for linha in linhas[1:]:
    nome, telefone = linha.strip().split(":")
    # adicionando o contato ao dicionário
    contatos[nome.strip()] = telefone.strip()

while True:
    nome_busca = input("Digite o nome do contato (ou 'sair' para encerrar): ")
    if nome_busca.lower() == 'sair':
        break
    elif nome_busca in contatos:
        print(f"Número do contato {nome_busca}: {contatos[nome_busca]}\n")
    else:
        print(f"O contato {nome_busca} não foi encontrado.\n")
