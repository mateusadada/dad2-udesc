# Criar um novo arquivo chamado “frases.txt” com a seguintes 
# frases: “Estudando Python.”, “Programando em Python.” e
# “Manipulação de arquivos.” 

# Criar um programa que retorne somente as linhas que 
# possuem a palavra Python

# Desenvolver um método que retorne somente as linhas que 
# contém uma palavra específica a critério do usuário

import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))

caminho_frases = os.path.join(diretorio_atual, "frases.txt")

with open(caminho_frases, "w") as arquivo:
    arquivo.write("Estudando Python.\n")
    arquivo.write("Programando em Python.\n")
    arquivo.write("Manipulacao de arquivos.\n")

def encontrar_linhas_com_palavra(arquivo, palavra):
    linhas_encontradas = []
    with open(arquivo, "r") as arquivo:
        for linha in arquivo:
            if palavra.lower() in linha.lower():
                linhas_encontradas.append(linha.strip())
    return linhas_encontradas

linhas_com_python = encontrar_linhas_com_palavra(caminho_frases, "Python")
print("Linhas contendo a palavra 'Python':")
for linha in linhas_com_python:
    print(linha)

def encontrar_linhas_com_palavra_especifica(arquivo, palavra):
    linhas_encontradas = []
    with open(arquivo, "r") as arquivo:
        for linha in arquivo:
            if palavra.lower() in linha.lower():
                linhas_encontradas.append(linha.strip())
    return linhas_encontradas

palavra = input("Insira a palavra para buscar no arquivo: ")

linhas_com_palavra = encontrar_linhas_com_palavra_especifica(caminho_frases, palavra)
print(f"Linhas contendo a palavra '{palavra}':")
for linha in linhas_com_palavra:
    print(linha)
