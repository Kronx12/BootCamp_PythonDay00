import sys
import string


def countUpper(text):
    tmp = 0
    for i in text:
        if i.isupper():
            tmp += 1
    return tmp


def countLower(text):
    tmp = 0
    for i in text:
        if i.islower():
            tmp += 1
    return tmp


def countPunct(text):
    tmp = len(text)
    tmp -= len(text.translate(str.maketrans('', '', string.punctuation)))
    return tmp


def countSpace(text):
    tmp = 0
    for i in text:
        if i == ' ':
            tmp += 1
    return tmp


def text_analyzer(*args):
    """'text_analyzer(text)': This function counts the number of upper
    characters, lower characters, punctuation and spaces in a given text."""
    text = ""
    if len(args) > 1:
        print("ERROR")
        return
    elif len(args) == 0:
        print("What is the text to analyse?\n>> ", end='')
        for line in sys.stdin:
            text += line
    else:
        text = str(args[0])
    print("The text contains " + str(len(text)) + " characters:")
    print("\n- " + str(countUpper(text)) + " upper letters")
    print("\n- " + str(countLower(text)) + " lower letters")
    print("\n- " + str(countPunct(text)) + " punctuation marks")
    print("\n- " + str(countSpace(text)) + " spaces")
