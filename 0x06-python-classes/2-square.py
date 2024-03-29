#!/usr/bin/python3
""" Defines a square """


class Square:
    """ Creating attributes for the class

    Args:
        size: refers to dimensions of the square

    Raises:
        TypeError: if size is not of type  int
        ValueError: if size is less than 0

    """
    def __init__(self, size=0):
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
