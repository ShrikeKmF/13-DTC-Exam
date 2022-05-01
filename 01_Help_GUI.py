""" Help GUI
Author: Jono Schwass
Version: 1
"""

# Imports
from tkinter import *
from functools import partial  # to prevent unwanted windows


class Convertor:
    def __init__(self):
        # Formatting
        background_color = "light blue"

        # Main Screen
        self.convertor_frame = Frame(width=300, height=300,
                                     bg=background_color, pady=10)
        self.convertor_frame.grid()

        # Title
        self.temp_convertor_label = Label(self.convertor_frame,
                                          text="Te Reo Maori Quiz",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_convertor_label.grid(row=0)

        # Help Button
        self.help_button = Button(self.convertor_frame, text="Help",
                                  font=("Arial", "14"),
                                  padx=10, pady=10, command=self.help)
        self.help_button.grid(row=1)

    # Help Command
    def help(self):
        print("Log: Help")
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")


class Help:
    def __init__(self, partner):
        # Formatting
        background = "orange"

        partner.help_button.config(state=DISABLED)

        self.help_box = Toplevel()

        # Stop unwanted Windows
        self.help_box.protocol('WM_DELETE_WINDOWS', partial(self.close_help, partner))

        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()

        # Help Title
        self.how_heading = Label(self.help_frame, text="Help",
                                 font="arial 16 bold", bg=background)
        self.how_heading.grid(row=0)

        self.help_text = Label(self.help_frame, text="", justify="left",
                               width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)

        # Close Button
        self.dismiss_btn = Button(self.help_frame, text="Closs", width=10,
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
