#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)

    if (idx < 0 or idx >= length):
        return listCopy

    listCopy = my_list.copy()

    for i in range(length):
        if (i == idx):
            listCopy[i] = element

    return listCopy
