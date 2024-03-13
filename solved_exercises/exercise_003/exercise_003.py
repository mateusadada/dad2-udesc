while True:
    nome = str(input('\nDigite um nome para pesquisar: '))

    arquivo = open('exercise_003/contatos.txt', 'r')
    for index, value in enumerate(arquivo):
        if nome in value:
            print(f'Telefone da {nome}: {value[len(nome) + 1:]}')

    sair = str(min(input('Para encerrar digite sair: ')).strip())
    if sair == 'sair':
        break
