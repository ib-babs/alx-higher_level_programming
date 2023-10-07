#!/usr/bin/python3


# Deletes the item at a specific position in a list.
def delete_at(my_list=[], idx=0):
    if my_list is None:
        return
    if 0 <= idx < len(my_list):
        del my_list[idx]
    return my_list
