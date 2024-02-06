#!/usr/bin/python3
def read_file(filename=""):
    """ Reads a text file

    Args:
        filename: name of the file
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read())
