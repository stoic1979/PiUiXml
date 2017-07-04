from kivy.base import runTouchApp
from kivy.uix.spinner import Spinner

spinner = Spinner(
    # default value shown
    text='Home',
    # available values
    values=('Home', 'Work', 'Other', 'Custom'),
    # just for positioning in our example
    size_hint=(None, None),
    size=(100, 44),
    pos_hint={'center_x': .5, 'center_y': .5})

def show_selected_value(spinner, text):
    print('The spinner', spinner, 'have text', text)

spinner.bind(text=show_selected_value)

runTouchApp(spinner)
"""
BoxLayout:
                size_hint: 1, .1
                orientation: 'horizontal'
                Label:
                    text: 'TCVG'
                    color: 0, 0, 0, 1
                Label:
                    text: 'Harle Storm \n71% THC  14.6% CBD'
                    color: 0, 0, 0, 1
                Label:
                    text: 'ALL'
            BoxLayout:
                orientation: 'horizontal'
                Label:
                    text: 'KYND'
                    color: 0, 0, 0, 1
                Label:
                    text: 'Ringo Gift \n0.4% 9.7% CBD'
                    color: 0, 0, 0, 1
                Label:
                    text: 'ALL'
                    color: 0, 0, 0, 1
            BoxLayout:
                orientation: 'horizontal'
                Label:
                    text: 'GPL'
                    color: 0, 0, 0, 1
                Label:
                    text: 'Fire Angel \n5.5% THC 8.7% CBD'
                    color: 0, 0, 0, 1
                Label:
                    text: 'ALL'
                    color: 0, 0, 0, 1




                    BoxLayout:
                size_hint: 1, .1
                orientation: 'horizontal'
                Label:
                    size_hint: .2, .1
                    text: ''
                Label:
                    size_hint: 1,.9
                    text: ''
                    canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1
                    Rectangle:
                        pos: self.pos
                        size: self.size
                Label:
                    size_hint: .4,.9
                    text: '[b]CBD FLOWER[/b]'
                    font_size: '22sp'
					markup: True
					color: 0, 0, 0, 1
		        Label:
		            size_hint: 1,.9
		            text: ''
		            canvas.before:
                        Color:
                            rgba: 0, 0, 0, 1
                        Rectangle:
                            pos: self.pos
                            size: self.size
                Label:
                    size_hint: .2,.1
                    text: ''





















                    Label:
                size_hint: 1,.1
                text: '1G $15  1/8 $40  1/4 $75 \n      1/2$140 oz$270'
                canvas.before:
                    Color:
                        rgba: 0,0,0,1
                    Rectangle:
                        pos: self.pos
                        size: self.size

"""
