""" Start GUI
Author: Jono Schwass
Version: 2
"""

# Imports
from tkinter import *


class Start:
    def __init__(self):
        # Background Formatting
        background_color = "light blue"
        helpbg = "orange"  # Help Background Color Formatting
        start_buttonbg = "light green"  # to distinguish the buttons better

        # Main Screen
        self.start_frame = Frame(width=300, height=300,
                                 bg=background_color, pady=10)
        self.start_frame.grid()

        # Title Label
        self.temp_convertor_label = Label(self.start_frame,
                                          text="Te Reo Maori Quiz",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_convertor_label.grid(row=0)

        # Welcome Msg
        self.temp_welcome_msg_label = Label(self.start_frame,
                                            text="Welcome to the Teo Reo "
                                                 "Maori Quiz. \nMade by Jono"
                                                 " Schwass",
                                            font=("Arial", "12"),
                                            bg=background_color,
                                            padx=10, pady=10)
        self.temp_welcome_msg_label.grid(row=1)

        # Creating a Button frame to make the Buttons into a grid
        self.button_frame = Frame(self.start_frame, width=300, height=300,
                                  bg="light blue", pady=10)
        self.button_frame.grid()

        # Start Button
        self.start_button = Button(self.button_frame, text="Start",
                                   font=("Arial", "14"), bg=start_buttonbg,
                                   padx=20, pady=10, command=self.startQuiz)
        self.start_button.grid(row=0, column=0)

        # Help Button
        self.help_button = Button(self.button_frame, text="Help",
                                  font=("Arial", "14"),
                                  padx=20, pady=10, command=self.help,
                                  bg=helpbg)
        self.help_button.grid(row=0, column=1)

    # Help Command Function
    def help(self):
        print("Log: Help")
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")

    # Start Command
    def startQuiz(self):
        print("Log: Start Quiz")
        quit()


# Main Retinue
if __name__ == "__main__":
    root = Tk()
    root.title("Te Reo Maori Quiz")
    something = Start()
    root.mainloop()
