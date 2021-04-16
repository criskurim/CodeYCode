import speech_recognition as sr
from googlesearch import search
import pyttsx3

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

while True:
    frase = ouvir_microfone()
    if encontrar_comando('casa', frase):
        print(frase)
    else:
        print('não encontrei')