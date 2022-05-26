""" Quiz GUI
Author: Jono Schwass
Version: 1
"""

# Imports
from tkinter import *

# Testing
questionNum = 1
questionTxt = "What number does this Maori word mean?"
questionAns = "Tekau mā"
Ans1 = "10"
Ans2 = "12"
Ans3 = "22"
Ans4 = "18"


class Convertor:
    def __init__(self):
        # Background Formatting
        background_color = "light blue"
        background_color2 = "light blue"

        # Main Screen
        self.convertor_frame = Frame(width=300, height=300,
                                     bg=background_color, pady=10)
        self.convertor_frame.grid()

        # Title
        self.temp_convertor_label = Label(self.convertor_frame,
                                          text="Te Reo Maori Number Quiz",
                                          font=("Arial", "24", "bold"),
                                          bg=background_color,
                                          padx=50, pady=10)
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
                                          text=questionTxt,
                                          font=("Arial", "12", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_convertor_label.grid(row=2, column=0)

        # Quiz Buttons 1-4
        self.b1_button = Button(self.convertor_frame, text=Ans1,
                                font=("Arial", "10"),
                                padx=30, pady=10)
        self.b1_button.grid(row=3, column=0)
        self.b2_button = Button(self.convertor_frame, text=Ans2,
                                font=("Arial", "10"),
                                padx=30, pady=10)
        self.b2_button.grid(row=3, column=1)
        self.b3_button = Button(self.convertor_frame, text=Ans3,
                                font=("Arial", "10"),
                                padx=30, pady=10)
        self.b3_button.grid(row=4, column=0)
        self.b4_button = Button(self.convertor_frame, text=Ans4,
                                font=("Arial", "10"),
                                padx=30, pady=10)
        self.b4_button.grid(row=4, column=1)


# Main Retinue
if __name__ == "__main__":
    root = Tk()
    root.title("Te Reo Maori Quiz")
    something = Convertor()
    root.mainloop()
