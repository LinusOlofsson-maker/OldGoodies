import os
import time
from sqlite3.dbapi2 import Time
from time import strftime
import webbrowser
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.pagelayout import PageLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from datetime import datetime
from datetime import timedelta
from kivy.clock import Clock
from kivy_deps import sdl2, glew


global clocktext

class ClockText(Label):
    def update(self, *args):
        self.text = time.strftime('[b]%H[/b]:%M:%S')


class MyGrid(Widget):



    def runDplay(self):
        webbrowser.open("https://www.dplay.se/")

    def runPlex(self):
        os.startfile("C:/Program Files/Plex/Plex Media Player/PlexMediaPlayer.exe")

    def runNetflix(self):
        os.startfile("C:/Users/Olofs/Desktop/Netflix")

    def runSpotify(self):
        os.startfile("C:/Users/Olofs/Desktop/Spotify")

    def runCNN(self):
        os.startfile("C:/Users/Olofs/Desktop/CNN")

    def runBBC(self):
        os.startfile("C:/Users/Olofs/Desktop/BBC")

    def runGnews(self):
        os.startfile("C:/Users/Olofs/Desktop/Gnews")


class MyApp(App):
    def build(self):
        grid = MyGrid()
        clocktext =grid.ids.clocktext
        Clock.schedule_interval(clocktext.update, 1)
        return grid


if __name__ == "__main__":
    MyApp().run()
