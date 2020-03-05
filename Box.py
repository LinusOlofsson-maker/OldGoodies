import os
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class MyBox(BoxLayout):
    def __init__(self, **kwargs):
        super(MyBox, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')
        self.layout = self.add_widget(layout)
        self.btn1 = Button(text='Hello', font_size=20)
        self.btn2 = Button(text='World', font_size=20)
        self.add_widget(self.btn1)
        self.btn1.bind(on_press=self.pressbtn1)
        self.add_widget(self.btn2)
        self.btn2.bind(on_press=self.pressbtn2)

    def pressbtn1 (self,instance):
        print("yes")

    def pressbtn2 (self,instance):
        print("no")

class MyApp(App):
    def build(self):
        return MyBox()


if __name__ == "__main__":
    MyApp().run()
