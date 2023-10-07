#!/usr/bin/python3


# Finds the biggest integer of a list.
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    maximun = my_list[0]

    for i in my_list:
        if maximun < i:
            maximun = i
    return maximun
