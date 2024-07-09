from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import model
from lib_program.Acthion import Acthion
from abstract.screen import IScreen
class SceenApp(App):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.ScreenSwaper=model.ScreenSwaper()
        self.ScreenSwaper.Swap+=self.__Swap
        self.start=Acthion()
        self.ModellInit()
        self.layout = BoxLayout(padding=0)
    def ModellInit(self):pass
    def __Swap(self,OldSceen:IScreen,NewSceen:IScreen):
        """меняет сценны"""
        self.layout.add_widget(NewSceen.GetSerf())
        if OldSceen!=None:
            self.layout.remove_widget(OldSceen.GetSerf())
    def build(self):
        super().build()
        self.start.invoke()
        return self.layout
