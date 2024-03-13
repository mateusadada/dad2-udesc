# Utilizando o mesmo arquivo (string) do exercício 1, faça um 
# método que mostre na tela os registros da seguinte forma:
# Exemplo: 021.478.345-23 14/02/1984

def formatar_registro(registro):
    cpf = registro[:3] + '.' + registro[3:6] + '.' + registro[6:9] + '-' + registro[9:11]
    data_nascimento = registro[11:13] + '/' + registro[13:15] + '/' + registro[15:19]
    
    return cpf, data_nascimento

def mostrar_registros(registros):
    tamanho_do_registro = 19
    
    for i in range(0, len(registros), tamanho_do_registro):
        cpf, data_nascimento = formatar_registro(registros[i:i + tamanho_do_registro])
        print(cpf, data_nascimento)

registros = "021478345231402198408189472328090419790164437663021101996091789834401805198616773422110231220010017325545008091968040901876902511198100789089990090919991753135151210101987"

mostrar_registros(registros)
