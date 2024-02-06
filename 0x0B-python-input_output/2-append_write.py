#!/usr/bin/python3
""" This module appends a string at the end of a text file """


def append_write(filename="", text=""):
    """ appends a string at the end of a text file

    Args:
        filename: name of file
        text: content of the file

    Returns:
        returns the no of characters appended
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        nchars = file.write(text)
        return nchars
