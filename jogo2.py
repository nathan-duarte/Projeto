from random import randint

from time import sleep

itens = ('Pedra', 'Papél', 'Tesoura')

computador = randint (0, 2)

print ('Suas opções: [0] Pedra [1] Papél [2] Tesoura')

jogador = int(input('Qual é a sua jogada? '))

print ('O jogador jogou {}'.format(itens[jogador]))

print ('O computador jogou {}'.format(itens[computador]))

print('PEDRA')

sleep(1)

print('PAPÉL')

sleep(1)

print('TESOURA')

print('-=' * 11)

if computador == 0: #jogador jogou pedra

    if jogador == 0:

        print('Empate')

    elif jogador == 1:

        print('O jogador venceu')

    elif jogador == 2:

        print('O compuatdor venceu')

    else:

        ('Jogada inválida')

if computador == 2: #computador jogou tesoura

    if jogador == 1:

        print('O computador venceu')

    elif jogador == 2:

        print('Empate')

    elif jogador == 0:

        print('Jogador venceu')

    else:

        print('Jogada inválida')
        
    if computador == 1:

        if jogador == 1:

            print('Empate')

        elif jogador == 2:

            print('Jogador venceu')

        elif jogador == 0:

            print('Computador venceu')

        else:

            ('Jogada inválida')







