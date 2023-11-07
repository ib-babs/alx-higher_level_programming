#!/usr/bin/python3
"""
Class module
"""


def class_to_json(obj):
    """Return dict repr"""
    return obj.__dict__
