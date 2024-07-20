from viw.LableConstruct import LableConstruct



class fabric():
    def __init__(self, model,input_formul):
        self.model=model
        self.__input_formul=input_formul
    def Lableformul(self,text):
        layout=LableConstruct(text)
        def set(text):
            layout.setText(text)
        def createSceen(instans):

            input=self.__input_formul(set,layout.getText(),model=self.model)
            self.model.addRelated(input)
        layout.bind(on_press=createSceen)

        return layout
