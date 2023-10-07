#!/usr/bin/python3


# Adds 2 tuples.
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a_len = len(tuple_a)
    tuple_b_len = len(tuple_b)
    if tuple_a_len == 0:
        tuple_a = (0, 0)
    if tuple_b_len == 0:
        tuple_b = (0, 0)

    if tuple_a_len < 2:
        tuple_a = (tuple_a[0], 0)
    if tuple_b_len < 2:
        tuple_b = (tuple_b[0], 0)

    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return (result)
