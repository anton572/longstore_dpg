from abstract.screen import BasicSceen
from model.Model import ModelScreen
from kivy.uix.boxlayout import BoxLayout
from viw.Atribut import Parameters


class sceen(BasicSceen):
    def __init__(self, model:ModelScreen=None):
        super().__init__(model)
        self.el=BoxLayout(padding=2,orientation='vertical')
        self.Parameters=Parameters()
        self.el.add_widget(self.Parameters)
        model.changePlayer+=self.Parameters.setPlayer
        self._add(self.el)
    def edit(self, checkbox, value):
        for i in self.bodys:
            i.edit(value)
