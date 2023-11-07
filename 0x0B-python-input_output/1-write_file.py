#!/usr/bin/python3
"""
Function module
"""


def write_file(filename="", text=""):
    """Write file function"""
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
