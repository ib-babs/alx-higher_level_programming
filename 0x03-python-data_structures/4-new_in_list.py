#!/usr/bin/python3


#  replaces an element in a list at a specific position
#  without modifying the original list
def new_in_list(my_list, idx, element):
    if my_list is None:
        return
    my_list_copy = my_list[:]

    if 0 <= idx < len(my_list):
        my_list_copy[idx] = element
    return my_list_copy
