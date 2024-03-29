#!/usr/bin/python3
""" This module defines a rectangle """


class Rectangle:
    """ Defines a Rectangle """
    def __init__(self, width=0, height=0):
        """ Initializes a Rectangle

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Retrieves the width of the rectangle

        Has a setter method that sets the value and raises errors
        if certain conditions are not met
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets width value """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ Retrieves the height of the rectangle

        Has a setter method that sets the value and raises errors
        if certain conditions are not met
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets height value """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
