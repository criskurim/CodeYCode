import speech_recognition as sr
import googlesearch

#Link vídeo com código rodando: (https://www.youtube.com/watch?v=Z1fEd-TP4zY)
#reconhecedor
microfone = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Diga alguma coisa: ")
        audio = microfone.listen(source)
        try:
            frase = microfone.recognize_google(audio, language='pt-BR')
            print('Você disse: ' + frase)
        except sr.UnknownValueError:
            print("Não entendi")
    if frase == "Oi Bete":
        print("O que deseja? ")
        audio = microfone.listen(source)
        try:
            frase = microfone.recognize_google(audio, language='pt-BR')
            print('Você disse: ' + frase)
            results = Google.search(frase)
            print(googlesearch.search(frase, num_results=10, lang="pt"))
        except sr.UnknownValueError:
            print("Não entendi")







