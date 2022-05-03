""" Quiz GUI
Author: Jono Schwass
Version: 1
"""

# Imports
from tkinter import *

# Testing
questionNum = 1
questionQ1 = "What is the Maori word for 12"


class Convertor:
    def __init__(self):
        # Background Formatting
        background_color = "light blue"

        # Main Screen
        self.convertor_frame = Frame(width=300, height=300,
                                     bg=background_color, pady=10)
        self.convertor_frame.grid()

        # Title
        self.temp_convertor_label = Label(self.convertor_frame,
                                          text="Te Reo Maori Quiz",
                                          font=("Arial", "24", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_convertor_label.grid(row=0, column=0)

        # Question Number
        self.temp_convertor_label = Label(self.convertor_frame,
                                          text="Question {}".format(
                                              questionNum),
                                          font=("Arial", "12", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_convertor_label.grid(row=1, column=0)

        # Question Text
        self.temp_convertor_label = Label(self.convertor_frame,
                                          text=questionQ1,
                                          font=("Arial", "12", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_convertor_label.grid(row=2, column=0)

        # Quiz Frame
        self.quiz_frame = Frame(self.convertor_frame,
                                width=300, height=300,
                                bg=background_color, pady=10)
        self.quiz_frame.grid()

        # Quiz Buttons
        self.b1_button = Button(self.quiz_frame, text="B1",
                                font=("Arial", "10"),
                                padx=20, pady=10)
        self.b1_button.grid(row=1, column=1)
        self.b2_button = Button(self.quiz_frame, text="B2",
                                font=("Arial", "10"),
                                padx=20, pady=10)
        self.b2_button.grid(row=1, column=2)
        self.b3_button = Button(self.quiz_frame, text="B3",
                                font=("Arial", "10"),
                                padx=20, pady=10)
        self.b3_button.grid(row=2, column=1)
        self.b4_button = Button(self.quiz_frame, text="B4",
                                font=("Arial", "10"),
                                padx=20, pady=10)
        self.b4_button.grid(row=2, column=2)


# Main Retinue
if __name__ == "__main__":
    root = Tk()
    root.title("Te Reo Maori Quiz")
    something = Convertor()
    root.mainloop()
