from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
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

        decrement_button.bind(on_press=lambda i:self.__decrement())
        increment_button.bind(on_press=lambda i:self.__increment())
        box=Show(2)

        box.add(0,decrement_button)
        box.add(0, self.__counter_label)
        box.add(0,increment_button)
        self.__box=box
        box.add(1, self.__counter_label)
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
        self.__counter_label.text=str(value)
        self.change.invoke(value)
    def __decrement(self):
        value=self.getValue()-1
        if value<self.min:
            value = self.min
        self.__counter_label.text=str(value)
        self.change.invoke(value)
    def getValue(self):
        return int(self.__counter_label.text)
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
            size_hint=(None, None)
        )
        self.label_count = Label(
            text=f'{self.number}(0/{self.number*2})',
            font_size=24,
            size_hint=(None, None)
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
    def __updateStait(self):
        res=sum(map(lambda i:i.getValue(),self.__rows))
        self.label_count.text=f'{self.number}({res}/{self.number*2})'
    def edit(self,mod):
        for i in self.__rows:
            i.edit(mod)

