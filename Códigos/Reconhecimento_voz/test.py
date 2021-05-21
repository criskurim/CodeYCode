from datetime import datetime
import speech_recognition as sr
from googlesearch import search
import pyttsx3
import webbrowser

import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
import selenium

def abrir_site(site):
    webbrowser.open(site, new=0, autoraise=True)

def data_atual():
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y')
    return data_e_hora_em_texto


data_hoje = data_atual()

#site = f'https://www.uol.com.br/esporte/futebol/central-de-jogos/#/{data_hoje}'
#abrir_site(site)

############################################################################################################################

#query = input('Digite o produto que deseja pesquisar: ')


resposta = requests.get('https://www.goal.com/br/not%C3%ADcias/programacao-partidas-futebol-tv-aberta-fechada-onde-assistir/1jf3cuk3yh5uz18j0s89y5od6w')

lista_jogos = []

content = resposta.content

site = BeautifulSoup(content, 'html.parser')
tabela_jogos = site.find('table', attrs={'class': 'tableizer-table'})
jogos = tabela_jogos.findAll('tr')
for jogo in jogos:
    print(jogo.text)

#print(site_html)








