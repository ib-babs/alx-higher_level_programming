#!/usr/bin/python3
"""Author: Babatunde Ibrahim
`say_my_name` function recieves two parameters
<firstname> and <lastname> to print the result
`My name is <firstname> <lastname>`
<firstname> and <lastname> must be of string type"""


def say_my_name(first_name, last_name=""):
    """Define say_my_name function
    Args(first_name, last_name)
    first_name: your firstname and last_name"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
