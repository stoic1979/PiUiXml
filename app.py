from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
# Config.set('graphics', 'fullscreen', 'fake')
# Config.set('graphics', 'fullscreen', 1)


# Builder.load_file("main.kv")
# Builder.load_file("second.kv")
Builder.load_file("menu.kv")


class MainScreen(Screen):
    pass


class SecondScreen(Screen):
    pass


class MenuScreen(Screen):
    pass

sm = ScreenManager()
# sm.add_widget(MainScreen(name='main'))
# sm.add_widget(SecondScreen(name='second'))
sm.add_widget(MenuScreen(name='menu'))


class MyApp(App):

    data = ['A', 'B', 'C']

    def build(self):
        return sm

if __name__ == '__main__':
    MyApp().run()
