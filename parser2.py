from dataclasses import field
from distutils.errors import PreprocessError
from email.utils import decode_params
#from enum import _magic_enum_attr
from lib2to3.pgen2 import grammar
import os
from tty import setcbreak
from unittest.mock import NonCallableMock
from regex import E
#from turtle import color
os.system('cls||clear')

import requests
from bs4 import BeautifulSoup

from prettytable import PrettyTable

import time

tickers = ['NLMK'] # голубые фишки


def connect2(ticker):
    global dsi
    global ssi
    global peg 
    global res
    base_url = 'https://porti.ru/company/analysis/extend/MOEX:'
    url = base_url+ticker
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'html.parser')
    res = []
    peg = 'PEG:' + soup('div',class_="ds-col-12")[12].b.string 
    dsi = soup('div',class_="progress-label")[1].b.string
    ssi = soup('div',class_="progress-label")[2].b.string
    res = [peg,dsi,ssi]
    return

   
for i in range(len(tickers)):
    connect2(tickers[i])
    print (res)