""" Start GUI
Author: Jono Schwass
Version: 1
"""

# Imports
from tkinter import *


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
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_convertor_label.grid(row=0)

        # Start Button
        self.start_button = Button(self.convertor_frame, text="Start",
                                  font=("Arial", "14"),
                                  padx=10, pady=10, command=self.start)
        self.start_button.grid(row=1)

    # Start Command
    def start(self):
        print("Log: Start Quiz")


# Main Retinue
if __name__ == "__main__":
    root = Tk()
    root.title("Te Reo Maori Quiz")
    something = Convertor()
    root.mainloop()
