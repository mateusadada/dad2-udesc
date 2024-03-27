# Desenvolva um programa em Python para inserir registros de alunos em uma estrutura de dados do tipo Tabela Hash.
# Considere para cada registro a seguinte informação:

# Matrícula: <Inteiro de 5 dígitos>
# Nome: <String>
# Nota: <Float>

# Utilize o método de resto da divisão para a função de espalhamento. Não é necessário realizar o tratamento de colisões.

# Considere que inicialmente que o conteúdo de cada posição (slot) da tabela é None.

# Implemente um método de inserção dos registros e um método de mostrar todo o conteúdo da tabela. Por exemplo:

# tabela.insereHash(19191, "Eu", 10.0)
# tabela.insereHash(28282, "Fulano", 9.0)
# tabela.insereHash(37373, "Ciclano", 8.0)
# tabela.insereHash(46464, "Beltrano", 7.0)
# tabela.insereHash(11111, "Alguém", 10.0)
# tabela.mostraHash()

def hash(matricula, tamanho):
    return matricula % tamanho

def insere_hash(tabela, matricula, nome, nota):
    tamanho = len(tabela)
    posicao = hash(matricula, tamanho)
    if tabela[posicao] is None:
        tabela[posicao] = [(matricula, nome, nota)]
    else:
        tabela[posicao].append((matricula, nome, nota))

def mostra_hash(tabela):
    for i in range(len(tabela)):
        if tabela[i] is not None:
            for registro in tabela[i]:
                print(f"Matrícula: {registro[0]}, Nome: {registro[1]}, Nota: {registro[2]}")


tamanho_tabela = 10
tabela_hash = [None] * tamanho_tabela

insere_hash(tabela_hash, 19191, "Eu", 10.0)
insere_hash(tabela_hash, 28282, "Fulano", 9.0)
insere_hash(tabela_hash, 37373, "Ciclano", 8.0)
insere_hash(tabela_hash, 46464, "Beltrano", 7.0)
insere_hash(tabela_hash, 11111, "Alguém", 10.0)
mostra_hash(tabela_hash)
