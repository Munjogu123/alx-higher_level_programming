#!/usr/bin/python3
""" This module creates a subclass of list class """


class MyList(list):
    """ Inherits from list """
    def print_sorted(self):
        """ Sorts a list """
        print(sorted(self))
