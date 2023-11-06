#!/usr/bin/python3
"""
Method module
"""


def inherits_from(obj, a_class):
    """Define 'inherits_from' function"""
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
