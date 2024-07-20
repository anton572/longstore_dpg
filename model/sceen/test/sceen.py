
#сценна с двумя кнопками
from abstract.screen import BasicSceen
from model.Model import ModelScreen



class sceen(BasicSceen):
    def __init__(self, model:ModelScreen=None):
        super().__init__(model)
        fo="""frttrewa [{damage}1d6] dfge [1d4] t"""
        label = model.Fabric.Lableformul(fo)
        self._add(label)
