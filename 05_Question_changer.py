""" Question Changer
Author: Jono Schwass
Version: 1
"""

# Testing
questionNum = 1
QuestionTxtList = ["What number does this Maori word mean? 'Tekau mā'"
    , "What number does this Maori word mean? 'Tekau mā'"]
questionTxt = ""
questionAnsList = [12, 12]
questionAns = 12
Ans1 = 10
Ans2 = 12
Ans3 = 22
Ans4 = 18
userAns = 0
print(questionAnsList)


def questionChanger():
    QuestionTxt = QuestionTxtList[questionNum]
    print("log: ",QuestionTxt)
    questionAns = questionAnsList[questionNum]
    print("Log: ",questionAns)


questionChanger()
