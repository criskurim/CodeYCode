from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class sm(ScreenManager):
    contFutebol = 0  # Contador para menu do futebol
    contVolei = 0
    contMeme1 = 0
    contmeme2 = 0
    conttecnico = 0
    contjogadores = 0

    def MudarMenu(self):
        self.current = 'menu'
        # self.nome = self.get_screen('pinicial').ids.nome.text
        # self.email = self.get_screen('pinicial').ids.email.text
        # self.get_screen('menu').ids.infos.text = f'Olá {self.nome}, seu email: {self.email}'

    def MudarPaginaInicial(self):
        self.current = 'pinicial'

    def MudarPaginaSobreEsportes(self):
        self.current = 'sobre'

    def Futebol(self):
        if (self.contFutebol == 0):  # Verifica se é a primeira vez que o botão está sendo apertado
            texto = Label(text='Conteudo Futebol')
            self.get_screen('sobre').ids.futebol.add_widget(texto)
            self.contFutebol += 1
        else:
            self.get_screen('sobre').ids.futebol.clear_widgets()
            self.contFutebol = 0

    def Volei(self):
        if (self.contVolei == 0):  # Verifica se é a primeira vez que o botão está sendo apertado
            texto2 = Label(text='Conteudo Volei')
            self.get_screen('sobre').ids.volei.add_widget(texto2)
            self.contVolei += 1
        else:
            self.get_screen('sobre').ids.volei.clear_widgets()
            self.contVolei = 0


    def Meme1(self):
        if (self.contMeme1 == 0):  # Verifica se é a primeira vez que o botão está sendo apertado
            texto = Label(text='meme1')
            self.get_screen('memes').ids.meme1.add_widget(texto)
            self.contMeme1 += 1
        else:
            self.get_screen('memes').ids.meme1.clear_widgets()
            self.contMeme1 = 0

    def Meme2(self):
        if (self.contmeme2 == 0):  # Verifica se é a primeira vez que o botão está sendo apertado
            texto2 = Label(text='meme2')
            self.get_screen('memes').ids.meme2.add_widget(texto2)
            self.contmeme2 += 1
        else:
            self.get_screen('memes').ids.meme2.clear_widgets()
            self.contmeme2 = 0


    def MudarPaginaInfoTime(self):
        self.current = 'Infotime'

    def tecnico(self):
        if (self.conttecnico == 0):  # Verifica se é a primeira vez que o botão está sendo apertado
            texto = Label(text='tecnico')
            self.get_screen('Infotime').ids.tecnico.add_widget(texto)
            self.conttecnico += 1
        else:
            self.get_screen('Infotime').ids.tecnico.clear_widgets()
            self.conttecnico = 0

    def jogadores(self):
        if (self.contjogadores == 0):  # Verifica se é a primeira vez que o botão está sendo apertado
            texto2 = Label(text='jogadores')
            self.get_screen('Infotime').ids.jogadores.add_widget(texto2)
            self.contjogadores += 1
        else:
            self.get_screen('Infotime').ids.jogadores.clear_widgets()
            self.contjogadores = 0


    def MudarPaginaMemes(self):
        self.current = 'memes'



class PaginaInicial(Screen):
    pass


class MenuInicial(Screen):
    pass


class SobreEsportes(Screen):
    pass

class Memes(Screen):
    pass

class InfoTime(Screen):
    pass

class teste(App):
    def build(self):
        return sm()


if __name__ == "__main__":
    teste().run()