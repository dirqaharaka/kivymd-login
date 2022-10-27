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
        global screen_manager
        screen_manager = ScreenManager()
        # self.manager = ScreenManager(transition = NoTransition())
        screen_manager.add_widget(Builder.load_file("pre-splash.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        return screen_manager 

    def on_start(self):
        Clock.schedule_once(self.login, 7)

    def login(self, *args):
        screen_manager.current = "login"
if __name__== '__main__':
    LoginApp().run()