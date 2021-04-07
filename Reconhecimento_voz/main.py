
import speech_recognition as sr
import googlesearch
from googlesearch import search

#Link vídeo com código rodando: (https://www.youtube.com/watch?v=Z1fEd-TP4zY)
#reconhecedor


#função para ouvir o microfone
def ouvir_microfone():
    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        #print("Diga alguma coisa: ")
        audio = microfone.listen(source)
        try:
            frase = microfone.recognize_google(audio, language='pt-BR')
            #print('Você disse: ' + frase)
            return frase
        except sr.UnknownValueError:
            #print("Não entendi!")
            return "Não entendi!"




#loop para ouvir continuamente
ouvindo = True
while ouvindo:
    print("Diga alguma coisa: ") #solicita que o usuária diga algo
    ouvir_microfone() #aciona a função ouvir_microfone()
    frase = ouvir_microfone() #armazena em uma variável o que foi retornado da função
    if frase == "Oi Bete": #condição para entrar o comando pesquisar
        print("O que deseja pesquisar? ")
        busca = ouvir_microfone() #armazena na variável busca o que foi retornado da função ouvir_microfone
        print(f'Estes são os resultados para: {busca}') #confirma para o usuário o que foi dito
        for i in search(busca, tld="com", num=10, stop=10, pause=2):#realiza a pesquisa
            print(i) #inprime os resultados

    elif frase == "parar":#comando de voz que encerra o programa
        print("O programa encerrou!!")
        ouvindo = False
    else: #imprime sempre que não atende a nenhuma condição
        print('Você disse: ' + frase)








