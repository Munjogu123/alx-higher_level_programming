#!/usr/bin/python3
"""

This module prints a square with the character #

"""


def print_square(size):
    """  prints a square #

    Args:
        size: size of the square

    Raises:
        TypeError: if size is not int
        if size is float and less than 0
        ValueError: if size is less than 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
