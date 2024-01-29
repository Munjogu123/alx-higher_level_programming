#!/usr/bin/python3
""" This module defines a rectangle """


class Rectangle:
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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
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
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Gets the area of the rectangle

        Returns:
            Returns the area of the rectangle
        """
        return int(self.width) * int(self.height)

    def perimeter(self):
        """ Gets the perimeter of the rectangle

        Returns:
            The perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""

        data = ""
        for i in range(self.height):
            data += ("#" * self.width) + "\n"

        return data[:-1]
