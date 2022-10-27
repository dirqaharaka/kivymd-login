from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import ObjectProperty
import kivy


kivy.require('1.0.8')

Window.size = (350, 580)
class LoginApp(MDApp):
    def build(self):
        self.manager = ScreenManager(transition = NoTransition())
        self.manager.add_widget(Builder.load_file("pre-splash.kv"))
        return self.manager 


if __name__== '__main__':
    LoginApp().run()