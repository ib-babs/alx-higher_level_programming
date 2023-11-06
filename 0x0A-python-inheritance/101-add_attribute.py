#!/usr/bin/python3
"""Add attribute to the object
if possible, else raise TypeError"""


def add_attribute(obj, name, value):
    """Define add attribute function"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    if (not hasattr(obj, name)):
        obj.__setattr__(name, value)
