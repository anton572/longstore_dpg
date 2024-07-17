from lib_program.abstraction import Interference
from model.Model import ModelScreen
from kivy.uix.boxlayout import BoxLayout
# интерфейс сценны обязан наледовать от него сценны
class IScreen(Interference):
    def GetSerf(self):pass
class BasicScreen(IScreen):
    def __init__(self, model:ModelScreen=None):
        self.model=model
        layout = BoxLayout(padding=10)
        self.__layout=layout
    def _add(self,element):
        self.__layout.add_widget(element)
        return self
    #возврощает видимость сценны
    def GetSerf(self):
        return self.__layout
class RelatedScreen(BasicScreen):pass
