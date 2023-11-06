#!/usr/bin/python3
"""
Class Module
"""


from typing import Any


class MyInt(int):
    """int class subclass"""

    def __eq__(self, __value):
        """Inverted equal method"""
        return super().__ne__(__value)

    def __ne__(self, __value):
        """Inverted notEqual method"""
        return super().__eq__(__value)
