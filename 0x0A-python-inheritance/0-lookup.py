#!/usr/bin/python3
"""lookup: returns the list of available
attributes and methods of an object
"""


def lookup(obj):
    """Lookup function"""
    return list(obj.__dict__)
