""" Quiz GUI
Author: Jono Schwass
Version: 6 (Final)
"""

# Imports
from tkinter import *  # GUI Import
from functools import partial  # to prevent unwanted windows

# Print log Start
print("****************\nWelcome to the Te Reo Maori Quiz")
print("All actions taken in the program will be logged in here")
print("Created by Jono Schwass\nVersion 6")
print("****************")

# Setting the Quiz Questions
# Requires 1 item after the questions E.G. "END"
QuestionTxtList = ["What number does this Maori word mean? 'Tekau mā rua'"
                   , "What number does this Maori word mean? "
                     "'rua tekau mā rima'"
                   , "What number does this Maori word mean?'Tekau'"
                   , "What number does this Maori word mean? 'tekau mā ono'"
                   , "What number does this Maori word mean? 'toru tekau'"
                   , "What number does this Maori word mean? 'tekau mā iwa'"
                   , "What number does this Maori word mean? 'rima tekau'"
                   , "What number does this Maori word mean? "
                     "''rua tekau mā toru'"
                   , "What number does this Maori word mean? "
                     "'rua tekau mā waru'"
                   , "What number does this Maori word mean? "
                     "'toru tekau mā iwa'"
                   , "END"]

# Setting the Quiz and Button Answers
# Requires 1 item at the end of list after Answers E.G. "99"
# 99 is used as an end function not an Answer
questionAnsList = [12, 25, 10, 16, 30, 19, 50, 23, 28, 39, 99]
b1List = [10, 21, 22, 39, 33, 39, 11, 13, 28, 43, 99]
b2List = [12, 28, 25, 15, 30, 18, 22, 28, 15, 26, 99]
b3List = [22, 25, 10, 25, 50, 19, 40, 25, 39, 15, 99]
b4List = [18, 19, 12, 16, 44, 22, 50, 23, 21, 39, 99]

# Setting Starting Values
questionNum = 0  # Current Question Number minus 1 (Python Counts from 0)
correctAns = 0  # Amount of correct Questions
maxQuestion = 10  # Maximum question in program


# Answer Checker
def AnswerChecker(userAns):
    global questionNum
    global correctAns
    if userAns == questionAnsList[questionNum]:
        print("Log: Ans Correct")  # Printing Log Msgs
        correctAns += 1
    else:
        print("Log: Ans Incorrect")  # Printing Log Msgs
    print("Log: Old Question Num {}".format(questionNum))  # Printing Log Msgs
    questionNum += 1
    print("Log: New Question Num {}".format(questionNum))  # Printing Log Msgs
    print("\n")  # Adding space to make the Log Easier to read


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
        self.start_frame.destroy()
        self.newWindow = Quiz()
        print("Log: Start Quiz")


