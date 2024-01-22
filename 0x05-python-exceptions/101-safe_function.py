#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
        return res
    except (ZeroDivisionError, IndexError, TypeError) as err:
        print("Exception:", err, file=sys.stderr)
        return None
