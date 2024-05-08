# Desafio: escreva um programa que decifre uma senha de 8 
# caracteres. Esta senha possui apenas os seguintes caracteres:
# 1 2 3 a e i o u

# A hash MD5 que representa a senha é: bc9b5d33aca080fda8b85032bc0ed1ea

import hashlib
from itertools import product

caracteres = ['1', '2', '3', 'a', 'e', 'i', 'o', 'u']
hash_final = 'bc9b5d33aca080fda8b85032bc0ed1ea'

total_combinacao = product(caracteres, repeat=8)

for combinacao in total_combinacao:
    senha = ''.join(combinacao)
    
    senha_hash = hashlib.md5(senha.encode()).hexdigest()
    
    if senha_hash == hash_final:
        print(f"Senha encontrada: {senha}")
        break
