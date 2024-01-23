#!/usr/bin/python3
"""" Defines a square """


class Square:
    """ Creates a private attribute size for the square

    Args:
        size: refers to dimensions of the square

    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """ retrieves the value of the size

        The setter method verifies if the size
        is an integer and raises either TypeError
        or ValueError if certain conditions are not
        met.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """ Calculates the area of a square

    Returns:
        the area of a square

    """
    def area(self):
        return self.__size ** 2

    """ Prints square based on its size

    Examples:
        >>>print(# for i in range(3))
        ###
        ###
        ###
    """
    def my_print(self):
        if self.__size == 0:
            print()

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
