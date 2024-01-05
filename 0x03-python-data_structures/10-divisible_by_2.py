#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if (len(my_list) == 0):
        return None

    res = []
    for i in my_list:
        res.append(i % 2 == 0)

    return res
