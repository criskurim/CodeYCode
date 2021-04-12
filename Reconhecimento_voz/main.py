import speech_recognition as sr
from googlesearch import search
import pyttsx3




# Link vídeo com código rodando: (https://www.youtube.com/watch?v=Z1fEd-TP4zY)


# função para ouvir o microfone
def ouvir_microfone():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        audio = microfone.listen(source)
        try:
            frase = microfone.recognize_google(audio, language='pt-BR')
            return frase
        except sr.UnknownValueError:
            return "Não entendi!"


# função para sintetizar voz
def sintese_voz(entrada_de_texto):
    falar = pyttsx3.init('sapi5')
    falar.say(entrada_de_texto)
    falar.runAndWait()





# loop para ouvir continuamente
ouvindo = True
while ouvindo:
    bet_diz = 'Diga algo!'
    print(bet_diz)  # solicita que o usuária diga algo
    sintese_voz(bet_diz)
    ouvir_microfone()  # aciona a função ouvir_microfone()
    frase = ouvir_microfone()  # armazena em uma variável o que foi retornado da função
    frase = frase.lower()
    if frase == "poderia me ajudar":  # condição para entrar o comando pesquisar
        bet_diz = ("O que deseja pesquisar? ")
        print(bet_diz)
        sintese_voz(bet_diz)
        busca = ouvir_microfone()  # armazena na variável busca o que foi retornado da função ouvir_microfone
        bet_diz = (f'Estes são os resultados para: {busca}')
        sintese_voz(bet_diz)
        print(f'{bet_diz}')  # confirma para o usuário o que foi dito
        for i in search(busca, tld="com", num=4, stop=4, pause=2):  # realiza a pesquisa
            print (i)


    elif frase == "obrigado":  # comando de voz que encerra o programa
        bet_diz = "Foi um prazer ajudá-lo!!"
        sintese_voz(bet_diz)
        print(bet_diz)
        ouvindo = False
    else:  # imprime sempre que não atende a nenhuma condição
        bet_diz = (frase)
        sintese_voz(bet_diz)
        print(bet_diz)
