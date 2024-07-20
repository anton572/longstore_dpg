from abstract.screen import BasicScreen
from model.Model import ModelScreen
from kivy.uix.boxlayout import BoxLayout
from model.Atribut import Parameters
from kivy.uix.checkbox import CheckBox
class screen(BasicScreen):
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
