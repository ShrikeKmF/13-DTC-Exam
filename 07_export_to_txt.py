""" Export to Txt
Author: Jono Schwass
Version: 1
"""
import re

data = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']

has_error = "yes"
while has_error == "yes":
    print()
    filename = input("Enter a Filename: ")

    valid_char = "[A-Za-z0-9_]"
    for letter in filename:
        if re.match(valid_char, letter):
            continue

        elif letter == "  ":
            problem = "(No spaces allowed)"

        else:
            problem = "(no {}'s is allowed".format(letter)
        has_error = "yes"

    if filename == "":
        problem = "Filename can't be blank"
        has_error = "yes"

    if has_error == "yes":
        print("Invalid Filename - {}".format(problem))
    else:
        print("You have entered a valid filename")

filename = filename + ".txt"

f = open(filename, "W+")

for item in data:
    f.write(item + "/n")

f.close()
