from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.properties import ColorProperty

import PyPDF2

import pyttsx3

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
    vocab_words = None
    input_widgets = {
        0: "",
        1: "",
        2: "",
        3: "",
        4: "",
        5: "",
        6: "",
        7: "",
        8: "",
        9: ""
    }
    user_vocab_words = ["", "", "", "", "", "", "", "", "", ""]
    wrong_right_colors = [
        ColorProperty([1, 1, 1, 1]),
        ColorProperty([1, 1, 1, 1]),
        ColorProperty([1, 1, 1, 1]),
        ColorProperty([1, 1, 1, 1]),
        ColorProperty([1, 1, 1, 1]),
        ColorProperty([1, 1, 1, 1]),
        ColorProperty([1, 1, 1, 1]),
        ColorProperty([1, 1, 1, 1]),
        ColorProperty([1, 1, 1, 1]),
        ColorProperty([1, 1, 1, 1])
    ]

    # Create Engine
    engine = pyttsx3.init()
    engine.setProperty("rate", 125)

    def change_window_background(self, hex_color):
        Window.clearcolor = get_color_from_hex(hex_color)

    def get_vocab_words(self, pdf_file):
        file = open(pdf_file, "rb")  # Open the pdf file
        readed_file = PyPDF2.PdfFileReader(file)  # Read the pdf file
        wanted_page = readed_file.getPage(1)  # Get the wanted page
        extracted_text = wanted_page.extractText()  # Get the text of the page
        seperated_text = extracted_text.split()  # Split the the string (extracted_text) so that the vocab words can have spaces in them. This will allow to easily extract out the vocab words.
        self.vocab_words = seperated_text[-11:-1]  # Fish out the vocab words

    def speak_word(self, which_button):
        if which_button == "b1":
            speaking_word = self.vocab_words[0]

        elif which_button == "b2":
            speaking_word = self.vocab_words[1]

        elif which_button == "b3":
            speaking_word = self.vocab_words[2]

        elif which_button == "b4":
            speaking_word = self.vocab_words[3]

        elif which_button == "b5":
            speaking_word = self.vocab_words[4]

        elif which_button == "b6":
            speaking_word = self.vocab_words[5]

        elif which_button == "b7":
            speaking_word = self.vocab_words[6]

        elif which_button == "b8":
            speaking_word = self.vocab_words[7]

        elif which_button == "b9":
            speaking_word = self.vocab_words[8]

        elif which_button == "b10":
            speaking_word = self.vocab_words[9]

        self.engine.say(speaking_word)
        self.engine.runAndWait()

    def add_widget_in_input_list(self, widget, index):
        self.input_widgets[index] = widget

    def check_user_guess(self):
        for index, i in enumerate(self.vocab_words):
            if i.lower() == self.user_vocab_words[index]:
                try:
                    self.input_widgets[index].foreground_color = get_color_from_hex("#2a9d8f")
                    print("correct")
                except:
                    print("Error occurred --1")
            else:
                try:
                    self.input_widgets[index].foreground_color = [1, 0, 0, 1]
                    print("wrong")
                except:
                    print("Error occurred --2")



# Run the App
SpellerApp().run()
