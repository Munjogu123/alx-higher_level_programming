#!/usr/bin/python3
""" This module defines a rectangle """


class Rectangle:
    """ Defines a Rectangle """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initializes a Rectangle

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Checks if rect_1 and rect_2 are instances of Rectangle and returns
        rect_1 if both rect_1 and rect_2 have the same area

        Args:
            rect_1: object 1
            rect_2: object 2

        Raises:
            TypeError if rect_1 or rect_2 is not an instance of rectangle

        Returns:
            rect_1 if both rect_1 and rect_2 have the same area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() > rect_2.area():
                return rect_1
            elif rect_2.area() > rect_1.area():
                return rect_2
            else:
                return rect_1

    @classmethod
    def square(cls, size=0):
        """ Returns a new instance with the height and width equal to size

        Args:
            size: dimensions for width and height

        Returns:
            returns a new instance with the height and width equal to size
        """
        return cls(size, size)

    def __str__(self):
        """ prints rectangle with the character #

        Returns:
            rectangles printed or an empty string
        """
        if self.width == 0 or self.height == 0:
            return ""

        data = ""
        for i in range(self.height):
            data += ("{}".format(self.print_symbol) * self.width) + "\n"

        return data[:-1]

    def __repr__(self):
        """ Prints string representation of rectangle

        Returns:
            returns a string representation of the rectangle
        """
        return 'Rectangle({}, {})'.format(self.width, self.height)

    def __del__(self):
        """" Prints a message if an instance is being deleted """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
