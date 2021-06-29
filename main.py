from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout

# Change the window color
Window.clearcolor = get_color_from_hex("#f8edeb")

# Create the screens
class Greeting(Screen):
    pass

class SelectFile(Screen):
    pass

class AskSpellings(Screen):
    pass

# Create screen manager
class WindowManager(ScreenManager):
    pass

# Create app
class SpellerApp(App):
    pdf_file_path = ""

    def change_window_background(self, hex_color):
        Window.clearcolor = get_color_from_hex(hex_color)

# Run the App
SpellerApp().run()