#!/usr/bin/python3
"""
Function module
"""


def append_write(filename="", text=""):
    """Append file function"""
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
