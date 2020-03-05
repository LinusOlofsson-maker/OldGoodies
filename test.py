from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.button import Button
import os


class startroot(Accordion):
    def __init__(self, **kwargs):
        super(startroot, self).__init__(**kwargs)
        self = Accordion()
        for x in range(3):
            item = AccordionItem(title='Title %d' % x)
            item.add_widget(Label(text='Very big content\n' * 10))
            self.add_widget(item)
            bb = B
            self.bbc = Button(text=" BBC ", font_size=20)
            self.bbc.bind(on_press=self.runBBC)
            self.add_widget(self.bbc)

    def runBBC(self, instance):
        os.startfile("C:/Users/Olofs/Desktop/BBC")


class AccordionApp(App):
    def build(self):
        return startroot()


if __name__ == '__main__':
    AccordionApp().run()
