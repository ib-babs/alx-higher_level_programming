#!/usr/bin/python3


# Print element at index idx
def element_at(my_list, idx):
    return(my_list[idx] if 0 <= idx < len(my_list) else None)
