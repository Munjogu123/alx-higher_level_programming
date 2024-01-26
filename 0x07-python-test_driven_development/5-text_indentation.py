#!/usr/bin/python3
"""

This module prints text with 2 new lines after '.', '?' and ':'

"""


def text_indentation(text):
    """ Prints text with 2 new lines after '.', '?' and ':'

    Args:
        text: text to be formatted according to specs

    Raises:
        TypeError: if text is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    
    i = 0
    while i < len(text) and text[i] == " ":
        i += 1

    while i < len(text):
        print(text[i], end="")
        if text[i] == "\n" or text[i] in ".?:":
            if text[i] in ".?:":
                print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
