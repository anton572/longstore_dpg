from abstract.screen import BasicScreen
from model.Model import ModelScreen
class screen(BasicScreen):
    def __init__(self, model:ModelScreen=None):
        super().__init__(model)

