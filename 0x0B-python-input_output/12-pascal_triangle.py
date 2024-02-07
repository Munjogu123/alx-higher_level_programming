#!/usr/bin/python3
""" This module implements Pascal's triangle """


def pascal_triangle(n):
    """ Implements pascal triangle

    Args:
        n: length of pascal triangle

    Returns:
        list of values of pascal triangle
    """
    if n <= 0:
        return []

    res = [[] for i in range(n)]
    for i in range(n):
        for j in range(i + 1):
            if j < i:
                if j == 0:
                    res[i].append(1)
                else:
                    res[i].append(res[i - 1][j] + res[i - 1][j - 1])
            elif j == i:
                res[i].append(1)

    return res
