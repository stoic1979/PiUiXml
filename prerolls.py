from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file("prerolls.kv")


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
