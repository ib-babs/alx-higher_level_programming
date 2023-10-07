#!/usr/bin/python3


# Removes all characters c and C from a string.
def no_c(my_string):
    new_string = ''
    for string in my_string:
        if string == 'c' or string == 'C':
            continue
        new_string += string
    return new_string
