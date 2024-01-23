#!/usr/bin/python3
""" Defines a square """


class Square:
    """ Represents attributes of the class

    Args:
        size: dimensions of the square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0

    """
    def __init__(self, size=0):
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    """ Calculates the area of a square

    Returns:
        the area of a square

    """
    def area(self):
        return self.__size ** 2
