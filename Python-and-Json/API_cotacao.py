import requests, os, json, time

#  AwesomeAPI: https://docs.awesomeapi.com.br/api-de-moedas

#  API de cotação de moedas

requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL') #  requisita a API
requisicao_json = requisicao.json() #  Converte para json

#  salvar arquivo em formato json

#  dict de cores 
cor = {
        'verde': '\033[32m',
        'vermelho': '\033[31m',
        'amarelo': '\033[33m',
        'azul': '\033[34m',
        'branco': '\033[37m',
        'limpa': '\033[m'
        }

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) #  diretorio atual
SAVE_TO = os.path.join(BASE_DIR, 'cotacao.json') #  diretorio e nome do arquivo

with open(SAVE_TO, 'w') as file: #  abre o arquivo
    json.dump(requisicao_json, file, indent=4) #  salva o arquivo
    print(cor['verde'],'Arquivo "cotacao.json" salvo com sucesso!',cor['limpa']) #  mensagem de sucesso
    time.sleep(1)

data_e_hora_em_texto = time.strftime('%d/%m/%Y %H:%M:%S') #  data e hora atual

print()
print('Escoha uma moeda para ver a cotação:')
print('1 - USD\n''2 - EUR\n''3 - BTC\n''4 - Sair\n\n'
      'Cotação atualizada em:', data_e_hora_em_texto)
print()

while True: 
    time.sleep(0.4)
    opcao = input('Digite a opção desejada: ').strip().upper()
    time.sleep(0.4)

    if opcao == '1' or opcao == 'USD' or opcao == 'DOLAR' or opcao == 'DÓLAR': 
        print()
        print(requisicao_json['USDBRL']['name'],'\nR$',requisicao_json['USDBRL']['bid'].replace('.',',')) #  exibe o valor do dolar
        print()

    elif opcao == '2' or opcao == 'EUR' or opcao == 'EURO':
        print()
        print(requisicao_json['EURBRL']['name'],'\nR$',requisicao_json['EURBRL']['bid'].replace('.',',')) #  exibe o valor do euro
        print()

    elif opcao == '3' or opcao == 'BTC' or opcao == 'BITCOIN':
        print()
        print(requisicao_json['BTCBRL']['name'],'\nR$',requisicao_json['BTCBRL']['bid']) #  exibe o valor do bitcoin
        print()

    elif opcao == '4' or opcao == 'SAIR':
        print()
        print('Saindo',end='') #  mensagem de saída
        for i in range(3):
            print('.',end='')
            time.sleep(0.4)
        exit()
    else:
        print()
        print(cor['vermelho'],'Opção inválida!',cor['limpa']) #  mensagem de opção inválida
        print()
        continue
