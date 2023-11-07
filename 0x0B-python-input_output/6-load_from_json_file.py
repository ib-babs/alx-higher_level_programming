#!/usr/bin/python3
"""
Function module
"""
import json


def load_from_json_file(filename):
    """load_from_json_file function"""
    with open(filename) as f:
        return (json.load(f))
