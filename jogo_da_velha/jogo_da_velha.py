from random import *

def escolher_modo_de_jogo(modo):
    while modo < 1 or modo > 2:
        print(f'"Modo {modo} é inexistente... "')
        modo = int(input('Escolha o modo de jogo: '))
    if modo == 1:
        print(f'Você escolheu o modo de jogo {modo}')
        print('Preparando-me para a batalha...')
    else:
        print(f'Você escolheu o modo de jogo {modo}! Multijogador...')
        print('Preparem-se para a batalha!')

def sortear_quem_comeca(escolha):
    if escolha == 0:
        print(f'Você escolheu CARA.')
    else:
        print(f'Você escolheu COROA')
    cara = 0
    coroa = 1
    sorteio = randint(0,1)
    if sorteio == 0:
        print ('Deu Cara!')
    else:
        print ('Deu Coroa!')
    if escolha == sorteio:
        print (f'Você irá começar...')
        return 'X'
    else:
        print ('Eu irei começar...')
        return 'O'

def exibir_jogo_da_velha():
    print('-'*20)
    for linha in matriz:
        for valor in linha:
            print(f'[{valor}]', end=' ')
        print()
    print('-'*20)

def verificar_posicao_ocupada(jogada_linha, jogada_coluna):
    while matriz[jogada_linha][jogada_coluna] == 'X' or matriz[jogada_linha][jogada_coluna] == 'O':
        print('Posição ocupada! Digite outra.')
        jogada_linha = int(input('Digite a linha da sua jogada: (0-2) '))

        while jogada_linha < 0 or jogada_linha > 2:
            print('Número de linha inválido... Digite novamente...')
            jogada_linha = int(input('Digite a linha da sua jogada: (0-2) '))

        jogada_coluna = int(input('Digite a coluna da sua jogada: (0-2) '))
        while jogada_coluna < 0 or jogada_coluna > 2:
            print('Número de coluna inválido... Digite novamente...')
            jogada_coluna = int(input('Digite a coluna da sua jogada: (0-2) '))

    return jogada_linha, jogada_coluna

def colocar_jogada_do_jogador(jogada_linha, jogada_coluna):
    matriz[jogada_linha][jogada_coluna] = 'X'




#tentativas de vitória do computador
def tentar_vencer_por_linha():
    for i in range(len(matriz)):
        qtd_o = 0
        for j in range(len(matriz)):
            if matriz[i][j] == 'O':
                qtd_o += 1
        if qtd_o == 2:
            for j in range(len(matriz[i])):
                if matriz[i][j] == " ":
                    matriz[i][j] = 'O'
                    return True
    return False

def tentar_vencer_por_coluna():
    for j in range(len(matriz[0])):
        qtd_o = 0
        for i in range(len(matriz)):
            if matriz[i][j] == 'O':
                qtd_o += 1
            if qtd_o == 2:
                for i in range(len(matriz)):
                    if matriz[i][j] == " ":
                        matriz[i][j] = 'O'
                        return True
    return False

def tentar_vencer_por_diagonal_principal():
    qtd_o = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == j and matriz[i][j] == 'O':
                qtd_o += 1
        if qtd_o == 2:
            for i in range(len(matriz)):
                for j in range(len(matriz[i])):
                    if i == j and matriz[i][j] == ' ':
                        matriz[i][j] = 'O'
                        return True
    return False

def tentar_vencer_por_diagonal_secundaria():
    qtd_o = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if (j == len(matriz) - 1 - i) and matriz[i][j] == 'O':
                qtd_o += 1
        if qtd_o == 2:
            for i in range(len(matriz)):
                for j in range(len(matriz[i])):
                    if (j == len(matriz) - 1 - i) and matriz[i][j] == ' ':
                        matriz[i][j] = 'O'
                        return True
    return False




#bloqueios do computador
def tentar_bloquear_por_linha():
    for i in range(len(matriz)):
        qtd_x = 0
        for j in range(len(matriz)):
            if matriz[i][j] == 'X':
                qtd_x += 1
        if qtd_x == 2:
            for j in range(len(matriz[i])):
                if matriz[i][j] == " ":
                    matriz[i][j] = 'O'
                    return True
    return False

