#!/usr/bin/python3


# Print element in the list in reversed order
def print_reversed_list_integer(my_list=[]):
    idx = len(my_list) - 1
    if my_list is None:
        return
    while idx >= 0:
        print("{:d}", my_list[idx])
        idx -= 1
