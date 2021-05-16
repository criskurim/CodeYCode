import speech_recognition as sr
from googlesearch import search
import pyttsx3
import webbrowser

#Declaração de funções a serem chamadas ao longo do programa


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

def encontrar_comando (comando, frase):
    if comando in frase:
        return True
    else:
        return False

def sintese_voz(entrada_de_texto): #função para sintetizar voz
    falar = pyttsx3.init('sapi5')
    falar.say(entrada_de_texto)
    falar.runAndWait()

def pesquisa_web(termo): #realiza a pesquisa em google.com e imprime os links
    for i in search(termo, tld="com", num=3, stop=4, pause=2):
        print(i)
    return
def abrir_site(site):
    webbrowser.open(site, new=0, autoraise=True)

def consulta_time(time, list):  
    if time in list:
        return True
    else:
        return False


bet_diz = "Diga o nome do time! "
print(bet_diz)
sintese_voz(bet_diz)
time = ouvir_microfone()

list_times = ['América-MG', 'Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Bahia', 'Bragantino', 'Ceará', 'Chapecoense', 'Corinthians', 'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Grêmio', 'Internacional', 'Juventude', 'Palmeiras', 'Santos', 'São Paulo', 'Sport', 'Avaí', 'Botafogo', 'Brasil de Pelotas', 'Brusque', 'CRB', 'CSA', 'Confiança', 'Coritiba', 'Cruzeiro', 'Goiás', 'Guarani', 'Londrina', 'Náutico', 'Operário-PR', 'Ponte Preta', 'Remo', 'Sampaio Corrêa', 'Vasco', 'Vila Nova', 'Vitória']

if consulta_time(time, list_times):
    print('Você escolheu: ', time)
    site_videos = f'www.youtube.com/results?search_query={time}'
    site_memes = f'https://oledobrasil.com.br/?s={time}'
    site_noticias = f'https://globoesporte.globo.com/busca/?q={time}'

    abrir_site(site_videos)
    abrir_site(site_memes)
    abrir_site(site_noticias)
else:
    print('Não entendi qual o time você escolheu!')
print('Tudo parece ok!')