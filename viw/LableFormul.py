from kivy.uix.label import Label
from fabric.ui import generate_formul
from lib_program.Acthion import Acthion
class LableFormul(Label):
    def __init__(self,text,size=26):
        self.__text=text
        super().__init__(text=generate_formul(self.__text),markup=True,font_size=size)
        self.clic_math=Acthion()
        self.bind(on_ref_press=self._handler)
    def _handler(self,instance, ref):
        self.clic_math.invoke(ref)
    def setText(self,text):
        self.__text=text
        self.text=generate_formul(self.__text)
    def getText(self):
        return self.__text
