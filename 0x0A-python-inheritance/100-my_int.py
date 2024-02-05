#!/usr/bin/python3
""" This module changes the way operators work """


class MyInt(int):
    """ defines how the operators work """
    def __eq__(self, __value: object) -> bool:
        """ Changes how the == operator works """
        return not(super().__eq__(__value))

    def __ne__(self, __value: object) -> bool:
        """ Changes how the != operator works """
        return not(super().__ne__(__value))
