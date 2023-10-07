#!/usr/bin/python3


# Print element in the list in reversed order
def print_reversed_list_integer(my_list=[]):
    idx = len(my_list) - 1

    while idx >= 0:
        fmt = str.format("{:d}", my_list[idx])
        print(fmt)
        idx -= 1
