#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    len = len(sys.argv) - 1
    if (len == 0):
        print('0 arguments.')
    elif (len == 1):
        print('1 argument:')
    else:
        print('{} arguments:'.format(len))

    i = 1
    while i <= len:
        print(i, ': {}'.format(sys.argv[i]))
        i += 1
