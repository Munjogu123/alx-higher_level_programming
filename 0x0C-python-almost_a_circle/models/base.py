#!/usr/bin/python3
""" This module defines a class Base """
import json
import os


class Base:
    """ defines class base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Checks if id is None

        Args:
            id: value of id
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        filename = cls.__name__ + ".json"

        if list_objs is None:
            res = cls.to_json_string([])
        else:
            res = cls.to_json_string([i.to_dictionary() for i in list_objs])

        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(res)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        if json_string is None:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        filename = cls.__name__ + ".json"

        if os.path.exists(filename) is False:
            return []

        with open(filename, "r") as file:
            res_str = file.read()

        list_dict = cls.from_json_string(res_str)
        list_res = []

        for dict in list_dict:
            list_res.append(cls.create(**dict))

        return list_res
