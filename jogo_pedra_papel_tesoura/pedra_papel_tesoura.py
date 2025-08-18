from random import *
print('PEDRA, PAPEL OU TESOURA')
print('Opções:')
print('0 - PEDRA | '
      '1 - PAPEL | '
      '2 - TESOURA ')

escolha_computador = randint(0,2)
escolha_jogador = int(input('Insira sua escolha: '))
while escolha_jogador < 0 or escolha_jogador >2:
    print("escolha um número entre 0 e 2!")
    print('0 - PEDRA | '
          '1 - PAPEL | '
          '2 - TESOURA ')
    escolha_jogador = int(input('Insira sua escolha: '))

if escolha_jogador == 0:
    print('Você escolheu PEDRA.')
else:
    if escolha_jogador == 1:
        print('Você escolheu PAPEL.')
    else:
        if escolha_jogador == 2:
            print('Você escolheu TESOURA.')

if escolha_computador == 0:
    print('Eu joguei PEDRA')
else:
    if escolha_computador == 1:
        print('Eu joguei PAPEL')
    else:
        if escolha_computador == 2:
            print('Eu joguei TESOURA')

if escolha_jogador == escolha_computador:
    print('Deu EMPATE!')
else:
    if escolha_jogador == 0:
        if escolha_computador == 1:
            print('VOCÊ PERDEU!.')
        else:
            if escolha_computador == 2:
                print('VOCÊ VENCEU')
    else:
        if escolha_jogador == 1:
            if escolha_computador == 0:
                print('VOCÊ VENCEU!')
            else:
                if escolha_computador == 2:
                    print("VOCÊ PERDEU!")
        else:
            if escolha_jogador == 2:
                if escolha_computador == 0:
                    print("VOCÊ PERDEU!")
                else:
                    if escolha_computador == 1:
                        print("VOCÊ VENCEU!")