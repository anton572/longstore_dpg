from abstract.screen import IScreen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
#сценна с двумя кнопками
class screen(IScreen):
    def __init__(self,name1,name2):
        layout = BoxLayout(padding=10)
        layout.add_widget(Button(text=name1))
        layout.add_widget(Button(text=name2))
        self.__layout=layout
    #возврощает видимость сценны
    def GetSerf(self):
        return self.__layout
    def Lode(self,lode):pass
    def Damp(self):pass
