from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# setting font
from kivy.core.text import LabelBase
LabelBase.register(name="GothamMedium",
                   fn_regular="fonts/GothamMedium.ttf",
                   fn_bold="fonts/GothamMedium.ttf",
                   fn_italic="fonts/GothamMedium.ttf",
                   fn_bolditalic="fonts/GothamMedium.ttf")


Builder.load_file("premium.kv")


class MainScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))


class MyApp(App):

    data = ['A', 'B', 'C']

    def build(self):
        return sm

if __name__ == '__main__':
    MyApp().run()
