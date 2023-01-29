from WordData import *

from kivymd.app import MDApp
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.app import App
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.bottomnavigation.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.bottomnavigation.bottomnavigation import TabbedPanelBase

easy = []
medium = []
hard = []


class MainApp(MDApp):
    def build(self):

        self.theme_cls.primary_palette = "Teal"

    def gen_word(self):
        if len(easy) > 0:
            self.easy = choice_word(word_classification()[0])
            self.root.ids.label.text = self.easy
        elif len(medium) > 0:
            self.medium = choice_word(word_classification()[1])
            self.root.ids.label.text = self.medium
        elif len(hard) > 0:
            self.hard = choice_word(word_classification()[2])
            self.root.ids.label.text = self.hard
        self.root.ids.acerto.text = ' '
        self.root.ids.erro.text = ' '
        
        

    def easy(self):
        
        if len(hard) > 0:
            hard.clear()
        if len(medium) > 0:
            medium.clear()
        easy.append(1)

    def medium(self):
        
        if len(easy) > 0:
            easy.clear()
        if len(hard) > 0:
            hard.clear()
        medium.append(1)

    def hard(self):
        

        if len(easy) > 0:
            easy.clear()
        if len(medium) > 0:
            medium.clear()
        hard.append(1)

    def word_verification(self):
        if self.root.ids.input.text == translate_to_portuguese(self.root.ids.label.text.lower()):
            self.root.ids.acerto.text = "Acertou!"
            self.root.ids.erro.text = ' '
        else:
            self.root.ids.erro.text = "Errou :("
            self.root.ids.acerto.text = ' '
            
            
        

    def init_audio(self):
        get_audio(self.root.ids.label.text, 'en')
        play_and_remove_audio()

    def translate(self):
        traduction = translate_to_portuguese(self.root.ids.label.text)
        
        return traduction.upper()
        
        
        
MainApp().run()
