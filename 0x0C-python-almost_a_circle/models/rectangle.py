#!/usr/bin/python3
""" This module creates class Rectangle """
from models.base import Base


class Rectangle(Base):
    """ Defines a Rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Retrieves value of width """
        return self.__width

    @width.setter
    def width(self, value):
        """ checks if width is the proper data type and value """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Retrieves value of height """
        return self.__height

    @height.setter
    def height(self, value):
        """ checks if width is the proper data type and value """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ Retrieves value of x """
        return self.__x

    @x.setter
    def x(self, value):
        """ checks if width is the proper data type and value """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ Retrieves value of y """
        return self.__y

    @y.setter
    def y(self, value):
        """ checks if width is the proper data type and value """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ Finds area of a rectangle """
        return self.width * self.height

    def display(self):
        """ prints rectangle instance with the character # """
        for i in range(self.y):
            print()

        for j in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """ Updates the __str__ function """
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """ Updates the attributes of the class Rectangle """
        if len(args) != 0 and args is not None:
            attr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ creates a dictionary representaion of a class """
        attr = ['id', 'width', 'height', 'x', 'y']
        res = {}

        for key in attr:
            res[key] = getattr(self, key)

        return res
