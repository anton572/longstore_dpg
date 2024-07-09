from lib_program.Acthion import Acthion
# лезь суда только в крайнем случае
class ScreenSwaper():
    def __init__(self):
        self.__screen={}
        self.Swap=Acthion()
        self.__screenOld=None
    def Add(self,ScreenClass):
        name=id(ScreenClass)
        self.__screen[name] = ScreenClass
        return lambda :self.__set(name)
    def __set(self,name):
        screen=self.__screen[name]
        self.Swap.invoke(self.__screenOld,screen)
        self.__screenOld=screen
