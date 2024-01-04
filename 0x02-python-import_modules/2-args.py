#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    len = len(sys.argv) - 1
    if (len > 1):
        print('{} arguments:'.format(len))
    elif (len == 0):
        print('{} arguments.'.format(len))
    else:
        print('{} argument:'.format(len))

    i = 1
    while i <= len:
        print(i, ': {}'.format(sys.argv[i]))
        i += 1
