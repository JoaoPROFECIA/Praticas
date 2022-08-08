import requests

# AwesomeAPI: https://docs.awesomeapi.com.br/api-de-moedas
def cotacao():
    requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    requisicao
    requisicao.json()
    dic_requisicao = requisicao.json()
    if requisicao.status_code == 200:
        print(dic_requisicao['USDBRL']['bid'])
    if requisicao.status_code == 404:
        print('Erro 404. Moeda não encontrada')
    
cotacao()
