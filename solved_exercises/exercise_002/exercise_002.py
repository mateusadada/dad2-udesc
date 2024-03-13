# cria o arquivo e adicione frases
arquivo = open('exercise_002/frases.txt', 'w')
arquivo.write('Estudando Python.')
arquivo.write('\nProgramando em Python.')
arquivo.write('\nManipulacao de arquivos.')

# retorna linhas que possuem a palavra Python
arquivo = open('exercise_002/frases.txt', 'r')
for index, value in enumerate(arquivo):
    if 'Python' in value:
        print(f'Linha {index + 1} - {value}', end='')

# retorna as linhas a partir de um critério
criterio = str(input('\nDeseja procurar qual palavra específica? '))
arquivo = open('exercise_002/frases.txt', 'r')
for index, value in enumerate(arquivo):
    if criterio in value:
        print(f'Linha {index + 1} - {value}', end='')
