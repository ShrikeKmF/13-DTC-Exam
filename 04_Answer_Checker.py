""" Answer Checker
Author: Jono Schwass
Version: 1
"""

# Testing
questionNum = 1
questionTxt = "What number does this Maori word mean? 'Tekau mā'"
questionAns = 12
Ans1 = 10
Ans2 = 12
Ans3 = 22
Ans4 = 18
userAns = 0


def AnswerChecker(userAns, questionNum):
    if userAns == questionAns:
        print("Log: Ans Correct")
        questionNum += 1
        print("Log: Question Num {}".format(questionNum))
    else:
        print("Log: Ans Incorrect")
        questionNum += 1
        print("Log: Question Num {}".format(questionNum))


AnswerChecker(userAns, questionNum)
