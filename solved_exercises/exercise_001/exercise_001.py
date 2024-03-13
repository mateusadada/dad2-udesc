# Dado um arquivo sequencial, com registros de tamanho fixo, contendo 
# números de CPF (11 bytes) seguidos de datas de nascimento (8 bytes), 
# escreva uma fórmula possível para acessar o 3º registro deste arquivo:
# Obs.: utilizar uma variável do tipo string em substituição ao arquivo

registros = "021478345231402198408189472328090419790164437663021101996091789834401805198616773422110231220010017325545008091968040901876902511198100789089990090919991753135151210101987"

tamanho_do_registro = 19

posicao_inicial = (tamanho_do_registro * 2) + 1

terceiro_registro = registros[posicao_inicial:posicao_inicial + tamanho_do_registro]

cpf = terceiro_registro[:11]
data_nascimento = terceiro_registro[11:]

print("CPF:", cpf)
print("Data de nascimento:", data_nascimento)
