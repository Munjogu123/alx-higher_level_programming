#!/usr/bin/python3
""" This module contains a Geometry module """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


""" This module defines a rectangle """


class Rectangle(BaseGeometry):
    """ Inherits from BaseGeometry """
    def __init__(self, width, height):
        """ validates that the arguments are positive integers and
        initializes the values """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
