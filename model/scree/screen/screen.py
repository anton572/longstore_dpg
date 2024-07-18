
from viw.LableFormul import LableFormul
#сценна с двумя кнопками
from abstract.screen import BasicScreen
from model.Model import ModelScreen
from model.math import math
from fabric.ui import fabric
class screen(BasicScreen):
    def __init__(self, model:ModelScreen=None):
        super().__init__(model)
        self.fabric=fabric(model)
        self.math=math()
        fo="""frttrewa [math]{damage}1d6[/math] dfge [math]1d4 [/math] t"""
        label = self.fabric.Lableformul(fo)
        label.clic_math+=self.on_ref_press
        self._add(label)
    def on_ref_press(self, ref):
        val,ex=self.math.colculate(ref)
        print(ref,val,ex)
        self.model.addMessage(f"{ex}={val}")
