""" Quiz GUI
Author: Jono Schwass
Version: 4
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
state = 1


def AnswerChecker(userAns):
    global questionNum
    global correctAns
    if userAns == questionAnsList[questionNum]:
        print("Log: Ans Correct")
        print("Log: Old Question Num {}".format(questionNum))
        questionNum += 1
        correctAns += 1
        print("Log: New Question Num {}".format(questionNum))
    else:
        print("Log: Ans Incorrect")
        print("Log: Old Question Num {}".format(questionNum))
        questionNum += 1
        print("Log: New Question Num {}".format(questionNum))


if state == 1:
    class quiz:
        def __init__(self):
            background_color = "light blue"  # Background Color Formatting
            background_color2 = "light blue"  # Background Color Formatting
            b1bg = "red"  # Button Color Formatting
            b2bg = "blue"  # Button Color Formatting
            b3bg = "yellow"  # Button Color Formatting
            b4bg = "green"  # Button Color Formatting
            helpbg = "orange"  # Help Background Color Formatting

            # Main Screen
            self.quiz_frame = Frame(width=300, height=300,
                                         bg=background_color, pady=10)
            self.quiz_frame.grid()

            # Title
            self.temp_title_label = Label(self.quiz_frame,
                                              text="Te Reo Maori Number Quiz",
                                              font=("Arial", "24", "bold"),
                                              bg=background_color,
                                              padx=50, pady=10)
            self.temp_title_label.grid(row=0, column=0)

            # Question Number
            self.temp_questionnum_label = Label(self.quiz_frame,
                                              text="Question {}".format(
                                                  (questionNum + 1)),
                                              font=("Arial", "12", "bold"),
                                              bg=background_color,
                                              padx=10, pady=10)
            self.temp_questionnum_label.grid(row=1, column=0)

            # Question Text
            self.temp_questiontxt_label = Label(self.quiz_frame,
                                              text=QuestionTxtList[
                                                  questionNum],
                                              font=("Arial", "12", "bold"),
                                              bg=background_color,
                                              padx=10, pady=10)
            self.temp_questiontxt_label.grid(row=2, column=0)

            # Quiz Buttons Frame
            self.button_frame = Frame(self.quiz_frame,
                                    width=300, height=300,
                                    bg=background_color2, pady=10)
            self.button_frame.grid()

            # Quiz Buttons 1-4
            self.b1_button = Button(self.button_frame, text=b1List[questionNum],
                                    font=("Arial", "10"),
                                    padx=30, pady=10, bg=b1bg,
                                    command=self.answerB1)
            self.b1_button.grid(row=1, column=1)
            self.b2_button = Button(self.button_frame, text=b2List[questionNum],
                                    font=("Arial", "10"),
                                    padx=30, pady=10, bg=b2bg,
                                    command=self.answerB2)
            self.b2_button.grid(row=1, column=2)
            self.b3_button = Button(self.button_frame, text=b3List[questionNum],
                                    font=("Arial", "10"),
                                    padx=30, pady=10, bg=b3bg,
                                    command=self.answerB3)
            self.b3_button.grid(row=2, column=1)
            self.b4_button = Button(self.button_frame, text=b4List[questionNum],
                                    font=("Arial", "10"),
                                    padx=30, pady=10, bg=b4bg,
                                    command=self.answerB4)
            self.b4_button.grid(row=2, column=2)

            # Help Button
            self.help_button = Button(self.quiz_frame, text="Help",
                                      font=("Arial", "14"),
                                      padx=20, pady=10, command=self.help,
                                      bg=helpbg)
            self.help_button.grid(row=5, column=0)

        # Help Command Function
        def help(self):
            print("Log: Help")
            get_help = Help(self)
            get_help.help_text.configure(text="Help text goes here")

        # Answer Command Function 1-4
        def answerB1(self):  # Button 1 Answer
            print("Log: Answer 1")
            userAns = b1List[questionNum]
            AnswerChecker(userAns)
            self.UpdateTxt()

        def answerB2(self):  # Button 2 Answer
            print("Log: Answer 2")
            userAns = b2List[questionNum]
            AnswerChecker(userAns)
            self.UpdateTxt()

        def answerB3(self):  # Button 3 Answer
            global QuestionTxt
            global questionAns
            print("Log: Answer 3")
            userAns = b3List[questionNum]
            AnswerChecker(userAns)
            self.UpdateTxt()

        def answerB4(self):  # Button 4 Answer
            print("Log: Answer 4")
            userAns = b4List[questionNum]
            AnswerChecker(userAns)
            self.UpdateTxt()

        def UpdateTxt(self):
            self.temp_questiontxt_label['text'] = QuestionTxtList[questionNum]
            self.temp_questionnum_label['text'] = "Question", questionNum + 1
            self.b1_button['text'] = b1List[questionNum]
            self.b2_button['text'] = b2List[questionNum]
            self.b3_button['text'] = b3List[questionNum]
            self.b4_button['text'] = b4List[questionNum]

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
                                      command=partial(self.close_help,
                                                      partner))
            self.dismiss_btn.grid(row=2, pady=10)

        # Close Command
        def close_help(self, partner):
            partner.help_button.config(state=NORMAL)
            self.help_box.destroy()

# Main Retinue
if __name__ == "__main__":
    root = Tk()
    root.title("Te Reo Maori Quiz")
    something = quiz()
    root.mainloop()
print("Log: Number Correct", correctAns, "/ 12")
