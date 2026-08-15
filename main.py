from kivy.app import App
from kivy.uix.label import Label

class AimAssistApp(App):
    def build(self):
        return Label(text="Aim Assist Initialized!")

if __name__ == '__main__':
    AimAssistApp().run()
