#!/usr/bin/python3
""" This module returns the JSON representation of an object (string) """
import json


def to_json_string(my_obj):
    """ returns the JSON representation of an object (string)

    Args:
        my_obj: objected to be encoded

    Returns:
        returns JSON representation of an object
    """
    return json.dumps(my_obj)
