#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        fct(*args)
        return fct(*args)
    except Exception as E:
        sys.stderr.write("Exception: {}\n".format(E))
        return None
