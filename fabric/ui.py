from viw.LableConstruct import LableConstruct
from model.scree.input_formul.screen import screen as input_formul


class fabric():
    def __init__(self, model):
        self.model=model
    def Lableformul(self,text):
        layout=LableConstruct(text)
        def set(text):
            layout.setText(text)
        def createSceen(instans):

            input=input_formul(set,layout.getText(),model=self.model)
            self.model.addRelated(input)
        layout.bind(on_press=createSceen)
        return layout
