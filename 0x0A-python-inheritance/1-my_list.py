#!/usr/bin/python3
"""MyList inherits from `list` class"""


class MyList(list):
    """Define MyList class"""

    def print_sorted(self):
        """Print sorted list in ascending order"""
        print(sorted(self))
