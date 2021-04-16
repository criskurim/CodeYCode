#Bibliotecas demandadas pelo programa
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
# início do programa
bet_diz = "Olá, eu sua Bet! " \
          "Se disser, 'Pesquisar!', realizarei uma pesquisa do termo que você desejar," \
          " mas caso deseje encerrar o programa basta dizer 'Obrigado!'."

print(bet_diz)
sintese_voz(bet_diz)

#loop para ouvir continuamente
ouvindo = True

while ouvindo:
    bet_diz = 'Diga algo!'
    print(bet_diz)                  #solicita que o usuária diga algo
    sintese_voz(bet_diz)
    ouvir_microfone()               #aciona a função ouvir_microfone()
    frase = ouvir_microfone()       #armazena em uma variável o que foi retornado da função
    frase = frase.lower()

    if encontrar_comando('pesquisar', frase):        #condição para realizar a função pesquisa_web
        bet_diz = ("O que deseja pesquisar? ")
        print(bet_diz)
        sintese_voz(bet_diz)
        buscar = ouvir_microfone()  #armazena na variável busca o que foi retornado da função ouvir_microfone
        bet_diz = (f'Estes são os resultados para: {buscar}')
        sintese_voz(bet_diz)
        print(f'{bet_diz}')         #confirma para o usuário o que foi dito
        print(pesquisa_web(buscar))

    elif encontrar_comando('obrigado', frase):       #comando de voz que encerra o programa
        ouvindo = False

    else:                           #ouve e imprime o que foi dito indefinidamente até que algum comando seja entendido
        bet_diz = (frase)
        sintese_voz(bet_diz)
        print(bet_diz)


bet_diz = "Foi um prazer ajudá-lo!!"
sintese_voz(bet_diz)
print(bet_diz)







