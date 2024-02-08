#!/usr/bin/python3"
""" This module defines a class Base """


class Base:
    """ defines class base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Checks if id is None

        Args:
            id: value of id
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
