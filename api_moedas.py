from modulo import ApiCotacao
from time import sleep
    
if __name__ == '__main__':
    
    URL_ALL = 'https://economia.awesomeapi.com.br/all'
    try:
         api_cotacao = ApiCotacao(URL_ALL)
         moeda = input('Digite uma moeda para fazer cotação: ')
         while moeda:
             print(api_cotacao.mostrar_moeda(moeda))
             for contagem in range(0, 5):
                sleep(5)
    except Exception as e:
        print(e)


