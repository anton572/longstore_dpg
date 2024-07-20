from abstract.screen import BasicScreen
from model.Model import ModelScreen
from kivy.uix.boxlayout import BoxLayout
from model.Atribut import Atribut
from kivy.uix.checkbox import CheckBox
class screen(BasicScreen):
    def __init__(self, model:ModelScreen=None):
        super().__init__(model)
        self.bodys=[]
        self.bodys.append(Atribut("тело",['res','ress','resss']))
        self.bodys.append(Atribut("Centered ",['res','ress','resss']))
        self.bodys.append(Atribut("тело",['res','ress','resss']))
        self.bodys.append(Atribut("тело",['res','ress','resss']))
        self.el=BoxLayout(padding=2,orientation='vertical')
        self.isedit=CheckBox()
        self.isedit.bind(active=self.edit)
        self.el.add_widget(self.isedit)
        for i in self.bodys:
            (body:=BoxLayout(padding=2,pos_hint={'center_x': 0.5})).add_widget(i)
            self.el.add_widget(body)

        self._add(self.el)
    def edit(self, checkbox, value):
        for i in self.bodys:
            i.edit(value)
