import os
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






class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)



        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 1

        self.inside.add_widget(Label(text="News", font_size=30))
        self.cnn = Button(text=" CNN ", font_size=20)
        self.cnn.bind(on_press=self.runCNN)
        self.inside.add_widget(self.cnn)

        self.bbc = Button(text=" BBC ", font_size=20)
        self.bbc.bind(on_press=self.runBBC)
        self.inside.add_widget(self.bbc)

        self.gnews = Button(text=" Gnews ", font_size=20)
        self.gnews.bind(on_press=self.runGnews)
        self.inside.add_widget(self.gnews)

        self.add_widget(self.inside)

        self.outside = GridLayout()
        self.outside.cols = 1
        self.outside.add_widget(Label(text="Media", font_size=30))

        self.plex = Button(text=" Plex ", font_size=20)
        self.plex.bind(on_press=self.runPlex)
        self.outside.add_widget(self.plex)

        self.netflix = Button(text=" Netflix ", font_size=20)
        self.netflix.bind(on_press=self.runNetflix)
        self.outside.add_widget(self.netflix)

        self.spotify = Button(text=" Spotify ", font_size=20)
        self.spotify.bind(on_press=self.runSpotify)
        self.outside.add_widget(self.spotify)

        self.add_widget(self.outside)
        

    def build(self):
        layout = PageLayout()
        layout.inside.add_widget(Button(text='hello',background_color=(1,0,0,1)))
        layout.inside.add_widget(Button(text='world',background_color=(0,1,0,1)))
        layout.inside.add_widget(Button(text='welcome to',background_color=(1,1,1,1)))
        layout.inside.add_widget(Button(text='edureka',background_color=(0,1,1,1)))


    def runPlex(self, instance):
        os.startfile("C:/Program Files/Plex/Plex Media Player/PlexMediaPlayer.exe")

    def runNetflix(self, instance):
        os.startfile("C:/Users/Olofs/Desktop/Netflix")

    def runSpotify(self, instance):
        os.startfile("C:/Users/Olofs/Desktop/Spotify")

    def runCNN(self, instance):
        os.startfile("C:/Users/Olofs/Desktop/CNN")

    def runBBC(self, instance):
        os.startfile("C:/Users/Olofs/Desktop/BBC")

    def runGnews(self, instance):
        os.startfile("C:/Users/Olofs/Desktop/Gnews")



class MyApp(App):
    def build(self):
        return MyGrid()



if __name__ == "__main__":
    MyApp().run()
