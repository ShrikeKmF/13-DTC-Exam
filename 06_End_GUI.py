""" END GUI
Author: Jono Schwass
Version: 1
"""

# Imports
from tkinter import *
from functools import partial  # to prevent unwanted windows

# Testing
questionNum = 0
QuestionTxtList = ["What number does this Maori word mean? 'Tekau mā'"
    , "What number does this Maori word mean? 'Tekau'", ]
questionAnsList = [12, 10, ]
b1List = [10, 14, ]
b2List = [12, 13, ]
b3List = [22, 10, ]
b4List = [18, 19, ]
userAns = 0
correctAns = 0


class End:
    def __init__(self):
        # Background Formatting
        background_color = "light blue"

        # Main Screen
        self.end_frame = Frame(width=300, height=300,
                                 bg=background_color, pady=10)
        self.end_frame.grid()

        # Title
        self.temp_convertor_label = Label(self.end_frame,
                                          text="Te Reo Maori Quiz",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_convertor_label.grid(row=0)

        # Close Button
        self.end_button = Button(self.end_frame, text="Close",
                                   font=("Arial", "14"),
                                   padx=10, pady=10, command=self.endQuiz)
        self.end_button.grid(row=1)

    # end Command
    def endQuiz(self):
        self.end_frame.destroy()
        print("Log: End Quiz")
        print("Log: Number Correct", correctAns, "/ 12")
        quit()


# Main Retinue
if __name__ == "__main__":
    root = Tk()
    root.title("Te Reo Maori Quiz")
    something = End()
    root.mainloop()

