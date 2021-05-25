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

def pesquisa_web(termo): #realiza a pesquisa em google.com e imprime os links
    pesquisa = search(termo, num_results=3, lang="pt")
    return pesquisa
#data_hoje = data_atual()
def ouvir_microfone(): #função para ouvir o microfone
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        audio = microfone.listen(source)
        try:
            frase = microfone.recognize_google(audio, language='pt-BR')
            return frase
        except sr.UnknownValueError:
            return "Não entendi!"

def encontrar_comando (comando, frase): #encontra a palavra chave em uma frase qualquer
    if comando in frase:
        return True
    else:
        return False

lista_sites_apostas = ['bet365', 'betway', '1XBet', 'rivalo']
indices = ['primeiro', 'segundo', 'terceiro', 'quarto']

indice = ouvir_microfone()
print(indice)

for i in indices:
    if (encontrar_comando(i, indice)):
        if i == 'primeiro':
            abrir_site(pesquisa_web(lista_sites_apostas[0])[0])
        elif i == 'segundo':
            abrir_site(pesquisa_web(lista_sites_apostas[1])[0])
        elif i == 'terceiro':
            abrir_site(pesquisa_web(lista_sites_apostas[2])[0])
        elif i == 'quarto':
            abrir_site(pesquisa_web(lista_sites_apostas[3])[0])
    









