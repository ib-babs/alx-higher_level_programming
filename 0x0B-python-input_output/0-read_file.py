#!/usr/bin/python3
"""
Function module
"""


def read_file(filename=""):
    """Read file function"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end='')
