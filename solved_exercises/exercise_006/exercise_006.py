# Implemente um programa que leia e mostre na tela todos os registros do arquivo VEICULOS.TXT, na 
# seguinte ordem: CÓDIGO, PLACA e ANO

# 001MFL14292003
# 002ALO89232005
# 003LXM68211997
# 004MGW19772011
# 005BGY43442001
# 006KMJ73411985

import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))

caminho_veiculos = os.path.join(diretorio_atual, "VEICULOS.TXT")

with open(caminho_veiculos, "r") as arquivo:
    registros = arquivo.readlines()

for registro in registros:
    codigo = registro[:3]
    placa = registro[3:10]
    ano = registro[10:].strip()
    print(f"CÓDIGO: {codigo}, PLACA: {placa}, ANO: {ano}")
