#!/usr/bin/python3
"""

This module contains a function that calculates the sum oftwo integers

"""


def add_integer(a, b=98):
    """ Adds two integers or floats

    Args:
        a: first parameter
        b: second parameter

    Raises:
        TypeError: if a or b is not an integer or float

    Returns:
        returns the sum of two parameters
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
