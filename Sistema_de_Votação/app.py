import PySimpleGUI as sg
from rich import print
import os
#  CONSTANTES
VOTOS_BOLSONARO = 0
VOTOS_LULA = 0
values = 0

class Sistema_de_Votação:
    def __init__(self):
        # layout do sistema de votação
        layout = [
            [sg.Text('Sistema de Votação')],
            [sg.Text('1 - Bolsonaro')],
            [sg.Text('2 - Lula')],
            [sg.Text('Voto:', size=(25,0)),sg.Input(size=(10,0))],
            [sg.Text(f'Votos Bolsonaro: {VOTOS_BOLSONARO}')],
            [sg.Text(f'Votos Lula: {VOTOS_LULA}')],
            [sg.Button('Enviar Dados'), sg.Button('Sair')]
        ]
        # janela do sistema de votação
        
        janela = sg.Window('Sistema de Votação',layout=layout)
        # extrair dados da janela
        self.Button, self.values = janela.read()


    def votar(self):
        while True:
            # evento do sistema de votação
            try:
                if self.Button == 'Votar':
                # evento de votar
                    if values[0] == 1:
                        VOTOS_BOLSONARO += 1
                        values.update(f'{VOTOS_BOLSONARO}') 
                        return True
                    elif values[0] == 2:
                        VOTOS_LULA += 1
                        values.update(f'{VOTOS_LULA}') 
                        return
                    else:
                        print('Voto inválido')
                        return values
                elif self.Button == 'Sair':
                    # evento de sair
                    break
            except:
                print('Voto inválido')


    def iniciar(self):
        #janela do sistema de votação
        while True:
            print(self.values)
            print(self.votar)
            
        
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
