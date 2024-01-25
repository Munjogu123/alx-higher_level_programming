#!/usr/bin/python3
"""

This module contains a function that divides a matrix by div variable

"""


def matrix_divided(matrix, div):
    """ Divides matrix by div variable

    Args:
        matrix: 2d list to be divided
        div: the divisor

    Raises:
        TypeError: if div is not an int or float
        if matrix is not a list of lists
        if length of the rows in a matrix vary
        ZeroDivisionError: if div is equal to 0

    Returns:
        a new matrix containing the quotient of the operation
    """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in range(len(matrix) - 1):
        if type(matrix) is not list or type(matrix[i]) is not list:
            raise TypeError
        ("matrix must be a matrix (list of lists) of integers/floats")
        if len(matrix[i + 1]) != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")

    result = [list(map(lambda i: round(i / div, 2), row)) for row in matrix]
    return result
