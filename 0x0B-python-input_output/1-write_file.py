#!/usr/bin/python3
""" This module writes a string to a text file """


def write_file(filename="", text=""):
    """ Writes a string to a text file

    Args:
        filename: name of file
        text: content of the file

    Returns:
        returns the no of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        nchars = file.write(text)
        return nchars
