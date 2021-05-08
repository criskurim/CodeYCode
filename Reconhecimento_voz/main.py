
#Bibliotecas demandadas pelo programa
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

def encontrar_comando (comando, frase): #encontra a palavra chave em uma frase qualquer
    if comando in frase:
        return True
    else:
        return False

def sintese_voz(entrada_de_texto): #função para sintetizar voz
    falar = pyttsx3.init('sapi5')
    falar.say(entrada_de_texto)
    falar.runAndWait()

def pesquisa_web(termo): #realiza a pesquisa em google.com e imprime os links
    list_sites_resultados = []
    for i in search(termo, tld="com", num=3, stop=4, pause=2):
        list_sites_resultados.append(i)
    return list_sites_resultados

def abrir_site(site):
    webbrowser.open(site, new=0, autoraise=True)

# início do programa
bet_inicio = "Olá, eu sou Bet, sua assistente virtual!"

print(bet_inicio)
sintese_voz(bet_inicio)

#loop para ouvir continuamente
ouvindo = True

while ouvindo:
    bet_diz = 'Estou ouvindo!'
    print(bet_diz)                  #solicita que o usuária diga algo
    sintese_voz(bet_diz)
    frase = ouvir_microfone() #aciona a função ouvir_microfone() e armazena em uma variável o que foi retornado da função

    if encontrar_comando('pesquisa', frase):        #condição para realizar a função pesquisa_web
        bet_pergunta = ("O que deseja pesquisar? ")
        print(bet_pergunta)
        sintese_voz(bet_pergunta)
        pesquisando = True
        while pesquisando:
            termo_busca = ouvir_microfone()  # armazena na variável busca o que foi retornado da função ouvir_microfone
            if termo_busca != 'Não entendi!':
                bet_avisa = (f'Estes são os resultados para: {termo_busca}')
                sintese_voz(bet_avisa)
                print(f'{bet_avisa}')         #confirma para o usuário o que foi dito
                print(pesquisa_web(termo_busca))
                abrindo_sites = True
                while abrindo_sites:
                    bet_pergunta = "Deseja abrir algum destes sites?"
                    sintese_voz(bet_pergunta)
                    print(bet_pergunta)
                    resposta = ouvir_microfone()
                    if encontrar_comando('sim', resposta):
                        respondendo = True
                        while respondendo:
                            bet_pergunta = 'Qual destes sites deseja abrir?'
                            sintese_voz(bet_pergunta)
                            resposta = ouvir_microfone()
                            if encontrar_comando('primeiro', resposta):
                                abrir_site(pesquisa_web(termo_busca)[0])
                                respondendo = False
                            elif encontrar_comando('segundo', resposta):
                                abrir_site(pesquisa_web(termo_busca)[1])
                                respondendo = False
                            elif encontrar_comando('terceiro', resposta):
                                abrir_site(pesquisa_web(termo_busca)[2])
                                respondendo = False
                            elif encontrar_comando('quarto', resposta):
                                abrir_site(pesquisa_web(termo_busca)[3])
                                respondendo = False
                            else:
                                sintese_voz('Não entendi, tente novamente!')
                                respondendo = True
                    elif encontrar_comando('não', resposta):
                        abrindo_sites = False
                    else:
                        sintese_voz('Não ententi, tente novamente!')
                        abrindo_sites = True
                    pesquisando = False
            else:
                sintese_voz('Não entendi, tente novamente!')
                pesquisando = True

    elif encontrar_comando('obrigado', frase):       #comando de voz que encerra o programa
        ouvindo = False

    else:                           #ouve e imprime o que foi dito indefinidamente até que algum comando seja entendido
        sintese_voz(frase)
        print(frase)


bet_final = "Foi um prazer ajudá-lo!!"
sintese_voz(bet_final)
print(bet_final)