from lib_program.Acthion import Acthion
from abstract.screen import RelatedSceen,BasicSceen
# лезь суда только в крайнем случае
class ScreenSwaper():
    def __init__(self):
        self.__screen={}
        self.Swap=Acthion()
        self.__screenOld=None
        self.__related=[]
    def addRelated(self, Screen:RelatedSceen):
        if isinstance(Screen, RelatedSceen):
            raise ValueError("not RelatedScreen")
        self.__related.append(self.__screenOld)
        self.__setScreen(Screen)
    def UpRelated(self):
        obj=self.__related[-1]
        self.__related.remove(obj)
        self.__setScreen(obj)
    def add(self, ScreenClass:BasicSceen):
        if type(ScreenClass)==BasicSceen:
            raise ValueError("not BasicScreen")
        name=id(ScreenClass)
        self.__screen[name] = ScreenClass
        return lambda :self.__set(name)
    def __setScreen(self,Screen):
        screen=Screen
        self.Swap.invoke(self.__screenOld,screen)
        self.__screenOld=screen
    def __set(self,name):
        screen=self.__screen[name]
        self.__setScreen(screen)
