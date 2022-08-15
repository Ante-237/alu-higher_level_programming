#!/usr/bin/python3
"""
module for text indentation
"""


def text_indentation(text):
    """ just the function
    here """

    if type(text) is not str:
        raise TypeError("text must be a string")

    trigger = 0
    for i in text:
        if i in ['.', '?', ':']:
            print(i)
            print()
            trigger = 1
            continue
        if trigger == 1:
            if i is " ":
                trigger = 0
                continue
        else:
            print(i, end="")
