import requests, os, json

# AwesomeAPI: https://docs.awesomeapi.com.br/api-de-moedas

requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
requisicao_json = requisicao.json()


# salvar arquivo em formato json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SAVE_TO = os.path.join(BASE_DIR, 'cotacao.json')

with open(SAVE_TO, 'w') as file:
    json.dump(requisicao_json, file, indent=2)


dic_requisicao = requisicao.json()

if requisicao.status_code == 200:
    print(dic_requisicao['USDBRL']['name'],': R$',dic_requisicao['USDBRL']['bid'].replace('.',','))
    print(dic_requisicao['EURBRL']['name'],': R$',dic_requisicao['EURBRL']['bid'].replace('.',','))
    print(dic_requisicao['BTCBRL']['name'],': R$',dic_requisicao['BTCBRL']['bid'])
    
if requisicao.status_code == 404:
    print('Erro 404. Moeda não encontrada')
