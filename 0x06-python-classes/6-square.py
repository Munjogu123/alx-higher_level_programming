#!/usr/bin/python3
"""" Defines a square """


class Square:
    """ Creates a private attribute size for the square

    Args:
        size: refers to dimensions of the square

    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ retrieves the value of position

        Returns:
            returns the tuple position
        """
        return self.__position

    @position.setter
    def position(self, value):
        if type(value[0]) is not int or type(value[1] is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value) is not tuple or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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

        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
