from abstract.screen import IScreen
from kivy.uix.boxlayout import BoxLayout
from viw.LableFormul import LableFormul
from kivy.uix.textinput import TextInput
from fabric.ui import generate_formul
#сценна с двумя кнопками
class screen(IScreen):
    def __init__(self,name1,name2):
        layout = BoxLayout(padding=10)
        self.__layout=layout
        fo="""frttrewa [math]{name}d d[/math] dfge [math]d [/math]"""
        print(fo)
        label = LableFormul(
            text=fo,
            size=24
        )
        label.clic_math+=self.on_ref_press
        self._add(label)
    def _add(self,element):
        self.__layout.add_widget(element)
        return self
    def on_ref_press(self, ref):
        print(ref)
    #возврощает видимость сценны
    def GetSerf(self):
        return self.__layout
    def Lode(self,lode):pass
    def Damp(self):pass
