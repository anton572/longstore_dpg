from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
class Massage(BoxLayout):
    def __init__(self):
        super().__init__(padding=0,orientation='vertical',pos_hint={'x':0.,'y':0.},size_hint=(None,None),size=(200,120))
    def add_widget(self, text):
        if len(self.children)==6:
            self.remove_widget(self.children[-1])
        Layout=BoxLayout(padding=0,size_hint=(None,None),size=(220,30))
        label=Label(text=text,size_hint_x=0.7)
        button=Button(text='x',size_hint_x=0.3)
        Layout.add_widget(label)
        Layout.add_widget(button)
        button.bind(on_press=lambda instans:self.remove_widget(Layout))
        super().add_widget(Layout)
