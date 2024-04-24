# Utilizando como chave a palavra “SEGURANCA”, qual é o texto original da seguinte cifra de Playfair?

# FDUSFPFACNMENMDSUROSDOME
# VFNINATNSNGVGFRV

# Resposta com espaços e acentuação: "LÁGRIMAS NÃO SÃO ARGUMENTOS MACHADO DE ASSIS"

# Feito via códigos adaptados da internet e também com uma prova real no Excel.

from playfair import Playfair

texto_decifrado = input('Texto a ser decifrado: ')
senha = input('Senha: ')

cifra = Playfair()
print(cifra.descriptografar(texto_decifrado, senha))
