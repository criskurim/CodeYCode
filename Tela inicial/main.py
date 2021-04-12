from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class sm(ScreenManager):

    contFutebol = 0 #Contador para menu do futebol
    contVolei = 0

    def MudarMenu(self):
        self.current = 'menu'
        #self.nome = self.get_screen('pinicial').ids.nome.text
        #self.email = self.get_screen('pinicial').ids.email.text
        #self.get_screen('menu').ids.infos.text = f'Olá {self.nome}, seu email: {self.email}'
        
 
    def MudarPaginaInicial(self):
        self.current = 'pinicial'

    def MudarPaginaSobreEsportes(self):
        self.current = 'sobre'

    def Futebol(self):
        if(self.contFutebol==0): #Verifica se é a primeira vez que o botão está sendo apertado
            texto = Label(text='Conteudo Futebol')
            self.get_screen('sobre').ids.futebol.add_widget(texto)
            self.contFutebol +=1
        else:
            self.get_screen('sobre').ids.futebol.clear_widgets()
            self.contFutebol = 0

    def Volei(self):
        if(self.contVolei==0): #Verifica se é a primeira vez que o botão está sendo apertado
            texto2 = Label(text='Conteudo Volei')
            self.get_screen('sobre').ids.volei.add_widget(texto2)
            self.contVolei +=1
        else:
            self.get_screen('sobre').ids.volei.clear_widgets()
            self.contVolei = 0

class PaginaInicial(Screen):
    pass

class MenuInicial(Screen):
    pass

class SobreEsportes(Screen):
    pass



class teste(App):
    def build(self):
        return sm()

if __name__ == "__main__":
    teste().run()