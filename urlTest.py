import eel
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.label import Label


eel.init('web')
eel.start('Main.html', size=(510, 320), block=False)

print("This is now after start")


class MyBox(BoxLayout):
    def __init__(self, **kwargs):
        super(MyBox, self).__init__(**kwargs)

        self.display = BoxLayout()
        self.eel.init('web')
        self.start('Main.html', size=(510,320), block= False)
        self.add_widget()


class MyApp(App):
    def build(self):
        return MyBox()


if __name__ == "__main__":
    MyApp().run()

while True:
    eel.sleep(10)
