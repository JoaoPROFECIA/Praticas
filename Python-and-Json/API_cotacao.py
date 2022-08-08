import requests, os, json

#  AwesomeAPI: https://docs.awesomeapi.com.br/api-de-moedas

#  API de cotação de moedas

requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL') #  requisita a API
requisicao_json = requisicao.json() #  Converte para json

#  salvar arquivo em formato json

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) #  diretorio atual
SAVE_TO = os.path.join(BASE_DIR, 'cotacao.json') #  diretorio e nome do arquivo

with open(SAVE_TO, 'w') as file: #  abre o arquivo
    json.dump(requisicao_json, file, indent=2) #  salva o arquivo
    print('Arquivo cotacao.json salvo com sucesso!') #  mensagem de sucesso

dic_requisicao = requisicao_json #  cria um dicionario com a requisicao

#  print(dic_requisicao['USDBRL']['name'],': R$',dic_requisicao['USDBRL']['bid'].replace('.',','))
#  print(dic_requisicao['EURBRL']['name'],': R$',dic_requisicao['EURBRL']['bid'].replace('.',','))
#  print(dic_requisicao['BTCBRL']['name'],': R$',dic_requisicao['BTCBRL']['bid'])

while True: 
    #  menu de opções
    print('\n')
    print('1 - USD')
    print('2 - EUR')
    print('3 - BTC')
    print('4 - Sair')
    print('\n')

    opcao = int(input('Digite a opção desejada: ')) 

    if opcao == 1: 
        print('\n')
        print('R$',dic_requisicao['USDBRL']['bid'].replace('.',',')) #  exibe o valor do dolar

    elif opcao == 2:
        print('\n')
        print('R$',dic_requisicao['EURBRL']['bid'].replace('.',',')) #  exibe o valor do euro

    elif opcao == 3:
        print('\n')
        print('R$',dic_requisicao['BTCBRL']['bid'].replace('.',',')) #  exibe o valor do bitcoin

    elif opcao == 4:
        print('\n')
        print('Saindo...') #  mensagem de saída
        exit()
    else:
        print('\n')
        print('Opção inválida!') #  mensagem de opção inválida
        print('\n')
        continue
