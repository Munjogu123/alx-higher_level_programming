#!/usr/bin/python3
def multiple_returns(sentence):
    if (sentence == ''):
        char = None
    else:
        char = sentence[0]

    res = len(sentence), char
    return res
