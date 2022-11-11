#Estrutura de dados
fileira = []
sessao = []
menu = False

#Alimentando a matriz:
for i in range(0, 10):
    for j in range(0, 10):
        fileira.append('O')
    sessao.append(fileira[:])
    fileira.clear()

#main
while not menu:
    opcao = int(input('''Escolha uma opção:
    [ 1 ] - Mostrar layout
    [ 2 ] - Reservar cadeira
    [ 3 ] - Cancelar reserva
    [ 4 ] - Sair'''))
    if opcao == 1:
        for c, v in enumerate(sessao):
            print(f'''{c+1}{v}''')

    elif opcao == 2:
        choiceFileira = int(input('Escolha a fileira que deseja sentar: '))
        choiceCadeira = int(input('Agora escolha a cadeira que deseja reservar: '))
        #Validação do número da cadeira/número da fileira:
        while (choiceFileira < 1) or (choiceFileira > 10):
            print('O número da fileira é inválido.')
            choiceFileira = int(input('Escolha a fileira que deseja sentar: '))
        while (choiceCadeira < 1) or (choiceCadeira > 10):
            print('O número da cadeira é inválido.')
            choiceCadeira = int(input('Escolha a cadeira que deseja sentar: '))
        #Validação se a cadeira já está reservada ou não. Caso não, faz a reserva:
        if sessao[choiceFileira-1][choiceCadeira-1] == 'X':
            print('Esta cadeira já está reservada.')
        else:
            sessao[choiceFileira - 1][choiceCadeira - 1] = 'X'
            print('Cadeira reservada com sucesso!')

    elif opcao == 3:
        choiceFileira = int(input('Escolha a fileira que deseja cancelar a reserva: '))
        choiceCadeira = int(input('Agora escolha a cadeira que foi reservada: '))
        if sessao[choiceFileira-1][choiceCadeira-1] == 'O':
            print('Esta cadeira não está reservada.')
        else:
            sessao[choiceFileira - 1][choiceCadeira - 1] = 'O'
            print('Reserva cancelada com sucesso!')

    elif opcao == 4:
        menu = True

    else:
        print('ERRO! Escolha uma opção válida.')
