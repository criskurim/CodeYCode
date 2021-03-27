from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout

class sm(ScreenManager):
    def MudarPagina2(self):
        self.current = 'p2'
        self.nome = self.get_screen('pinicial').ids.nome.text
        self.email = self.get_screen('pinicial').ids.email.text
        self.get_screen('p2').ids.nome2.text = f'Olá {self.nome}, seu email: {self.email}'
        
 
    def MudarPaginaInicial(self):
        self.current = 'pinicial'

class PaginaInicial(Screen):
    pass

class Pagina2(Screen):
    pass

class Tarefa(BoxLayout):
    def __init__(self,text='',**kwargs):
        super().__init__(**kwargs)
        self.ids.nome2.text = text



class teste(App):
    def build(self):
        return sm()

if __name__ == "__main__":
    teste().run()