import PySimpleGUI as sg
from rich import print
import os
#  CONSTANTES
VOTOS_BOLSONARO = 0
VOTOS_LULA = 0

class Sistema_de_Votação:
    def __init__(self):
        #layout do sistema de votação
        layout = [
            [sg.Text('Sistema de Votação')],
            [sg.Text('1 - Bolsonaro')],
            [sg.Text('2 - Lula')],
            [sg.Text('Voto:'), sg.InputText()],
            [sg.Button('Votar'),sg.Button('Sair')]
        ]
        # Janela
        janela = sg.Window('Sistema de Votação',layout())
        # Extrair evento e valores
        self.button, self.values = janela.read()
    def iniciar(self):
        #janela do sistema de votação
        self.janela = sg.Window('Sistema de Votação',layout)
        while True:
            #evento do sistema de votação
            event, values = self.janela.read()
            try:
                if event == 'Voto':
                #evento de votar
                    if values[0] == '1':
                        VOTOS_BOLSONARO += 1
                    elif values[0] == '2':
                        VOTOS_LULA += 1
                    else:
                        print('Voto inválido')
                elif event == 'Sair':
                    #evento de sair
                    break
            except:
                print('Voto inválido')
tela = Sistema_de_Votação()
tela.iniciar()

#  roda eternamente
"""while True:
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
    os.system('cls')"""
