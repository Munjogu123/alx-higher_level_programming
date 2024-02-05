#!/usr/bin/python3
""" Checks if an object inherits from a class (directly or indirectly) """


def inherits_from(obj, a_class):
    """ Checks if an object is an instance of a specified class

    Args:
        obj: object being checked
        a_class: class used for the check

    Returns:
        true if obj is an instance otherwise false
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
