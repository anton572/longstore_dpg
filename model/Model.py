from lib_program.Acthion import Acthion
from fabric.ui import fabric
from model.math import math
from model.sceen.input_formul.sceen import sceen as input_formul
class Fabric():
    def __init__(self,model):
        self.fabric=fabric(model,input_formul)
        self.model=model

    def Lableformul(self,text):
        Lableformul=self.fabric.Lableformul(text)
        Lableformul.clic_math+=self.on_ref_press
        return Lableformul
    def on_ref_press(self, ref):
        val,ex=self.model.math.colculate(ref)
        self.model.addMessage(f"{ex}={val}")
class ModelScreen():
    def __init__(self,ScreenSwaper,Massage):
        self.__screenSwaper=ScreenSwaper
        self.__massage=Massage
        self.__player=None
        self.math=math()
        self.changePlayer=Acthion()
        self.Fabric=Fabric(self)
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
