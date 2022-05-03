""" Quiz GUI
Author: Jono Schwass
Version: 2
"""

# Imports
from tkinter import *
from functools import partial  # to prevent unwanted windows

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
        background_color = "light blue"  # Background Color Formatting
        background_color2 = "light blue"  # Background Color Formatting
        b1bg = "red"  # Button Color Formatting
        b2bg = "blue"  # Button Color Formatting
        b3bg = "yellow"  # Button Color Formatting
        b4bg = "green"  # Button Color Formatting
        helpbg = "orange"  # Help Background Color Formatting

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

        # Quiz Buttons Frame
        self.quiz_frame = Frame(self.convertor_frame,
                                width=300, height=300,
                                bg=background_color2, pady=10)
        self.quiz_frame.grid()

        # Quiz Buttons 1-4
        self.b1_button = Button(self.quiz_frame, text=Ans1,
                                font=("Arial", "10"),
                                padx=30, pady=10, bg=b1bg)
        self.b1_button.grid(row=1, column=1)
        self.b2_button = Button(self.quiz_frame, text=Ans2,
                                font=("Arial", "10"),
                                padx=30, pady=10, bg=b2bg)
        self.b2_button.grid(row=1, column=2)
        self.b3_button = Button(self.quiz_frame, text=Ans3,
                                font=("Arial", "10"),
                                padx=30, pady=10, bg=b3bg)
        self.b3_button.grid(row=2, column=1)
        self.b4_button = Button(self.quiz_frame, text=Ans4,
                                font=("Arial", "10"),
                                padx=30, pady=10, bg=b4bg)
        self.b4_button.grid(row=2, column=2)

        # Help Button
        self.help_button = Button(self.convertor_frame, text="Help",
                                  font=("Arial", "14"),
                                  padx=20, pady=10, command=self.help,
                                  bg=helpbg)
        self.help_button.grid(row=5, column=0)

    # Help Command Function
    def help(self):
        print("Log: Help")
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")


# Help Screen Class
class Help:
    def __init__(self, partner):
        # Formatting background
        background = "orange"

        partner.help_button.config(state=DISABLED)

        # Forcing to Top Level
        self.help_box = Toplevel()

        # Stop unwanted Windows
        self.help_box.protocol('WM_DELETE_WINDOWS',
                               partial(self.close_help, partner))

        # Frame Creation
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()

        # Help Title
        self.how_heading = Label(self.help_frame, text="Help",
                                 font="arial 16 bold", bg=background)
        self.how_heading.grid(row=0)

        # Help Text
        self.help_text = Label(self.help_frame, text="", justify="left",
                               width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)

        # Close Button
        self.dismiss_btn = Button(self.help_frame, text="Close", width=10,
                                  bg="orange", font="Arial 10 bold",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    # Close Command
    def close_help(self, partner):
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# Main Retinue
if __name__ == "__main__":
    root = Tk()
    root.title("Te Reo Maori Quiz")
    something = Convertor()
    root.mainloop()
