#!/usr/bin/python3
"""
This module writes an Object to a text file,
using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation

    Args:
        my_obj: object to be encoded
        filename: name of file
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
