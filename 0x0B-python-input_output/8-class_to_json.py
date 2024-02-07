#!/usr/bin/python3
"""
This module returns the dictionary
description with simple data structure
"""


def class_to_json(obj):
    """ returns the dictionary description with simple data structure

    Args:
        obj: obj to be encoded

    Returns:
        returns the dictionary description with simple data structure
    """
    return obj.__dict__
