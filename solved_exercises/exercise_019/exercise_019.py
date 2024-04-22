# Utilizando como chave a palavra “SEGURANCA”, qual é o texto original da seguinte cifra de Playfair?

# FDUSFPFACNMENMDSUROSDOME
# VFNINATNSNGVGFRV

# Resposta com espaços: lagrimas nao sao argumentos machado de assis

from playfair import Playfair

texto_decifrado = input('Texto a ser decifrado: ')
senha = input('Senha: ')

cifra = Playfair()
print(cifra.descriptografar(texto_decifrado, senha))
