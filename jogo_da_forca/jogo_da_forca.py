palavra = []
vidas = 6
letras_erradas = []

codigo = input('Digite a palavra que o outro jogador terá que descobrir: ').upper()

for i in range(100):
    print()

for j in codigo:
    palavra.append(j)

tracos = ["_"] * len(palavra)

print("SEJA BEM VINDO AO JOGO DA FORCA")
modo = int(input("ESCOLHA O SEU MODO DE JOGO [1 = FACIL (COM DICA)], [2 = NORMAL (SEM DICA)], [3 = DIFICIL (SEM DICA E COM POUCA VIDA)]: "))

if modo != 1 and modo != 2 and modo != 3:
    print("OPÇÃO INVÁLIDA")
    modo = int(input("ESCOLHA O SEU MODO DE JOGO NOVAMENTE: "))

if modo == 1:
    print("VOCÊ ESCOLHEU O MODO DE JOGO FACIL.")
    dica = input("Digite uma dica para o modo de jogo facil: ")
    for i in range(100):
        print()
    print('Modo: FÁCIL')
    print(f"VOCÊ PODE ERRAR APENAS {vidas} VEZES")
    print(f"A PALAVRA ESCOLHIDA TEM: {len(palavra)} CARACTERES")
    print(f"SUA DICA É: {dica}")
    for t in tracos:
        print(t, end=" ")
    print()

    while palavra != tracos and vidas > 0:
        tentativa = input('Digite uma letra: ').upper()

        while tentativa in letras_erradas:
            print(f'VOCÊ JÁ DIGITOU A LETRA {tentativa}')
            tentativa = input('DIGITE DE NOVO: ').upper()

        achou_na_palavra = False
        for letra in palavra:
            if tentativa == letra:
                achou_na_palavra = True

        achou_nos_tracos = False
        for letra in tracos:
            if tentativa == letra:
                achou_nos_tracos = True

        if not achou_nos_tracos:
            if not achou_na_palavra:
                vidas -= 1
                letras_erradas.append(tentativa)
                print("NÃO TEM ESSA LETRA CARA")
                print("SE COM DICA VOCÊ TÁ ERRANDO, IMAGINA SEM!")
                print(f"VOCÊ PODE ERRAR SÓ MAIS {vidas} VEZES")
                print()
            else:
                for i in range(len(palavra)):
                    if palavra[i] == tentativa:
                        tracos[i] = palavra[i]
                        print()
        else:
            print("VOCÊ NÃO SE LEMBRA DAS LETRAS QUE JÁ COLOCOU? TENTA DE NOVO!")

        for t in tracos:
            print(t, end=" ")
        print()
        print(f'Letras erradas: {letras_erradas}')
        print()

    if vidas == 0:
        print(f"PARABÉNS, MESMO COM DICA VOCE CONSEGUIU ERRAR A PALAVRA {codigo}...")
    else:
        print("PARABÉNS, COM DICA ESSE ERA O MÍNIMO QUE VOCÊ PODERIA FAZER!!")

if modo == 2:
    print(f"A PALAVRA ESCOLHIDA TEM: {len(palavra)} CARACTERES")
    print(f"VOCÊ PODE ERRAR APENAS {vidas} VEZES")

    for t in tracos:
        print(t, end=" ")
    print()

    while palavra != tracos and vidas > 0:
        tentativa = input('Digite uma letra: ').upper()

        while tentativa in letras_erradas:
            print(f'VOCÊ JÁ DIGITOU A LETRA {tentativa}. ELA ESTÁ ERRADA')
            tentativa = input('DIGITA DE NOVO: ').upper()

        achou_na_palavra = False
        for letra in palavra:
            if tentativa == letra:
                achou_na_palavra = True

        achou_nos_tracos = False
        for letra in tracos:
            if tentativa == letra:
                achou_nos_tracos = True

        if not achou_nos_tracos:
            if not achou_na_palavra:
                vidas -= 1
                letras_erradas.append(tentativa)
                print("NÃO TEM ESSA LETRA")
                print(f"VOCÊ PODE ERRAR SÓ MAIS {vidas} VEZES")
                print()
            else:
                for i in range(len(palavra)):
                    if palavra[i] == tentativa:
                        tracos[i] = palavra[i]
                        print()
        else:
            print("VOCÊ JÁ JOGOU ESSA LETRA!")

        for t in tracos:
            print(t, end=" ")
        print()
        print(f'Letras erradas: {letras_erradas}')
        print()

    if vidas == 0:
        print(f"INFELIZMENTE VOCÊ NÃO ACERTOU A PALAVRA QUE ERA: {codigo}")
    else:
        print("PARABÉNS VOCE ACERTOU A PALAVRA!!")

if modo == 3:
    print("VOCÊ ESCOLHEU O MODO DE JOGO DIFÍCIL, TE DESEJO SORTE!")
    print(f"A PALAVRA ESCOLHIDA TEM: {len(palavra)} CARACTERES")
    vidas = 4
    print(f"VOCÊ PODE ERRAR APENAS {vidas} VEZES")

    for t in tracos:
        print(t, end=" ")
    print()

    while palavra != tracos and vidas > 0:
        tentativa = input('Digite uma letra: ').upper()

        while tentativa in letras_erradas:
            print(f'VOCÊ JÁ DIGITOU A LETRA {tentativa}.ELA ESTÁ ERRADA.')
            tentativa = input('RESPIRE FUNDO E DIGITA DE NOVO: ').upper()

        achou_na_palavra = False
        for letra in palavra:
            if tentativa == letra:
                achou_na_palavra = True

        achou_nos_tracos = False
        for letra in tracos:
            if tentativa == letra:
                achou_nos_tracos = True

        if not achou_nos_tracos:
            if not achou_na_palavra:
                vidas -= 1
                letras_erradas.append(tentativa)
                print(f"NÃO TEM A LETRA {tentativa}")
                print(f"VOCÊ PODE ERRAR SÓ MAIS {vidas} VEZES")
                print()
            else:
                for i in range(len(palavra)):
                    if palavra[i] == tentativa:
                        tracos[i] = palavra[i]
                        print()
        else:
            print(f"VOCÊ JÁ JOGOU A LETRA {tentativa}")

        for t in tracos:
            print(t, end=" ")
        print()

    if vidas == 0:
        print(f"INFELIZMENTE VOCE NÃO ACERTOU A PALAVRA QUE ERA: {codigo}")
    else:
        print("PARABENS VOCE É MONSTRO, ACERTOU A PALAVRA!!")