# Main quiz Class/Frame
class Quiz:
    def __init__(self):
        background_color = "light blue"  # Background Color Formatting
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

        # Quiz Buttons Frame to create 2x2 grid
        self.button_frame = Frame(self.quiz_frame,
                                  width=300, height=300,
                                  bg=background_color, pady=10)
        self.button_frame.grid()

        # Quiz Buttons 1-4
        # Button 1
        self.b1_button = Button(self.button_frame,
                                text=b1List[questionNum],
                                font=("Arial", "10"),
                                padx=30, pady=10, bg=b1bg,
                                command=self.answerB1)
        self.b1_button.grid(row=1, column=1)
        # Button 2
        self.b2_button = Button(self.button_frame,
                                text=b2List[questionNum],
                                font=("Arial", "10"),
                                padx=30, pady=10, bg=b2bg,
                                command=self.answerB2)
        self.b2_button.grid(row=1, column=2)
        # Button 3
        self.b3_button = Button(self.button_frame,
                                text=b3List[questionNum],
                                font=("Arial", "10"),
                                padx=30, pady=10, bg=b3bg,
                                command=self.answerB3)
        self.b3_button.grid(row=2, column=1)
        # Button 4
        self.b4_button = Button(self.button_frame,
                                text=b4List[questionNum],
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
        print("Log: Answer 1")  # Printing log msg
        userAns = b1List[questionNum]
        AnswerChecker(userAns)
        self.UpdateTxt()
        if questionNum == maxQuestion:
            self.quiz_frame.destroy()
            self.newWindow = End()
            print("Log: End Quiz")  # Printing log msg

    def answerB2(self):  # Button 2 Answer
        print("Log: Answer 2")  # Printing log msg
        userAns = b2List[questionNum]
        AnswerChecker(userAns)
        self.UpdateTxt()
        if questionNum == maxQuestion:
            self.quiz_frame.destroy()
            self.newWindow = End()
            print("Log: End Quiz")  # Printing log msg

    def answerB3(self):  # Button 3 Answer
        global QuestionTxt
        global questionAns
        print("Log: Answer 3")  # Printing log msg
        userAns = b3List[questionNum]
        AnswerChecker(userAns)
        self.UpdateTxt()
        if questionNum == maxQuestion:
            self.quiz_frame.destroy()
            self.newWindow = End()
            print("Log: End Quiz")  # Printing log msg

    def answerB4(self):  # Button 4 Answer
        print("Log: Answer 4")  # Printing log msg
        userAns = b4List[questionNum]
        AnswerChecker(userAns)
        self.UpdateTxt()
        if questionNum == maxQuestion:
            self.quiz_frame.destroy()
            self.newWindow = End()
            print("Log: End Quiz")  # Printing log msg

    # Updating the Label Text for the buttons and titles
    def UpdateTxt(self):
        # Updating the Question and Number Text
        self.temp_questiontxt_label['text'] = QuestionTxtList[questionNum]
        self.temp_questionnum_label['text'] = "Question", questionNum + 1
        # ^ Adding in the question Number Plus 1 (As python counts from 0)
        # Updating the Button Labels
        self.b1_button['text'] = b1List[questionNum]
        self.b2_button['text'] = b2List[questionNum]
        self.b3_button['text'] = b3List[questionNum]
        self.b4_button['text'] = b4List[questionNum]


# Help Screen Class
class Help:
    def __init__(self, partner):
        # Formatting background
        background = "orange"  # Background Colour Help

        partner.help_button.config(
            state=DISABLED)  # Stopping Duplciate Windows

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
                               width=40, bg=background)
        self.help_text.grid(row=1)

        # Close Button
        self.dismiss_btn = Button(self.help_frame, text="Close", width=10,
                                  bg="orange", font="Arial 10 bold",
                                  command=partial(self.close_help,
                                                  partner))
        self.dismiss_btn.grid(row=2, pady=10)

    # Help Close Command
    def close_help(self, partner):
        partner.help_button.config(state=NORMAL)  # Resetting Help Button
        self.help_box.destroy()


# End Screen Class/Frame
class End:
    def __init__(self):
        # Background Formatting
        background_color = "light blue"  # End Screen Background Colour

        # Main Screen
        self.end_frame = Frame(width=300, height=300,
                               bg=background_color, pady=10)
        self.end_frame.grid()

        # Title
        self.temp_title_end_label = Label(self.end_frame,
                                          text="Te Reo Maori Quiz",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_title_end_label.grid(row=0)

        # Number Correct Label out of Amount of Questions
        self.temp_num_correct_label = Label(self.end_frame,
                                            text="Number Correct {} / "
                                                 "{}".format(correctAns,
                                                             questionNum),
                                            font=("Arial", "12"),
                                            bg=background_color,
                                            padx=10, pady=10)
        self.temp_num_correct_label.grid(row=1)

        # End Program
        self.end_button = Button(self.end_frame, text="Close",
                                 font=("Arial", "14"),
                                 padx=10, pady=10, command=self.endQuiz)
        self.end_button.grid(row=2)

    # end program Command
    def endQuiz(self):
        self.end_frame.destroy()  # Destroying Main Frame
        print("Log: Close Quiz")  # Printing log msg
        print("Log: Number Correct", correctAns, "/", questionNum)  # Log Msg
        quit()  # Ending Program


# Main Retinue
if __name__ == "__main__":
    root = Tk()
    root.title("Te Reo Maori Quiz")
    something = Start()
    root.mainloop()
