# Crie um arquivo chamado “dados.txt” e, como conteúdo, salve 
# o seu nome no arquivo; depois faça a leitura do arquivo para 
# uma variável e também na tela; utilize read() e readline()

# Agora acrescente a data de nascimento, cidade que nasceu e 
# sua idade (em linhas separadas no arquivo); depois faça a 
# leitura do arquivo novamente com readlines()

# Ainda utilizando o arquivo “dados.txt”, leia o que está dentro do 
# arquivo, mas agora utilizando um laço de repetição e 
# readlines(), apresentando o número das linhas a cada iteração.

import os

diretorio_atual = os.path.dirname(__file__)

caminho_arquivo = os.path.join(diretorio_atual, "dados.txt")

# Escrevendo no arquivo dados.txt
with open(caminho_arquivo, "w") as arquivo:
    arquivo.write("Nome: Mateus Adada\n")

# Lendo o arquivo e imprimindo o conteúdo utilizando read()
with open(caminho_arquivo, "r") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo lido com read():", conteudo)

with open(caminho_arquivo, "a") as arquivo:
    arquivo.write("Data de nascimento: 10/08/2001\n")
    arquivo.write("Cidade: Sao Bento do Sul\n")
    arquivo.write("Idade: 22\n")

with open(caminho_arquivo, "r") as arquivo:
    linhas = arquivo.readlines()
    print("\nConteúdo lido com readlines():")
    for linha in linhas:
        print(linha.strip())

with open(caminho_arquivo, "r") as arquivo:
    print("\nConteúdo lido com readlines() e laço de repetição:")
    numero_linha = 1
    for linha in arquivo.readlines():
        print("Linha", numero_linha, "-", linha.strip())
        numero_linha += 1
