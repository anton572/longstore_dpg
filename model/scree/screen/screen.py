
from viw.LableFormul import LableFormul
#сценна с двумя кнопками
from abstract.screen import BasicScreen
from model.Model import ModelScreen
from fabric.ui import fabric
class screen(BasicScreen):
    def __init__(self, model:ModelScreen=None):
        super().__init__(model)
        self.fabric=fabric(model)
        fo="""frttrewa [math]{damage}1d6[/math] dfge [math]1d4 [/math] t"""
        print(fo)
        label = self.fabric.Lableformul(fo)
        label.clic_math+=self.on_ref_press
        self._add(label)
    def on_ref_press(self, ref):
        print(ref)
