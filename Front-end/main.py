from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class sm(ScreenManager):

    contFutebol = 0 #Contador para menu do futebol
    contVolei = 0
    contBasquete = 0
    contCs = 0

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
            texto = Label(text='Conteudo Futebol', size_hint_y = None)
            self.get_screen('sobre').ids.futebol.add_widget(texto)
            self.contFutebol +=1
        else:
            self.get_screen('sobre').ids.futebol.clear_widgets()
            self.contFutebol = 0
    
    #Página Sobre Esportes

    def Volei(self):
        if(self.contVolei==0): #Verifica se é a primeira vez que o botão está sendo apertado
            texto2 = Label(text='Conteudo Volei', size_hint_y = None)
            self.get_screen('sobre').ids.volei.add_widget(texto2)
            self.contVolei +=1
        else:
            self.get_screen('sobre').ids.volei.clear_widgets()
            self.contVolei = 0
    
    def Basquete(self):
        if(self.contBasquete==0): #Verifica se é a primeira vez que o botão está sendo apertado
            texto3 = Label(text='Conteudo Basquete', size_hint_y = None)
            self.get_screen('sobre').ids.basquete.add_widget(texto3)
            self.contBasquete +=1
        else:
            self.get_screen('sobre').ids.basquete.clear_widgets()
            self.contBasquete = 0
    
    def Cs(self):
        if(self.contCs==0): #Verifica se é a primeira vez que o botão está sendo apertado
            texto4 = Label(text='Conteudo de CS', size_hint_y = None)
            self.get_screen('sobre').ids.cs.add_widget(texto4)
            self.contCs +=1
        else:
            self.get_screen('sobre').ids.cs.clear_widgets()
            self.contCs = 0

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