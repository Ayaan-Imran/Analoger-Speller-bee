from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

# Create the screens
class SelectFile(Screen):
    pass

class AskSpellings(Screen):
    pass

# Create screen manager
class WindowManager(ScreenManager):
    pass

# Create app
class SpellerApp(App):
    pass

# Run the App
SpellerApp().run()