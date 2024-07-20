from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

import model.Player.Player
from lib_program.Acthion import Acthion
class Show(BoxLayout):
    def __init__(self,ind=0,**kwargs):
        super().__init__(**kwargs)
        self.element=[[] for i in range(ind)]
        self.inde=None
        self.show(0)
    def add(self,indax, widget):
        self.element[indax].append(widget)
        if indax==self.inde:
            self.add_widget(widget)
    def show(self,index):
        if self.inde!=None:
            for i in self.element[self.inde]:
                self.remove_widget(i)
        for i in self.element[index]:
            self.add_widget(i)
        self.inde=index
class CounterRow(BoxLayout):
    def __init__(self, name, **kwargs):
        super().__init__(orientation='horizontal', **kwargs)

        name_label = Label(
            text=name,
            size_hint_x=0.3,
            halign='left',
            valign='middle',
            text_size=(self.width, None)
        )

        decrement_button = Button(text="[-]", size_hint_x=0.1)
        self.__counter_label = Label(text="0", size_hint_x=0.1)
        increment_button = Button(text="[+]", size_hint_x=0.1)
        self.__bonus = Label(text="", size_hint_x=None)
        decrement_button.bind(on_press=lambda i:self.__decrement())
        increment_button.bind(on_press=lambda i:self.__increment())
        box=Show(2)

        box.add(0,decrement_button)
        box.add(0, self.__counter_label)
        box.add(0,increment_button)
        box.add(0,self.__bonus)
        self.__box=box
        box.add(1, self.__counter_label)
        box.add(1,self.__bonus)
        self.add_widget(name_label)
        self.add_widget(box)
        self.change=Acthion()
        self.setRange(-2, 12)
    def setRange(self, min=None, max=None):
        self.min=min
        self.max=max
    def __increment(self):
        value=self.getValue()+1
        if value>self.max:
            value = self.max
        self.setText(value)
        self.change.invoke(value)
    def __decrement(self):
        value=self.getValue()-1
        if value<self.min:
            value = self.min
        self.setText(value)
        self.change.invoke(value)
    def setBound(self,value):
        if not isinstance(value,int):
            raise ValueError("not int")
        value=str(value)
        if value=='0':
            value=''
        if not '-' in value and value != '':
            value='+'+value
        self.__bonus.text=value
    def getValue(self):
        return int(self.__counter_label.text)
    def setText(self,value):
        self.__counter_label.text=str(value)
    def setValue(self,value:model.Player.Parameters.Value):
        self.setText(value.value)
        self.setBound(value.bonus)
    def edit(self,mod=False):
        self.__box.show(int(mod))
class Atribut(BoxLayout):
    def __init__(self, main_name, names,number=0, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        top_layout = BoxLayout()
        self.number=number
        label_name = Label(
            text=main_name,
            font_size=24,
            size_hint=(None, 1)
        )
        self.label_count = Label(
            text=f'{self.number}(0/{self.number*2})',
            font_size=24,
            size_hint=(None, 1)
        )
        top_layout.add_widget(label_name)
        top_layout.add_widget(self.label_count)
        self.__rows=[]
        self.add_widget(top_layout)
        for name in names:
            __row= CounterRow(name)
            self.add_widget(__row)
            self.__rows.append(__row)
        self.change=Acthion()
        for i in self.__rows:
            i.change+=lambda v:self.__updateStait()
        self.res=0
    def getValue(self):
        return self.number
    def setCount(self,number,res):
        self.number=number
        self.res=res
        self.label_count.text=f'{self.number}({self.res}/{self.number*2})'

    def setValue(self,Atribut:model.Player.Parameters.Atribut):
        for i in range(3):
            self.__rows[i].setValue(Atribut.values[i])
        self.setCount(Atribut.stronger,self.res)

    def __updateStait(self):
        res=sum(map(lambda i:i.getValue(),self.__rows))
        self.setCount(self.number,res)
    def edit(self,mod):
        for i in self.__rows:
            i.edit(mod)

class Parameters(BoxLayout):
    def __init__(self):
        super().__init__(orientation='vertical')
        self.body=Atribut('Тела',['Координация','Сила','Скорость реакции'],padding=2)
        self.intilegent=Atribut('разума',['Интеллект','Знания','Хитрость'],padding=2)
        self.mental=Atribut('духа',['Обаяние','Воля','мудрость'],padding=2)
        self.Wildness=Atribut("Дикости",['Восприятие','Подавление','Выносливость'],padding=2)

        atributs=BoxLayout(orientation='vertical')
        for i in [self.body,self.intilegent,self.mental,self.Wildness]:
            atributs.add_widget(i)
        self.add_widget(atributs)
    def edit(self,mod=False):
        for i in [self.body,self.intilegent,self.mental,self.Wildness]:
            i.edit(mod)
    def setPlayer(self,player:model.Player.Player.Player):
        parameters=player.parameters
        self.body      .setValue(parameters.body)
        self.intilegent.setValue(parameters.intilegent)
        self.mental    .setValue(parameters.mental)
        self.Wildness  .setValue(parameters.Wildness)



