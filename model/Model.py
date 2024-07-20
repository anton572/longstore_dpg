from lib_program.Acthion import Acthion

class ModelScreen():
    def __init__(self,ScreenSwaper,Massage):
        self.__screenSwaper=ScreenSwaper
        self.__massage=Massage
        self.__player=None
        self.changePlayer=Acthion()
    def setPlayer(self,player):
        self.__player=player
        self.changePlayer.invoke(player)
    def addMessage(self,text:str):
        if not isinstance(text,str):
            raise ValueError("not string")
        self.__massage.add_widget(text)
    def UpRelated(self):
        self.__screenSwaper.UpRelated()
    def addRelated(self,Screen):
        self.__screenSwaper.addRelated(Screen)
