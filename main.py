from kivy.core.window import Window
Window.size = (94*6, 151*6)
from SceenApp import SceenApp
from model.sceen.test.sceen import sceen as test
from model.sceen.atributs.sceen import sceen as Atribut
from model.Model import ModelScreen
from model.Player.Player import Player
class main(SceenApp):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    def ModellInit(self):

        self.model_screen=ModelScreen(ScreenSwaper=self.ScreenSwaper,Massage=self.massage)
        sceen = test(model=self.model_screen)
        sceenAtribut = Atribut(model=self.model_screen)
        linkToTest=self.ScreenSwaper.add(sceen)
        linkToAtribut=self.ScreenSwaper.add(sceenAtribut)
        # linkToScreen это функция при вызове которой мы переходим в sceen
        self.start+=linkToAtribut

        player=Player()
        self.model_screen.setPlayer(player)
if __name__ == '__main__':


    main().run()

