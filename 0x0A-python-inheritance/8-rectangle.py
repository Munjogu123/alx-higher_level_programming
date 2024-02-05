#!/usr/bin/python3
""" This module contains a Geometry module """


class BaseGeometry:
    """ Defines a geometry class """
    def area(self):
        """ Gets the area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value

        Args:
            name: name of the person
            value: parameter of type int and greater than 0

        Raises:
            TypeError: if value is not of type int
            ValueError: if value is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


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
