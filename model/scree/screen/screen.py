
from model.Atribut import Atribut
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
        fo="""frttrewa [{damage}1d6] dfge [1d4] t"""
        label = self.fabric.Lableformul(fo)
        label.clic_math+=self.on_ref_press
        self._add(label)
        at=Atribut('тело',['Координация','Сила','Скорость реакции'])
        at
        #self._add(at)
    def on_ref_press(self, ref):
        val,ex=self.math.colculate(ref)
        print(ref,val,ex)
        self.model.addMessage(f"{ex}={val}")
