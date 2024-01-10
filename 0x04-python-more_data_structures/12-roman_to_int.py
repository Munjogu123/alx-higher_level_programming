#!/usr/bin/python3
def roman_to_int(roman_string):
    r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    length = len(roman_string)

    for i in range(length):
        if i + 1 < length and r[roman_string[i]] < r[roman_string[i + 1]]:
            res -= r[roman_string[i]]
        else:
            res += r[roman_string[i]]

    return (res)