def tentar_bloquear_por_coluna():
    for j in range(len(matriz[0])):
        qtd_x = 0
        for i in range(len(matriz)):
            if matriz[i][j] == 'X':
                qtd_x += 1
        if qtd_x == 2:
            for i in range(len(matriz)):
                if matriz[i][j] == " ":
                    matriz[i][j] = 'O'
                    return True
    return False

def tentar_bloquear_por_diagonal_principal():
    qtd_x = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == j and matriz[i][j] == 'X':
                qtd_x += 1
        if qtd_x == 2:
            for i in range(len(matriz)):
                for j in range(len(matriz[i])):
                    if i == j and matriz[i][j] == ' ':
                        matriz[i][j] = 'O'
                        return True
    return False

def tentar_bloquear_por_diagonal_secundaria():
    qtd_x = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if (j == len(matriz) - 1 - i) and matriz[i][j] == 'X':
                qtd_x += 1
        if qtd_x == 2:
            for i in range(len(matriz)):
                for j in range(len(matriz[i])):
                    if (j == len(matriz) - 1 - i) and matriz[i][j] == ' ':
                        matriz[i][j] = 'O'
                        return True
    return False




#jogada aleatoria, caso não tenha como vencer e nem bloquear
def jogar_aleatoriamente():
    linha = randint(0, 2)
    coluna = randint(0, 2)
    while matriz[linha][coluna] == 'X' or matriz[linha][coluna] == 'O':
        linha = randint(0, 2)
        coluna = randint(0, 2)
    matriz[linha][coluna] = 'O'




#ver se alguém ganhou
def verificar_vencedor():
    for i in range(len(matriz)):
        if matriz[i][0] == matriz[i][1] == matriz[i][2] != ' ':
            if matriz[i][0] == 'X':
                return 'X'
            else:
                if matriz[i][0] == 'O':
                    return 'O'
        if matriz[0][i] == matriz[1][i] == matriz[2][i] != ' ':
            if matriz[0][i] == 'X':
                return 'X'
            else:
                if matriz[0][i] == 'O':
                    return 'O'

    if matriz[0][0] == matriz[1][1] == matriz[2][2] != ' ':
        if matriz[0][0] == 'X':
            return 'X'
        else:
            if matriz[0][0] == 'O':
                return 'O'
    if matriz[0][2] == matriz[1][1] == matriz[2][0] != ' ':
        if matriz[0][2] == 'X':
            return 'X'
        else:
            if matriz[0][2] == 'O':
                return 'O'

    return False


matriz = [[" ", " ", " "],
          [" ", " ", " "],
          [" ", " ", " "]]

#escolher modo de jogo
print('[1] -> Jogar Contra Computador')
print('[2] -> Multijogador Local')
modo = int(input('Escolha o modo de jogo: '))
escolher_modo_de_jogo(modo)

#cara ou coroa pra ver quem começa
escolha = int(input('Escolha Cara [0] ou Coroa [1] : '))
while escolha < 0 or escolha > 1:
    print('Escolha inválida.')
    escolha = int(input('Escolha Cara [0] ou Coroa [1] : '))


jogador_que_comeca = sortear_quem_comeca(escolha)

