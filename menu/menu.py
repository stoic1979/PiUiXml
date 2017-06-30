from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
from kivy.uix.dropdown import DropDown


Builder.load_file("menu.kv")


class Test(TabbedPanel):
    pass
    """
    print "============================="
    drop_down = CustomDropDown()
    dropdown = DropDown()
    print "++++++++++++++++++++++++++"
    notes = ['Features', 'Suggestions', 'Abreviations', 'Miscellaneous']
    for note in notes:
        btn = Button(text='%r' % note, size_hint_y=None, height=30)
        btn.bind(on_release=lambda btn: dropdown.select(btn.text))
        dropdown.add_widget(btn)

"""


class CustomDropDown(DropDown):
    pass


class TabbedPanelApp(App):
    def build(self):
        return Test()


if __name__ == '__main__':
    TabbedPanelApp().run()
