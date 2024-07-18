

class ModelScreen():
    def __init__(self,ScreenSwaper,Massage):
        self.__screenSwaper=ScreenSwaper
        self.__massage=Massage
    def addMessage(self,text:str):
        if not isinstance(text,str):
            raise ValueError("not string")
        self.__massage.add_widget(text)
    def UpRelated(self):
        self.__screenSwaper.UpRelated()
    def addRelated(self,Screen):
        self.__screenSwaper.addRelated(Screen)
