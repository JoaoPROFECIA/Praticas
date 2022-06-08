from rich import print
import os
#  CONSTANTES
VOTOS_BOLSONARO = 0
VOTOS_LULA = 0

#  roda eternamente
while True:
    print('*' * 20)
    print(f'TOTAL BOLSONARO: {VOTOS_BOLSONARO}{os.linesep}TOTAL LULA: {VOTOS_LULA}')
    print('*' * 20)
    #  permite o usuário escolher o candidato
    try:
        voto = int(input(f'Escolha o candidato:{os.linesep}1 - Bolsonaro{os.linesep}2 - Lula{os.linesep}Seu voto: '))
        #  verifica se o usuário escolheu o candidato correto
        if voto == 1:
            VOTOS_BOLSONARO += 1
        elif voto == 2:
            VOTOS_LULA += 1
        else:
            pass
    except:
        print('Você deve escolher um número entre 1 e 2')
    os.system('cls')
