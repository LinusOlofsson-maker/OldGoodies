## Sample Python application demonstrating the
## working with images in Kivy using .kv file

##################################################
# import kivy module
import kivy
import os
# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup

kivy.require('1.9.0')

# BoxLayout arranges children in a vertical or horizontal box.
# or help to put the children at the desired location.
from kivy.uix.boxlayout import BoxLayout

# to change the kivy default settings we use this module config
from kivy.config import Config

# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', True)
class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    
# creating the root widget used in .kv file
class Imagekv(BoxLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()



    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            self.text_input.text = stream.read()

        self.dismiss_popup()

    pass


# class in which name .kv file must be named My.kv.
class MyyApp(App):
    # define build() function
    def build(self):
        # returning the instance of Imagekv class
        return Imagekv()

    # run the App
Factory.register('LoadDialog', cls=LoadDialog)

if __name__ == '__main__':
    MyyApp().run()
