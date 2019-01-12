from kivy.app import App
from kivy.lang import Builder

KV = Builder.load_string ("""

ScreenManager:
    id: manager
    Screen:
        BoxLayout:
            orientation: 'vertical'
            GridLayout:
                cols:1
                Label:
                    text: 'Write a JSON string'
                TextInput:
                    size_hint_y: .2
            GridLayout:
                cols:1
                Button:
                    text: 'Patch Line'
                Button:
                    text: 'Post Line'
                Button:
                    text: 'Put Line'
                Button:
                    text: 'Delete Line'
                Button:
                    text: 'Get & Print Database'

""")

class MyApp(App):

    url = '/.json'

    def build(self):
        return KV

if __name__ == '__main__':
    MyApp().run()
