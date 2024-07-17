from kivy.uix.label import Label
from fabric.generate import formul
from lib_program.Acthion import Acthion
class LableFormul(Label):
    def __init__(self,text,size=26,**kwargs):
        self.__text=text
        super().__init__(text=formul(self.__text), markup=True, font_size=size, **kwargs)
        self.clic_math=Acthion()
        self.bind(on_ref_press=self._handler)
    def _handler(self,instance, ref):
        self.clic_math.invoke(ref)
    def setText(self,text):
        self.__text=text
        self.text=formul(self.__text)
    def getText(self):
        return self.__text
