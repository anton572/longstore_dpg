from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
class main(App):
    def build(self):
        super().build()
        layout = BoxLayout(padding=10)
        layout.add_widget(Button(text='des'))
        layout.add_widget(Button(text='res'))
        return layout
if __name__ == '__main__':
    main().run()