if jogador_que_comeca == 'O':
    exibir_jogo_da_velha() #mostrar o jogo com o tabuleiro vazio, antes do jogo de fato começar

    while ' ' not in matriz and not verificar_vencedor():

        #jogadas do computador
        jogada_realizada = False

        if tentar_vencer_por_linha():
            jogada_realizada = True
        else:
            if tentar_vencer_por_coluna():
                jogada_realizada = True
            else:
                if tentar_vencer_por_diagonal_principal():
                    jogada_realizada = True
                else:
                    if tentar_vencer_por_diagonal_secundaria():
                        jogada_realizada = True
                    else:
                        if tentar_bloquear_por_linha():
                            jogada_realizada = True
                        else:
                            if tentar_bloquear_por_coluna():
                                jogada_realizada = True
                            else:
                                if tentar_bloquear_por_diagonal_principal():
                                    jogada_realizada = True
                                else:
                                    if tentar_bloquear_por_diagonal_secundaria():
                                        jogada_realizada = True
                                    else:
                                        if jogar_aleatoriamente():
                                            jogada_realizada = True
        exibir_jogo_da_velha()


        vencedor = verificar_vencedor()
        if vencedor == 'X':
            print('Você Venceu!')
            break
        else:
            if vencedor == 'O':
                print('Eu venci!')
                break
            else:
                print('Sem Vencedor!')




        #permitir digitação por posição pelo jogador
        jogada_linha = int(input('Digite a linha da sua jogada: (0-2) '))
        while jogada_linha < 0 or jogada_linha > 2:
            print('Número de linha inválido... Digite novamente...')
            jogada_linha = int(input('Digite a linha da sua jogada: (0-2) '))

        jogada_coluna = int(input('Digite a coluna da sua jogada: (0-2) '))
        while jogada_coluna < 0 or jogada_coluna > 2:
            print('Número de coluna inválido... Digite novamente...')
            jogada_coluna = int(input('Digite a coluna da sua jogada: (0-2) '))
        jogada_linha,jogada_coluna = verificar_posicao_ocupada(jogada_linha,jogada_coluna)
        colocar_jogada_do_jogador(jogada_linha,jogada_coluna)
        exibir_jogo_da_velha()

        vencedor = verificar_vencedor()
        if vencedor == 'X':
            print('Você Venceu!')
            break
        else:
            if vencedor == 'O':
                print('Eu venci!')
                break
            else:
                print('Sem Vencedor!')

else:
    if jogador_que_comeca == 'X':
        exibir_jogo_da_velha()
        while ' ' not in matriz and not verificar_vencedor():
            # permitir digitação por posição pelo jogador
            jogada_linha = int(input('Digite a linha da sua jogada: (0-2) '))
            while jogada_linha < 0 or jogada_linha > 2:
                print('Número de linha inválido... Digite novamente...')
                jogada_linha = int(input('Digite a linha da sua jogada: (0-2) '))

            jogada_coluna = int(input('Digite a coluna da sua jogada: (0-2) '))
            while jogada_coluna < 0 or jogada_coluna > 2:
                print('Número de coluna inválido... Digite novamente...')
                jogada_coluna = int(input('Digite a coluna da sua jogada: (0-2) '))
            jogada_linha, jogada_coluna = verificar_posicao_ocupada(jogada_linha, jogada_coluna)
            colocar_jogada_do_jogador(jogada_linha, jogada_coluna)
            exibir_jogo_da_velha()

            vencedor = verificar_vencedor()
            if vencedor == 'X':
                print('Você Venceu!')
                break
            else:
                if vencedor == 'O':
                    print('Eu venci!')
                    break
                else:
                    print('Sem Vencedor!')

            # jogadas do computador
            jogada_realizada = False

            if tentar_vencer_por_linha():
                jogada_realizada = True
            else:
                if tentar_vencer_por_coluna():
                    jogada_realizada = True
                else:
                    if tentar_vencer_por_diagonal_principal():
                        jogada_realizada = True
                    else:
                        if tentar_vencer_por_diagonal_secundaria():
                            jogada_realizada = True
                        else:
                            if tentar_bloquear_por_linha():
                                jogada_realizada = True
                            else:
                                if tentar_bloquear_por_coluna():
                                    jogada_realizada = True
                                else:
                                    if tentar_bloquear_por_diagonal_principal():
                                        jogada_realizada = True
                                    else:
                                        if tentar_bloquear_por_diagonal_secundaria():
                                            jogada_realizada = True
                                        else:
                                            if jogar_aleatoriamente():
                                                jogada_realizada = True
            exibir_jogo_da_velha()

            vencedor = verificar_vencedor()
            if vencedor == 'X':
                print('Você Venceu!')
                break
            else:
                if vencedor == 'O':
                    print('Eu venci!')
                    break
                else:
                    print('Sem Vencedor!')

