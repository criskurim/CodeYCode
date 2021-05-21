
#Bibliotecas demandadas pelo programa
import speech_recognition as sr
from googlesearch import search
import pyttsx3
import webbrowser
import agenda_c_bd

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
    pesquisa = search(termo, num_results=3)
    for i in pesquisa:
        list_sites_resultados.append(i)
    return list_sites_resultados

def abrir_site(site):
    webbrowser.open(site, new=0, autoraise=True)

def verificar_data(dia, mes, ano):
    data = f"{ano}"

def consulta_time(time, list):  
    if time in list:
        return True
    else:
        return False
# listas de clubes brasileiros para referência

list_times = ['América mineiro', 'Athletico paranaense', 'Atlético goianiense', 'Atlético mineiro', 'Bahia', 'Bragantino', 'Ceará', 'Chapecoense', 'Corinthians', 'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Grêmio', 'Internacional', 'Juventude', 'Palmeiras', 'Santos', 'São Paulo', 'Sport', 'Avaí', 'Botafogo', 'Brasil de Pelotas', 'Brusque', 'CRB', 'CSA', 'Confiança', 'Coritiba', 'Cruzeiro', 'Goiás', 'Guarani', 'Londrina', 'Náutico', 'Operário', 'Ponte Preta', 'Remo', 'Sampaio Corrêa', 'Vasco', 'Vila Nova', 'Vitória']

# início do programa
bet_inicio = "Olá, eu sou Bet, sua assistente virtual!"

print(bet_inicio)
sintese_voz(bet_inicio)

#loop para ouvir continuamente
ouvindo = True

while ouvindo:
    bet_diz = 'Dê um comando!'
    print(bet_diz)                                   #solicita que o usuária diga algo
    sintese_voz(bet_diz)
    frase = ouvir_microfone()                        #aciona a função ouvir_microfone() e armazena em uma variável o que foi retornado da função

    if encontrar_comando('pesquisa', frase):         #condição para realizar a função pesquisa_web
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
                                pesquisando = False
                            elif encontrar_comando('segundo', resposta):
                                abrir_site(pesquisa_web(termo_busca)[1])
                                respondendo = False
                                pesquisando = False
                            elif encontrar_comando('terceiro', resposta):
                                abrir_site(pesquisa_web(termo_busca)[2])
                                respondendo = False
                                pesquisando = False
                            elif encontrar_comando('quarto', resposta):
                                abrir_site(pesquisa_web(termo_busca)[3])
                                respondendo = False
                                pesquisando = False
                                
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
    

    #Agenda
    elif encontrar_comando('agenda', frase):
        bet_pergunta = ("Aqui está sua agenda completa de jogos: ")
        print(bet_pergunta)
        sintese_voz(bet_pergunta)

        agenda_c_bd.exibir_agenda()

        while True:

            bet_pergunta = ("O que deseja realizar com a agenda: ")
            print(bet_pergunta)
            sintese_voz(bet_pergunta)

            termo_busca = ouvir_microfone()


            if(encontrar_comando('inserir', termo_busca)):

                bet_pergunta = ("Digite a data do jogo:  ")
                print(bet_pergunta)
                sintese_voz(bet_pergunta)

                data = str(input('Data (dd/mm/aaaa): '))
                    

                bet_pergunta = ("Digite o horario do jogo? ")
                print(bet_pergunta)
                sintese_voz(bet_pergunta)

                horario = str(input('Horario (hh:mm): '))

                bet_pergunta = ("Fale o nome do primeiro time que irá jogar:  ")
                print(bet_pergunta)
                sintese_voz(bet_pergunta)

                time1 = ouvir_microfone()

                bet_pergunta = ("Fale o nome do segundo time que irá jogar:  ")
                print(bet_pergunta)
                sintese_voz(bet_pergunta)

                time2 = ouvir_microfone()

                print(f'{time1} x {time2}')
                print(f'{data} --- {horario}')


                while True:
                    bet_pergunta = ("Deseja inserir esse jogo na agenda? ")
                    print(bet_pergunta)
                    sintese_voz(bet_pergunta)

                    resposta = ouvir_microfone()

                    if(encontrar_comando('sim', resposta)):
                        agenda_c_bd.inserir_na_agenda(time1, time2, data, horario)
                        break
                    elif(encontrar_comando('não', resposta)):
                        break
                    else:
                        continue
                
                break
            elif(encontrar_comando('deletar', termo_busca)):

                bet_pergunta = ("Digite o código do jogo para deletar: ")
                print(bet_pergunta)
                sintese_voz(bet_pergunta)

                cod_deletar = str(input('Código: '))

                agenda_c_bd.deletar_na_agenda(cod_deletar)
                
                break
            else:
                continue

        #busca por notícias(globo esporte)
    elif (encontrar_comando('notícia', frase)):
        busca_noticias = True
        while busca_noticias:
            bet_diz = 'Deseja receber notícias sobre qual time? '
            sintese_voz(bet_diz)
            time = ouvir_microfone()
            
            if consulta_time(time, list_times):
                bet_diz = 'Você escolheu: ', time
                sintese_voz(bet_diz)
                site_noticias = f'https://globoesporte.globo.com/busca/?q={time}'
                abrir_site(site_noticias)
                busca_noticias = False
            else:
                bet_avisa = 'Não entendi qual o time você escolheu! Repita, por favor!'
                sintese_voz(bet_avisa)
                busca_noticias = True
        
        #busca por vídeos(youtube)
    elif (encontrar_comando('vídeo', frase)):
        
        busca_videos = True
        while busca_videos:
            bet_diz = 'Deseja assistir vídeos sobre qual time? '
            sintese_voz(bet_diz)
            time = ouvir_microfone()
            if consulta_time(time, list_times):
                bet_diz = 'Você escolheu: ', time
                sintese_voz(bet_diz)
                site_videos = f'www.youtube.com/results?search_query={time}'
                abrir_site(site_videos)
                busca_videos = False
            else:
                bet_avisa = 'Não entendi qual o time você escolheu! Repita, por favor!'
                sintese_voz(bet_avisa)
                busca_videos = True

        #busca por memes (ole do brasil)
    elif (encontrar_comando('meme', frase)):
        busca_memes = True
        while busca_memes:
            bet_diz = 'Deseja visualizar memes sobre qual time? '
            sintese_voz(bet_diz)
            time = ouvir_microfone()
            if consulta_time(time, list_times):
                bet_diz = 'Você escolheu: ', time
                sintese_voz(bet_diz)
                site_memes = f'https://oledobrasil.com.br/?s={time}'
                abrir_site(site_memes)
                busca_memes = False
            else:
                bet_avisa = 'Não entendi qual o time você escolheu! Repita, por favor!'
                sintese_voz(bet_avisa)
                busca_memes = True
        
        #ouve e imprime o que foi dito indefinidamente até que algum comando seja entendido
    else:                
        sintese_voz(frase)
        print(frase)


bet_final = "Foi um prazer ajudá-lo!!"
sintese_voz(bet_final)
print(bet_final)