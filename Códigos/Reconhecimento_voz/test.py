from datetime import datetime
import speech_recognition as sr
from googlesearch import search
import pyttsx3
import webbrowser
import sqlite3
import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
import selenium
import agenda_c_bd

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

def sintese_voz(entrada_de_texto): #função para sintetizar voz
    falar = pyttsx3.init('sapi5')
    falar.say(entrada_de_texto)
    falar.runAndWait()




def comparar_data(data):
    if data == data_atual():
        return True
    else:
        return False



def lembrete_jogo():
    banco = sqlite3.connect('teste_agenda.db')
    cursor = banco.cursor()
    cursor.execute("SELECT* FROM jogos2 WHERE data='"+data_atual()+"'")
    jogos = 0
    for i in cursor:
        jogos += 1
        print(i)
    if jogos == 0:
        print('Nenhum jogo da sua agenda acontecendo hoje!')
    else:
        print("Estes são os jogos que acontecem hoje!")
        
    banco.close()


#agenda_c_bd.exibir_agenda()

#print(comparar_data('26/05/2021'))
lembrete_jogo()








