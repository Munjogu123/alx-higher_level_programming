#!/usr/bin/python3
"""

This module prints the name of a person

"""


def say_my_name(first_name, last_name=""):
    """ Prints name of person

    Args:
        first_name: person's first name
        last_name: person's last name

    Raises:
        TypeError: if first_name or last_name is not a string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
