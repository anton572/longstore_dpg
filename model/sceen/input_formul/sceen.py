from abstract.screen import BasicSceen
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
class sceen(BasicSceen):
    def __init__(self, setText,text,model):
        super().__init__(model)
        self.setText=setText
        self.TextInput=TextInput(text=text)
        self.Button=Button(text='close')
        self.Button.bind(on_press=lambda instans:self.close())

        self._add(self.TextInput)
        self._add(self.Button)
    def close(self):
        self.model.UpRelated()
        self.save()
    def save(self):
        self.setText(self.TextInput.text)
