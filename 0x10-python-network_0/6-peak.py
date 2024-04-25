#!/usr/bin/python3
""" contains a function that finds the peak value """


def find_peak(list_of_integers):
    """ Finds the peak value in a list """
    length = len(list_of_integers) - 1
    left = 0
    right = length - 1

    if list_of_integers == []:
        return None

    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return list_of_integers[left]
