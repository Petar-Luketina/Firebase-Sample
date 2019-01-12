from kivy.app import App
from kivy.lang import Builder
import json
import requests

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
                    id: JSON
            GridLayout:
                cols:1
                Button:
                    text: 'Patch Line'
                    on_release: app.patch(JSON.text)
                Button:
                    text: 'Post Line'
                    on_release: app.post(JSON.text)
                Button:
                    text: 'Put Line'
                    on_release: app.put(JSON.text)
                Button:
                    text: 'Delete Line'
                    on_release: app.delete(JSON.text)
                Button:
                    text: 'Get & Print Database'
                    on_release: app.get()

""")

class MyApp(App):

    url = 'https://samplefirebaseapp-fe077.firebaseio.com/.json'

    def patch(self, JSON):
        to_database = json.loads(JSON)
        requests.patch(url = self.url, json = to_database)

    def post(self, JSON):
        to_database = json.loads(JSON)
        requests.post(url = self.url, json = to_database)

    def put(self, JSON):
        to_database = json.loads(JSON)
        requests.put(url = self.url, json = to_database)

    def delete(self, JSON):
        requests.delete(url = self.url[:-5] + JSON + ".json")

    auth_key = 'qqdmdEODAGvCrj5S4BgXtaFmIUH8RcklpMEnWrcH'

    def get(self):
        request = requests.get(self.url + '?auth=' + self.auth_key)
        print(request.json())

    def build(self):
        return KV

if __name__ == '__main__':
    MyApp().run()