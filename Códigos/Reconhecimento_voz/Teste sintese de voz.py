
import pyttsx3
falar = pyttsx3.init('sapi5')


def sintese_voz(entrada_de_texto):
    falar.say(entrada_de_texto)
    falar.runAndWait()


while True:
    frase = input("Digite algo a ser dito: ")
    sintese_voz(frase)