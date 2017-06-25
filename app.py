import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

# Builder.load_file("main.kv")
Builder.load_file("second.kv")


class MainScreen(Screen):
    pass


class SecondScreen(Screen):
    pass

sm = ScreenManager()
# sm.add_widget(MainScreen(name = 'main'))
sm.add_widget(SecondScreen(name='second'))


class MyApp(App):

    def build(self):
        return sm


if __name__ == '__main__':
    MyApp().run()
