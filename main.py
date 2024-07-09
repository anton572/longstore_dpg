from SceenApp import SceenApp
from model.screen.screen import screen
class main(SceenApp):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def ModellInit(self):
        sceen = screen('der','sor')
        linkToScreen=self.ScreenSwaper.Add(sceen)
        # linkToScreen это функция при вызове которой мы переходим в sceen
        self.start+=linkToScreen
if __name__ == '__main__':
    main().run()

