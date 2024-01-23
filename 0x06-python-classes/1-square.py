#!/usr/bin/python3
""" Defines a square """


class Square:
    """ Creates a private attribute size for the square

    Args:
        size: refers to dimensions of the square

    """
    def __init__(self, size=0):
        self.__size = size
