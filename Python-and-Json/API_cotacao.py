import requests, os, json

# AwesomeAPI: https://docs.awesomeapi.com.br/api-de-moedas

# API de cotação de moedas

requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
requisicao_json = requisicao.json()

# salvar arquivo em formato json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SAVE_TO = os.path.join(BASE_DIR, 'cotacao.json')

with open(SAVE_TO, 'w') as file:
    json.dump(requisicao_json, file, indent=2)
    print('Arquivo cotacao.json salvo com sucesso!')

dic_requisicao = requisicao_json

#  print(dic_requisicao['USDBRL']['name'],': R$',dic_requisicao['USDBRL']['bid'].replace('.',','))
#  print(dic_requisicao['EURBRL']['name'],': R$',dic_requisicao['EURBRL']['bid'].replace('.',','))
#  print(dic_requisicao['BTCBRL']['name'],': R$',dic_requisicao['BTCBRL']['bid'])

while True:
    print('\n')
    print('1 - USD')
    print('2 - EUR')
    print('3 - BTC')
    print('4 - Sair')
    print('\n')

    opcao = int(input('Digite a opção desejada: '))

    if opcao == 1:
        print('\n')
        print('R$',dic_requisicao['USDBRL']['bid'].replace('.',','))

    elif opcao == 2:
        print('\n')
        print('R$',dic_requisicao['EURBRL']['bid'].replace('.',','))

    elif opcao == 3:
        print('\n')
        print('R$',dic_requisicao['BTCBRL']['bid'].replace('.',','))

    elif opcao == 4:
        print('\n')
        print('Saindo...')
        exit()
    else:
        print('\n')
        print('Opção inválida!')
        print('\n')
        continue
