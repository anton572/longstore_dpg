from SceenApp import SceenApp
from model.scree.screen.screen import screen
from model.Model import ModelScreen
class main(SceenApp):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def ModellInit(self):
        self.model_screen=ModelScreen(self.ScreenSwaper)
        sceen = screen(model=self.model_screen)
        linkToScreen=self.ScreenSwaper.add(sceen)
        # linkToScreen это функция при вызове которой мы переходим в sceen
        self.start+=linkToScreen
if __name__ == '__main__':
    main().run()

