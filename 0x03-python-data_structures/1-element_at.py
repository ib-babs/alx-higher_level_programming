#!/usr/bin/python3


# Print element at index idx
def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list):
        return None
    return my_list[idx]
