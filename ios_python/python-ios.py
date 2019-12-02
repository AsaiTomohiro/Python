import japanize_kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
class GreetingApp(App):
    def build(self):
         main_screen = BoxLayout()
         label = Label(text='こんにちは、世界')
         main_screen.add_widget(label)
         return main_screen
 


GreetingApp().run()
