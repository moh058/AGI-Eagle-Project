from kivy.app import App
from kivy.uix.label import Label

class AGIApp(App):
    def build(self):
        return Label(text='Eagle Eye AGI: System Online!')

if __name__ == '__main__':
    AGIApp().run()
