#!/usr/bin/python3
def weight_average(my_list=[]):
    product = 1
    weight = 0
    sum = 0

    if len(my_list) == 0:
        return 0

    for i in my_list:
        product = i[0] * i[1]
        weight += i[1]
        sum += product

    return (sum / weight)
