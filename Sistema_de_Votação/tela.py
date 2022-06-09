import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('Dark2')
        # layout do sistema
        layout = [
            [sg.Text('Nome',size=(5,0)),sg.Input(size=(15,0),key='nome')],
            [sg.Text('Idade',size=(5,0)),sg.Input(size=(15,0),key='idade')],
            [sg.Text('Quais provedores de e-mail são aceitos?')],
            [sg.Checkbox('Gmail',size=(5,0),key='gmail'),sg.Checkbox('Outlook',size=(5,0),key='outlook'),sg.Checkbox('Yahoo',size=(5,0),key='yahoo')],
            [sg.Text('Aceita cartão?')],
            [sg.Radio('Sim','cartões',key='aceitaCartao'),sg.Radio('Não','cartões',key='naoAceitaCartao')],
            [sg.Slider(range=(0,255),default_value=0,orientation='h',size=(15,20),key='sliderVelocidade')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(30,20))]
        ]
        # janela do sistema
        self.janela = sg.Window('Dados do usuario').layout(layout)
    
    def iniciar(self):
        while True:
            # extrair dados da janela
            self.button, self.values = self.janela.read()
            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            aceita_cartao = self.values['aceitaCartao']
            nao_aceita_cartao = self.values['naoAceitaCartao']
            velocidade_script = self.values['sliderVelocidade']
            print(f'Nome: {nome}')
            print(f'Idade: {idade}')
            print(f'Gmail: {aceita_gmail}')
            print(f'Outlook: {aceita_outlook}')
            print(f'Yahoo: {aceita_yahoo}')
            print(f'Cartão: {aceita_cartao}')
            print(f'Não aceita Cartão: {nao_aceita_cartao}')
            print(f'Velocidade do script: {velocidade_script}')

tela = TelaPython()
tela.iniciar()
