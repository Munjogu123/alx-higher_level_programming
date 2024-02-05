#!/usr/bin/python3
""" This module contains a Geometry module """


class BaseGeometry:
    """ Defines a geometry class """
    def area(self):
        """ Gets the area """
        raise Exception("area() is not implemented")
