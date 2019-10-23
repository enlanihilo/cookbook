"""
    docs: https://kivy.org/doc/stable/


    A widget (kivy.uix) is the base building block of GUI interfaces in kivy
    it provides:
        - canvas            - labels        - images        - switch
        - event handling    - buttons       - text input    - videos


    Layouts are containers used to arrange widgets in a particular manner

    anchor
    box
    float
    relative
    grid
    page
    scatter
    stack

"""

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.uix.gridlayout import GridLayout

class MyGrid(GridLayout):
    def __init__(self, **kwards):
        super(MyGrid, self).__init__(**kwards)
        self.cols = 2
        self.add_widget(Label(text="Name: "))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)


class EpicApp(App):
    #to add a button inside a boxlayout

    def build(self):
        return MyGrid()
        
        

if __name__ == "__main__":
    EpicApp().run()