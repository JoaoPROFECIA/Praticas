import requests
import os

# AwesomeAPI: https://docs.awesomeapi.com.br/api-de-moedas
def cotacao():
    requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

    requisicao
    
    requisicao.json()
    
    # salvar arquivo em formato json
    with open('cotacao.json', 'w') as f:
        f.write(requisicao.text)


    dic_requisicao = requisicao.json()

    if requisicao.status_code == 200:
        print(dic_requisicao['USDBRL']['name'],': R$',dic_requisicao['USDBRL']['bid'].replace('.',','))
        print(dic_requisicao['EURBRL']['name'],': R$',dic_requisicao['EURBRL']['bid'].replace('.',','))
        print(dic_requisicao['BTCBRL']['name'],': R$',dic_requisicao['BTCBRL']['bid'])
        
    if requisicao.status_code == 404:
        print('Erro 404. Moeda não encontrada')
    

cotacao()
