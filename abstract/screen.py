from lib_program.abstraction import Interference
from kivy.uix.boxlayout import BoxLayout
# интерфейс сценны обязан наледовать от него сценны
class ISceen(Interference):
    def GetSerf(self):pass
class BasicSceen(ISceen):
    def __init__(self, model):
        self.model=model
        layout = BoxLayout(padding=10,orientation='vertical')
        self.__layout=layout
    def _add(self,element):
        self.__layout.add_widget(element)
        return self
    #возврощает видимость сценны
    def GetSerf(self):
        return self.__layout
class RelatedSceen(BasicSceen):pass
