#!/usr/bin/python3
""" This module returns the lsit of attributes and methods of an object """


def lookup(obj):
    """ returns the list of available attributes and methods of an object

    Args:
        obj: object to lookup

    Returns:
        the list of available attributes and methods of an object
    """
    return dir(obj)
