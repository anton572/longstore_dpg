from viw.LableFormul import LableFormul
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
class LableConstruct(BoxLayout):
    def __init__(self,text,**kwargs):
        super().__init__(**kwargs)
        label = LableFormul(
            text=text,
            size_hint_x=0.7
        )

        button = Button(
            text="...",
            size_hint_x=0.3
        )
        self.__label=label
        self.__button=button

        self.add_widget(label)
        self.add_widget(button)
        self.add_widget=None
        self.remove_widget=None
        self.clic_math=self.__label.clic_math
    def bind(self,on_press):
        self.__button.bind(on_press=on_press)
    def setText(self,text):
        self.__label.setText(text)
    def getText(self):
        return self.__label.getText()
