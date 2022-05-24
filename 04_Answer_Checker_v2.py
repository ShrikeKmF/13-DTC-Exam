""" Answer Checker
Author: Jono Schwass
Version: 1
"""

# Testing
questionNum = 0
QuestionTxtList = ["What number does this Maori word mean? 'Tekau mā'"
, "What number does this Maori word mean? 'Tekau'"
, "What number does this Maori word mean? 'rua tekau mā rima'"
, "What number does this Maori word mean? 'tekau mā ono'"
, "What number does this Maori word mean? 'toru tekau'"
, "What number does this Maori word mean? 'tekau mā iwa'"
, "What number does this Maori word mean? 'rima tekau'"
, "What number does this Maori word mean? ''rua tekau mā toru'"
, "What number does this Maori word mean? 'rua tekau mā waru'"
, "What number does this Maori word mean? 'toru tekau mā iwa'"
                   ,"END"]
questionAnsList = [12, 10, 25, 16, 30, 19, 50, 23, 28, 39, 11]
b1List = [10, 14, 22, 39, 33, 39, 11, 13, 28, 43, 11]
b2List = [12, 13, 25, 15, 30, 18, 22, 28, 15, 26, 11]
b3List = [22, 10, 42, 25, 50, 19, 40, 25, 39, 15, 11]
b4List = [18, 19, 12, 16, 44, 22, 50, 23, 21, 39, 11]
userAns = 12
correctAns = 0
maxQuestion = 10


# Answer Checker
def AnswerChecker(userAns):
    global questionNum
    global correctAns
    if userAns == questionAnsList[questionNum]:
        print("Log: Ans Correct") # Printing Log Msgs
        correctAns += 1
    else:
        print("Log: Ans Incorrect") # Printing Log Msgs
    print("Log: Old Question Num {}".format(questionNum)) # Printing Log Msgs
    questionNum += 1
    print("Log: New Question Num {}".format(questionNum)) # Printing Log Msgs
    print("\n")


AnswerChecker(userAns)
