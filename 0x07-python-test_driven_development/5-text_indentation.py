#!/usr/bin/python3
"""Author: Babatunde Ibrahim
`text_indentation: a function that print the result
of the `text` parameter after the operation - Checking
of `.?:` characters has been performed on it
Note: The `text` param must be string, error otherwise"""


def text_indentation(text):
    """Define Text Indentation function
    Arg(text):
        text: string to test the function with"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    read = 0
    while read < len(text):
        print(text[read], end='')
        if text[read] in ".?:":
            print("\n")
            if (text[read + 1] == ' '):
                read += 1
        read += 1
