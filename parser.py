# скачиваем страницу в test.html
# import requests
# from bs4 import BeautifulSoup
# url = 'https://porti.ru/company/analysis/extend/MOEX:GAZP'
# r = requests.get(url)
# with open ('test.html','w') as output_file:
#    output_file.write(r.text)

from dataclasses import field
from distutils.errors import PreprocessError
from email.utils import decode_params
#from enum import _magic_enum_attr
from lib2to3.pgen2 import grammar
import os
#from tty import setcbreak
from unittest.mock import NonCallableMock
#from regex import E
#from turtle import color
os.system('cls||clear')

import requests
from bs4 import BeautifulSoup

from prettytable import PrettyTable

import time

#print (page.status_code)

# lets go


# голубые фишки 15шт 
# imoex 27шт (1+2 эшелон)
# 58 акций индекс малой и средней капитализации 2-3 эшелон

tickers = ['NLMK','GAZP','MTSS','SBER','TATN','YNDX','NVTK','MGNT','LKOH'] # голубые фишки
#tickers = ['GMKN','ROSN','SNGS'] # голубые фишки


def connect(ticker):  # получаем показатели по тикеру - пример использования: connect('GAZP')
    global stock_name 
    global stock_price
    global pe
    global pbv
    global roe

    base_url = 'https://porti.ru/company/mfso/MOEX:'
    url = base_url+ticker
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'html.parser')

    stock_name = soup.find('h1').text
    stock_price = soup.find('td', {'data-type': 'LTM'}, field="common_share").text
    pe = soup.find('td', {'data-type': 'LTM'}, field="p_e").text
    pbv = soup.find('td', {'data-type': 'LTM'}, field="p_bv").text
    roe = soup.find('td', {'data-type': 'LTM'}, field="roe").text
    return


def connect2(ticker):
    global res
    global dsi
    global ssi
    global peg 
    global buffet
    global graham
    global div_strategy
    global gram
    global ddm
    global dcf

    base_url = 'https://porti.ru/company/analysis/extend/MOEX:'
    url = base_url+ticker
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'html.parser')
    res = []
    peg = 'PEG: ' + soup('div',class_="ds-col-12")[12].b.string 
    dsi = 'DSI: ' + soup('div',class_="progress-label")[1].b.string
    ssi = 'SSI: ' + soup('div',class_="progress-label")[2].b.string
    buffet = 'Buffet: ' + soup('div',class_="progress-label")[3].b.string
    graham = 'Graham ' + soup('div',class_="progress-label")[4].b.string
    div_strategy = 'Div-strategy(!): ' + soup('div',class_="progress-label")[5].b.string
    gram = 'Gram ' + soup('div',class_="progress-label")[6].b.string
    ddm = 'DDM(!) ' + soup('div',class_="ds-col-12")[10].b.string
    dcf = 'DCF ' + soup('div',class_="ds-col-12")[11].b.string

    res = [peg,dsi,ssi,buffet,graham,div_strategy,gram,ddm,dcf]
    return

 # выводим результат 

for i in range(len(tickers)):
    connect(tickers[i])
    newtable = PrettyTable(['Stock','Price','Pe','Pbv','Roe'])
    newtable.add_row([stock_name,stock_price,pe,pbv,roe])
    print (newtable)
    time.sleep(0.5)
    connect2(tickers[i])
    print (res)



   

