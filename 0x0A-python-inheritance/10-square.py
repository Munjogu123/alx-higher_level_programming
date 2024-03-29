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
        super().__init__(size, size)
        self.__size = size
