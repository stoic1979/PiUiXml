from kivy.uix.dropdown import DropDown
from kivy.app import App
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.lang import Builder

Builder.load_file("testDrop.kv")

    # create a dropdown with 10 buttons
class CustomDropDown(DropDown):
    pass

dropdown = CustomDropDown()
mainbutton = Button(text='Hello')
mainbutton.bind(on_release=dropdown.open)
dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

class TabbedPanelApp(App):
    def build(self):
        return CustomDropDown()

if __name__ == '__main__':
    TabbedPanelApp().run()

