#!/usr/bin/python3
""" This module defines a class student """


class Student:
    """ Defines a class Student """
    def __init__(self, first_name, last_name, age):
        """Initializes some attributes

        Args:
           first_name: first name
           last_name: last name
           age: age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dictionary representation of a Student instance """
        return self.__dict__
