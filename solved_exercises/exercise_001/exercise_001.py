# criar e salvar o nome
arquivo = open('exercise_001/dados.txt', 'w')
arquivo.write('Mateus Adada')

# abrir e mostrar tudo
arquivo = open('exercise_001/dados.txt', 'r')
print(arquivo.read())

# mostrar uma linha
arquivo = open('exercise_001/dados.txt', 'r')
print(arquivo.readline())

# adicionar data de nascimento, cidade e idade em linhas diferentes
arquivo = open('exercise_001/dados.txt', 'a')
arquivo.write('\n10/08/2001')
arquivo.write('\nSao Bento do Sul')
arquivo.write('\n22 anos')

# mostrar várias linhas
arquivo = open('exercise_001/dados.txt', 'r')
print(arquivo.readlines())

# mostrar todas as linhas usando for
print()
arquivo = open('exercise_001/dados.txt', 'r')
for index, value in enumerate(arquivo):
    print(f'Linha {index + 1} e valor {value}', end='')
