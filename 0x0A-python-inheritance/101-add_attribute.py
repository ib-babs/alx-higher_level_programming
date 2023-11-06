#!/usr/bin/python3
"""Add attribute to the object
if possible, else raise TypeError"""


def add_attribute(obj, name, value):
    """Define add attribute function"""
    if hasattr(obj, "__dict__") == False:
        raise TypeError("can't add new attribute")
    obj.name = name
    obj.value = value
