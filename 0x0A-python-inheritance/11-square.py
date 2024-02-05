#!/usr/bin/python3
""" Inherits from Rectangle and BaseGeometry """
Rectangle = __import__('9-rectangle').Rectangle


""" This module defines a square """


class Square(Rectangle):
    """ Defines a square """
    def __init__(self, size):
        """ Initializes size and checks if it is
        a positive integer """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Implements area of a square """
        return self.__size ** 2

    def __str__(self):
        """ Returns the description of the rectangle """
        return f"[Rectangle] {self.__size}/{self.__size}"
