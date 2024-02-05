#!/usr/bin/python3
""" This module checks if an object is an instance of a specified class """


def is_kind_of_class(obj, a_class):
    """ Checks if an object is an instance of a specified class

    Args:
        obj: object being checked
        a_class: class used for the check

    Returns:
        true if obj is an instance otherwise false
    """
    return isinstance(obj, a_class)
