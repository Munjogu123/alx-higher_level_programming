#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    listCopy = my_list.copy()
    length = len(my_list)

    if (idx < 0):
        return listCopy

    if (idx >= length):
        return listCopy

    for i in range(length):
        if (i == idx):
            listCopy[i] = element

    return listCopy
