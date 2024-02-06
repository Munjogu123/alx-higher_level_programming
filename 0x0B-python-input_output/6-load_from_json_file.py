#!/usr/bin/python3
""" This module creates an Object from a “JSON file” """
import json


def load_from_json_file(filename):
    """  creates an Object from a “JSON file”

    Args:
        filename: name of file
    """
    with open(filename) as file:
        return json.load(file)
