import json
from time import sleep

import requests

URL_ALL = 'https://economia.awesomeapi.com.br/all'
class ApiCotacao:
          def __init__(self, url):
              self.url_all = url
              
          def parsing(self, moeda):
              try:
                  url = self.url_all
                  resposta = requests.get(f'{url}/{moeda}')
                  if resposta:
                      texto = resposta.text
                  if texto:
                      conversao = json.loads(texto)
                  return conversao
              except:
                  print('erro')    

          def mostrar_moeda(self, moeda):

             try:
                 dictionary = ApiCotacao.parsing(self, moeda)
                 if dictionary:
                     chave = dictionary[moeda]
                     code = chave['code']
                     codein = chave['codein']
                     name = chave['name']
                     bid = chave['bid']
                     ask = chave['ask']
                     high = chave['high']
                     low = chave['low']
                     varbid = chave['varBid']
                     print(f'## MOEDA: {code} - {codein} / {name}  ##')
                     print(f'## BID: {bid} # ASK: {ask} ##')
                     print(f'## HIGH: {high} # LOW: {low} ##')
                     print(f'## varBid: {varbid}   ##') #-0.02
             except Exception as e:
                print(e)
