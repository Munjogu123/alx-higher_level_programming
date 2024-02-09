#!/usr/bin/python3"
""" This module defines a square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ This class inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ initializes the attributes """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Retrieves the value of the size of square """
        return self.width

    @size.setter
    def size(self, value):
        """ Checks if size is of correct value and type """
        self.width = value
        self.height = value

    def __str__(self):
        """ Overloads the __str__ function for class Rectangle """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - "
                f"{self.size}")

    def update(self, *args, **kwargs):
        """ Assigns arguments to respective attributes """
        if args and len(args) != 0:
            attr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ creates a dictionary representaion of a class """
        attr = ['id', 'size', 'x', 'y']
        res = {}

        for key in attr:
            res[key] = getattr(self, key)

        return res
