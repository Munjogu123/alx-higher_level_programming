#!/usr/bin/python3
""" This module returns an object represented by a JSON string"""
import json


def from_json_string(my_str):
    """ decodes the string passed

    Args:
        my_str: encoded JSON string

    Returns:
        returns an object represented by a JSON string
    """
    return json.loads(my_str)
