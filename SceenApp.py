from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from viw.massage import Massage
from model.ScreenSwaper import ScreenSwaper
from lib_program.Acthion import Acthion
from abstract.screen import ISceen
class SceenApp(App):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.ScreenSwaper=ScreenSwaper()
        self.ScreenSwaper.Swap+=self.__Swap
        self.start=Acthion()
        self.massage=Massage()
        self.ModellInit()
        self.grup = FloatLayout()

        self.layout=BoxLayout(padding=0)
        self.grup.add_widget(self.layout)
        self.grup.add_widget(self.massage)

    def ModellInit(self):pass
    def __Swap(self, OldSceen:ISceen, NewSceen:ISceen):
        """меняет сценны"""
        self.layout.add_widget(NewSceen.GetSerf())
        if OldSceen!=None:
            self.layout.remove_widget(OldSceen.GetSerf())
    def build(self):
        super().build()
        self.start.invoke()
        return self.grup
